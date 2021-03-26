import difflib

from library_item_generator import LibraryItemGenerator


class Catalogue:
    """
    This class simulates a library's catalogue. You can add, find and delete any library resources through this class.
    """

    def __init__(self, resource_list):
        self._resource_list = resource_list
        self._factory_object = LibraryItemGenerator()

    def retrieve_call_number(self, call_number):
        """
        The visible method to get a resource's call number.
        :return: A resource's call number.
        """
        self._retrieve_resource_by_call_number(call_number)

    @property
    def resource_list(self):
        """
        Gets the list of learning resources.

        :return: A list of current books in the Catalogue.
        """
        return self._resource_list

    def find_resources(self, title):
        """
        Find resources with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = [learning_resource.title for learning_resource in self._resource_list]
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def _retrieve_resource_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an resource with
        the given call number from the library.
        :param call_number: a string
        :return: resource object if found, None otherwise
        """
        found_resource = None
        for learning_resource in self._resource_list:
            if learning_resource.call_number == call_number:
                found_resource = learning_resource
                break
        return found_resource

    def add_item(self):
        """
        Add a brand new resource to the library with a unique call number.
        """
        release_date, region_code, issue_number, publisher = "", "", "", ""

        item_type = input("Enter item type: Book, DVD or Journal ")
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter author/director/names of contributors: ")

        if item_type == 'DVD':
            release_date = input("Enter release date: ")
            region_code = input("Enter region code: ")
        elif item_type == 'Journal':
            issue_number = input("Enter issue number: ")
            publisher = input("Enter publisher: ")

        item_dict = {"item_type": item_type, "call_number": call_number,
                     "title": title, "num_copies": num_copies, "author": author,
                     "release_date": release_date, "region_code": region_code,
                     "issue_number": issue_number, "publisher": publisher}

        new_resource = self._factory_object.item_process(item_dict)

        found_resource = self._retrieve_resource_by_call_number(new_resource.call_number)
        if found_resource:
            print(f"Could not add book with call number "
                  f"{new_resource.call_number}. It already exists. ")
        else:
            self._resource_list.append(new_resource)
            print("book added successfully! book details:")
            print(new_resource)

    def remove_item(self, call_number):
        """
        Remove an existing resource from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_resource = self._retrieve_resource_by_call_number(call_number)
        if found_resource:
            self._resource_list.remove(found_resource)
            print(f"Successfully removed {found_resource.title} with "
                  f"call number: {call_number}")
        else:
            print(f"Resource with call number: {call_number} not found.")
