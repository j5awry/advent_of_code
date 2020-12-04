import re

# Part 1
def traveler_info(chunked_text: str) -> list:
    """
    Given chunked travel info as a list of strings like
    ["hgt:159cm pid:1234 eyr:2025", "..."]
    create a list of traveler dicts
    """
    travelers = []
    for chunk in chunked_text:
        # make a list of the text
        split_chunk = chunk.split()
        traveler_info = {}
        for item in split_chunk:
            split_item = item.split(":")
            traveler_info[split_item[0]] = split_item[1]
        travelers.append(traveler_info)
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

def valid_byr(byr):
    if int(byr) < 1920:
        return False
    if int(byr) > 2002:
        return False
    return True


def valid_iyr(iyr):
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False
    return True


def valid_eyr(eyr):
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False
    return True


def valid_hgt(hgt):
    # will be in format \d+\w+
    try:
        split = re.findall(r'(\d+)(in|cm)', hgt)[0]
    except IndexError:
        return False
    if split[1] == "cm":
        if int(split[0]) < 150 or int(split[0]) > 193:
            return False
    if split[1] == "in":
        if int(split[0]) < 59 or int(split[0]) > 76:
            return False
    return True


def valid_hcl(hcl):
    matched = re.match(r"#[0-9a-f]{5}", hcl)
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
    matched = re.match(r"[\d]{9}", pass_id)
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
                print(f"INVALID VALUE for {req[0]}")
                invalid.append((req[0], traveler_info[req[0]]))
        except Exception as e:
            print(f"EXCEPTION RAISED on {req[0]}")
            print(e)
            invalid.append((req[0], traveler_info.get(req[0])))
    return invalid


def main():
    with open("input.txt", "r") as fopen:
        input_lines = fopen.read()

    chunked = input_lines.split("\n\n")

    all_travelers = traveler_info(chunked)

    valid_passports = 0
    required_fields = [
        ("byr", valid_byr),
        ("iyr", valid_iyr),
        ("eyr", valid_eyr),
        ("hgt", valid_hgt),
        ("hcl", valid_hcl),
        ("ecl", valid_ecl),
        ("pid", valid_pid)
    ]
    for traveler in all_travelers:
        print("*" * 32)
        print("New traveler!")
        print(traveler)
        missing = validate_info(traveler, required_fields)
        if missing:
            print(f"invalid values for the following: {missing}")
        if not missing:
            valid_passports += 1
    return valid_passports