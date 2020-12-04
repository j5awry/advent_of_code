def valid_password(password: str, rule: tuple) -> bool: 
    """ 
    given a password and rule, ensure the rule is enforced in the pw 
    passwords are strings 
    rules are tuples of (int(-int), str)
    rules define number of times a letter can be in a password 
    """
    pw_min, pw_max = rule[0].split("-") 
    pw_min = int(pw_min) 
    pw_max = int(pw_max) 
    count = 0 
    for letter in password: 
        if letter == rule[1]: 
            count += 1 
    if count >= pw_min and count <= pw_max: 
        return True 
    return False 

# leaving for posterity, even though I refactored
# after the silly shopkeep
def count_valid_passwords(passwords: list):
    """
    Given a list of passwords in format
    ["int-int str: str"]
    call valid_password()
    """
    count = 0 
    for password in passwords: 
        match_num, letter, pw = password.split() 
        rule = (match_num, letter.strip(":")) 
        if valid_password(pw, rule): 
            count += 1 
    return count


def valid_password_toboggan(password: str, rule: tuple) -> bool: 
    """
    given a password and rule, ensure the rule is enforced in the pw 
    passwords are strings 
    rules are tuples of (int(-int), str)
    rules define placement in a password
    the letter can only occur in ONE position
    No positions is bad and 2 positions is bad 
    """
    # because a foolish shopkeep messed up the rules 
    placement_a, placement_b = rule[0].split("-") 
    placement_a = int(placement_a) 
    placement_b = int(placement_b) 
    valid = 0 
    if password[placement_a-1] == rule[1]: 
        valid += 1 
    if password[placement_b-1] == rule[1]: 
        valid += 1 
    if valid == 1: 
        return True 
    return False


def count_valid_passwords(passwords: list, pw_func=valid_password):
    """
    Given a list of passwords in format
    ["int-int str: str"]
    call pw_func, default is valid_password
    """
    count = 0 
    for password in passwords: 
        match_num, letter, pw = password.split() 
        rule = (match_num, letter.strip(":")) 
        if pw_func(pw, rule): 
            count += 1 
    return count  