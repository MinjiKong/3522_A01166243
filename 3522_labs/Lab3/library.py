""" This module houses the library"""
from book import Book
from catalogue import Catalogue


class Library:
    """
    The Library consists of a list of resources and provides an
    interface for users to check out, return and find resources.
    """

    def __init__(self, resource_list):
        """
        Intialize the library with a list of resources.
        :param resource_list: a sequence of resource objects.
        """
        self._catalogue = Catalogue(resource_list)

    def check_out(self, call_number):
        """
        Check out a resource with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_resource = self._catalogue.retrieve_resource_by_call_number(call_number)
        if library_resource.check_availability():
            status = self.reduce_resource_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find resource with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_resource(self, call_number):
        """
        Return a resource with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_resource_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find resource with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of resources, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all resources")
            print("2. Check Out a resource")
            print("3. Return a resource")
            print("4. Find a resource")
            print("5. Add a resource")
            print("6. Remove a resource")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_resources()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the resource"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the resource"
                                    " you wish to return.")
                self.return_resource(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the resource:")
                found_titles = self._catalogue.find_resources(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the resource")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def display_available_resources(self):
        """
        Display all the resources in the library.
        """
        print("Resources List")
        print("--------------", end="\n\n")
        for library_resource in self._catalogue.get_resource_list():
            print(library_resource)

    def reduce_resource_count(self, call_number):
        """
        Decrement the resource count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the resource was found and count decremented, false
        otherwise.
        """
        resource = self._catalogue.retrieve_resource_by_call_number(call_number)
        if resource:
            resource.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_resource_count(self, call_number):
        """
        Increment the resource count for an resource with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the resource was found and count incremented, false
        otherwise.
        """
        resource = self._catalogue.retrieve_resource_by_call_number(call_number)
        if resource:
            resource.increment_number_of_copies()
            return True
        else:
            return False


def generate_test_resources():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    resource_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
    ]
    return resource_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    resource_list = generate_test_resources()
    my_epic_library = Library(resource_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
