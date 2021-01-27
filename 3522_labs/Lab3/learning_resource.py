import abc


class LearningResource(abc.ABC):

    @abc.abstractmethod
    def increment_number_of_copies(self):
        """
        Set's the number of copies of an resource
        :param value: a positive integer
        """
        pass

    @abc.abstractmethod
    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an resource
        :param value: a positive integer
        """
        pass

    @abc.abstractmethod
    def check_availability(self):
        """
        Returns True if the resource is available and False otherwise
        :return: A Boolean
        """
        pass
