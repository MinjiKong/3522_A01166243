import des
import argparse
import abc
import enum


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
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handler(self, crypto_request) -> (str, bool):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class EncryptionHandler(BaseHandler):
    def handler(self, crypto_request: Request) -> (str, bool):
        des_key = des.DesKey(crypto_request.key)
        string_to_encrypt = b""

        if crypto_request.input_file and self.next_handler:
            try:
                with open(crypto_request.input_file, mode="r", encoding="utf-8") as text_file:
                    string_to_encrypt += text_file.read()
                    text_file.close()
                crypto_request.result = des_key.encrypt(string_to_encrypt)
            except FileNotFoundError:
                return "File not found", False
        elif crypto_request.data_input and self.next_handler:
            crypto_request.result = des_key.encrypt(bytes(crypto_request.data_input, "utf-8")), True
        else:
            return self.next_handler.handler(crypto_request)


class OutputHandler(BaseHandler):
    def handler(self, crypto_request) -> (str, bool):
        if crypto_request.output == "--output print":
            print(crypto_request.result)
        else:
            with open(crypto_request.output[8:], mode="w", encoding="utf-8") as text_file:
                text_file = crypto_request.data_input.write()
                text_file.close()
            if not self.next_handler:
                return "", True
            else:
                self.next_handler.handler(crypto_request)


class DecryptionHandler(BaseHandler):
    def handler(self, crypto_request: Request) -> (str, bool):
        des_key = des.DesKey(crypto_request.key)
        string_to_decrypt = ""

        if crypto_request.input_file and self.next_handler:
            try:
                with open(crypto_request.input_file, mode="r", encoding="utf-8") as text_file:
                    string_to_decrypt += text_file.read()
                    text_file.close()
                crypto_request.result = des_key.decrypt(string_to_decrypt)
            except FileNotFoundError:
                return "File not found", False
        elif crypto_request.data_input and self.next_handler:
            crypto_request.result = des_key.decrypt(bytes(crypto_request.data_input, "utf-8")), True
        else:
            return self.next_handler.handler(crypto_request)


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
        self.encryption_start_handler = None
        self.decryption_start_handler = None

    def execute_request(self, request: Request):
        pass


def main(request: Request):
    pass


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)