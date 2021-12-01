import re
import json


# Part 1
def traveler_info(chunked_text: str) -> list:
    """
    Given chunked travel info as a list of strings like
    ["hgt:159cm pid:1234 eyr:2025", "..."]
    create a list of traveler dicts
    """
    travelers = []
    chunks = [string.replace("\n", " ") for string in chunked_text]
    for chunk in chunks:
        # make a list of the text
        split_chunk = chunk.split()
        traveler_info = {}
        for item in split_chunk:
            split_item = item.split(":")
            traveler_info[split_item[0]] = split_item[1]
        travelers.append(traveler_info)
    # print(len(travelers))
    return travelers


def validate_info(traveler_info: dict, required: list) -> list:
    """
    Given a dict of traveler_info
    validate that all required keys are present
    returns list of missing required keys.
    """
    missing = []
    for req in required:
        if req not in traveler_info.keys():
            missing.append(req)
    return missing


def main():
    with open("input.txt", "r") as fopen:
        input_lines = fopen.read()

    chunked = input_lines.split("\n\n")

    all_travelers = traveler_info(chunked)

    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for traveler in all_travelers:
        print("*" * 32)
        print("New traveler!")
        print(traveler)
        missing = validate_info(traveler, required_fields)
        print(f"Missing the following: {missing}")
        if not missing:
            valid_passports += 1
    return valid_passports

# Part  2
# Validators -- all funcs return Bool
# names of funcs are regular


def valid_year(year, lowest, highest):
    return lowest <= year <= highest


def valid_byr(byr):
    return valid_year(int(byr), 1920, 2020)


def valid_iyr(iyr):
    return valid_year(int(iyr), 2010, 2020)


def valid_eyr(eyr):
    return valid_year(int(eyr), 2020, 2030)


def valid_hgt(hgt):
    # will be in format \d+\w+
    match = re.match(r'^(?P<measure>\d+)(?P<type>in|cm)$', hgt)
    if not match:
        return False
    measure = int(match.groupdict()['measure'])
    scale = match.groupdict()['type']
    if scale == "cm":
        return 150 <= measure <= 193
    elif scale == "in":
        return 59 <= measure <= 76
    return False


def valid_hcl(hcl):
    matched = re.match(r"#[0-9a-f]{6}", hcl)
    if not matched:
        return False
    return True


def valid_ecl(ecl, values=None):
    if values is None:
        values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in values:
        return False
    return True


def valid_pid(pass_id):
    matched = re.match(r"[0-9]{9}", pass_id)
    if not matched:
        return False
    return True


def validate_info(traveler_info: dict, required: list) -> list:
    """
    Given a dict of traveler_info
    validate that all required keys are present
    returns list of missing required keys.
    """
    invalid = []
    for req in required:
        if req[0] not in traveler_info.keys():
            invalid.append((req[0], None))
            break
        try:
            is_valid = req[1](traveler_info[req[0]])
            if not is_valid:
                # print(f"INVALID VALUE for {req[0]}")
                invalid.append((req[0], traveler_info[req[0]]))
        except Exception as e:
            print(f"EXCEPTION RAISED on {req[0]}")
            print(e)
            invalid.append((req[0], traveler_info.get(req[0])))
    return invalid


def check_travelers():
    with open("input.txt", "r") as fopen:
        input_lines = fopen.read()

    chunked = input_lines.split("\n\n")

    all_travelers = traveler_info(chunked)

    required_fields = [
        ("byr", valid_byr),
        ("iyr", valid_iyr),
        ("eyr", valid_eyr),
        ("hgt", valid_hgt),
        ("hcl", valid_hcl),
        ("ecl", valid_ecl),
        ("pid", valid_pid)
    ]
    invalid_passports = []
    valid_passports = []
    for traveler in all_travelers:
        print("*" * 32)
        print("New traveler!")
        print(traveler)
        missing = validate_info(traveler, required_fields)
        if missing:
            invalid_passports.append(traveler)
            print(f"invalid values for the following: {missing}")
        else:
            valid_passports.append(traveler)
        #print(f"Current valid passports = {valid_passports}")
    return {"valid": valid_passports, "invalid": invalid_passports}


if __name__ == "__main__":
    print(len(check_travelers()['valid']))
