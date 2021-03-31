import des
import argparse
import abc
import enum
import ast


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """
    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


class BaseHandler(abc.ABC):
    """
    Base handler class that sets up the framework each handler class should have. (- = attributes, * = methods)
    - next_handler: Stores the next handler in the chain
    * handler: The method that this handler class uses, should return the result of the next handler stored in the class
    * set_handler: Sets the next handler that this class will use
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handler(self, crypto_request) -> (str, bool):
        """
        The handler that all inherited handler classes will use. Should return the next handler in the chain.
        @param: Request
        return: The next handler or None if the chain is finished
        """
        pass

    def set_handler(self, handler):
        """
        Setter for the handler.
        @param: Handler
        """
        self.next_handler = handler


class EncryptionHandler(BaseHandler):
    """
    Encryption handler for handling commands that are specified to be encrypted.
    """
    def handler(self, crypto_request: Request) -> (str, bool):
        """
        Encrypts the requested data, will either return the next handler (output handler) or catch an Exception
        @precondition: Request must have all attributes not equal to None, except for Data and Input file, in which
                       either or must be not equal to None.
        @param: Request
        return: The next handler (Handler)
        """
        des_key = des.DesKey(bytes(crypto_request.key, "utf-8"))

        if crypto_request.input_file:
            try:
                with open(crypto_request.input_file, mode="r", encoding="utf-8") as text_file:
                    string_to_encrypt = text_file.read()
                    text_file.close()
                crypto_request.result = des_key.encrypt(bytes(string_to_encrypt, "utf-8"), padding=True)
                return self.next_handler.handler(crypto_request)
            except FileNotFoundError as e:
                print(e)
            except AssertionError as e:
                print(e)
        elif crypto_request.data_input:
            try:
                crypto_request.result = des_key.encrypt(bytes(crypto_request.data_input, "utf-8"), padding=True)
                return self.next_handler.handler(crypto_request)
            except AssertionError as e:
                print(e)


class OutputHandler(BaseHandler):
    """
    Output handler for handling the received encrypted or decrypted data.
    """
    def handler(self, crypto_request) -> (str, bool):
        """
        Handles the output for the request, the request is either printed or written to a new text file with its name
        specified in the Request.
        @precondition: Request must have all attributes not equal to None, except for Data and Input file, in which
                       either or must be not equal to None.
        @param: Request
        return: None
        """
        if crypto_request.output == "print":
            print(crypto_request.result)
        else:
            with open(crypto_request.output, mode="w", encoding="utf-8") as text_file:
                text_file.write(crypto_request.result)
                text_file.close()


class DecryptionHandler(BaseHandler):
    """
    Decryption handler for handling commands that are specified to be decrypted
    """
    def handler(self, crypto_request: Request) -> (str, bool):
        """
        Decrypts the requested data, will either return the next handler (output handler) or catch an Exception.
        @precondition: Request must have all attributes not equal to None, except for Data and Input file, in which
                       either or must be not equal to None.
        @param: Request
        return: The next handler (Handler)
        """
        des_key = des.DesKey(bytes(crypto_request.key, "utf-8"))

        if crypto_request.input_file and self.next_handler:
            try:
                with open(crypto_request.input_file, mode="r") as text_file:
                    string_to_decrypt = text_file.read()
                    text_file.close()
                crypto_request.result = des_key.decrypt(ast.literal_eval(string_to_decrypt), padding=True)\
                    .decode("utf-8")
                return self.next_handler.handler(crypto_request)
            except FileNotFoundError as e:
                print(e)
            except AssertionError as e:
                print(e)
        elif crypto_request.data_input and self.next_handler:
            try:
                crypto_request.result = des_key.decrypt(ast.literal_eval(crypto_request.data_input), padding=True)\
                    .decode("utf-8")
                return self.next_handler.handler(crypto_request)
            except AssertionError as e:
                print(e)


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self):
        self.encryption_start_handler = EncryptionHandler()
        self.decryption_start_handler = DecryptionHandler()
        self.output_start_handler = OutputHandler()

    def execute_request(self, request: Request):
        self.encryption_start_handler.set_handler(self.output_start_handler)
        self.decryption_start_handler.set_handler(self.output_start_handler)

        if request.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.handler(request)
        else:
            self.decryption_start_handler.handler(request)


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)