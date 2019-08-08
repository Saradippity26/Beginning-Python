"""
Use the flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def main():
    """
    Test function
    :return: 
    """
    f1 = Flight("SN066", Aircraft("G-EUP", "Airbus A319", num_rows= 22, num_seats_per_row= 6))
    # print(a1.registration(), a1.model()))
    # print(f1.number(), f1.airline())
    # f2 = Flight("SN013")
    # print(f2.number(), f2.airline())
    # # could use: Flight.number(f) horrible notation
    # a1 = Aircraft("G-EUP", "Airbus A319", num_rows= 22, num_seats_per_row= 6)
    # print(a1.registration(), a1.model())
    pp(f1._seating)
    f1.allocate_seat("02A", "Guido Van Roussum")
    f1.allocate_seat("02F", "Van Roussum")
    f1.allocate_seat("02B", "Van")
    # f1.allocate_seat("02A", "Guido Roussum")
    pp(f1._seating)


if __name__ == '__main__':
    main()
    exit(0)