def split_array(to_split, bitwise):
    # """
    # Given an array, split either front or back half
    # """
    split = len(to_split)/2
    if bitwise == "F":
        return to_split[:split]
    if bitwise == "B":
        return to_split[split:]

def get_seat(seat_code, columns=None, rows=None):
    # """
    # Given a binary seat code, retrun dict of row, column, seatid
    # """
    if columns is None:
        columns = [x for x in range(8)]
    if rows is None:
        rows = [x for x in range(128)]
    for char in seat_code:
        if char == "F":
            rows = split_array(rows, "F")
        elif char == "B":
            rows = split_array(rows, "B")
        elif char == "R":
            columns = split_array(columns, "B")
        elif char == "L":
            columns = split_array(columns, "F")
    seat_dict = {}
    seat_dict["row"] = rows[0]
    seat_dict["column"] = columns[0]
    seat_dict["seat"] = (seat_dict["row"] * 8) + seat_dict["column"]
    return seat_dict

def all_seats(all_seat_codes):
    seats = []
    for line in all_seat_codes:
        line = line.strip()
        seat = get_seat(line)["seat"]
        seats.append(seat)
    return seats

max(seats)

def find_my_seat(all_seat_codes):
    seats = all_seats(all_seat_codes)
    seats.sorted()
    for possible in range(seats[0], seats[:-1]):
        if possible not in seats:
            if possible+1 in seats and possible-1 in seats:
                return(seat)

