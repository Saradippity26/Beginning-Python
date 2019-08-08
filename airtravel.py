"""
Create an flight class: Model for aircraft flights
keyword for class: class Class\initializer\constructors in other languages
 (naming conventing for class is uppercase first letter)
"""


class Flight: # Class
    """
    A Flight with a particular passenger aircraft
    """
    # Python does not have private, public and protected variables : __dunders__ are meant for private use
    # _on underscore means meant for private private use in Python
    def __init__(self, number): # Methods
        """
        Initialized Flight number
        :param number: flight number
        :raises: exception on ValueError (or invalid format)
        """
        # implementation details begin with '_'
        # validate flight number:
        # 5 characters long: AADDD A->ALPHA, D->Digit
        if len(number) != 5:
            raise ValueError("Invalid flight number length".format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}".format(number))
        self._number = number

    def number(self):
        """
        (self) first parameter is required and default for any method in a class
        A Flight with a particular passenger aircraft
        :return: flight number
        """
        return self._number[2:]
        # (self) first parameter is required and default for any method in a class

    def airline(self):
        return self._number[:2]


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):

        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration # returns a registration

    def model(self):
        return self._model # returns a model






def main():
        """
        A Flight with a particular passenger aircraft
        Test function
        :return:
        """
        pass

if __name__ == '__main__':
    main()
    exit(0)