"""
Use the flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    """

    :return:
    """
    flight = Flight("SN066", Aircraft("G-EUP", "Airbus A319", num_rows= 22, num_seats_per_row= 6))

    # print(a1.registration(), a1.model()))
    # print(flight.number(), flight.airline())
    # f2 = Flight("SN013")
    # print(f2.number(), f2.airline())
    # # could use: Flight.number(f) horrible notation
    # a1 = Aircraft("G-EUP", "Airbus A319", num_rows= 22, num_seats_per_row= 6)
    # print(a1.registration(), a1.model())
    # pp(f1._seating)
    flight.allocate_seat("02A", "Guido Van Roussum")
    flight.allocate_seat("02F", "Van Roussum")
    flight.allocate_seat("02B", "Van")
    # flight.allocate_seat("02A", "Guido Roussum")
    return flight


def console_card_printer(passenger, seat, flight_number, aircraft):
    """
    Isolate the code to print the boarding pass
    :return:
    """
    output = "| Name: {0}" \
             "Flight: {1}" \
             "Seat: {2}" \
             "Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) -2) + "+"
    border = " |" + " " * (len(output) -2) + " |"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def main():
    """
    Test function
    :return: 
    """
    flight_1 = make_flight()
    pp(flight_1._seating)
    print("Avaliable seats", flight_1.num_available_seats())
    flight_1.make_boarding_class(console_card_printer) # do not include the () we want to pass as a parameter
    # () will execute the function


if __name__ == '__main__':
    main()
    exit(0)