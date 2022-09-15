"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Return the ID code from the input and determine if it is valid.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    id_code = (''.join(filter(str.isdigit, text)))
    if len(id_code) == 11:
        return id_code
    elif len(id_code) > 11:
        return "Too many numbers!"
    elif len(id_code) < 11:
        return "Not enough numbers!"


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    id_code = (''.join(filter(str.isdigit, text)))
    if len(id_code) != 11:
        return "Incorrect ID code!"
    control_algorithm = (int(id_code[0]) * 1 + int(id_code[1]) * 2 + int(id_code[2]) * 3 + int(id_code[3]) * 4 +
                         int(id_code[4]) * 5 + int(id_code[5]) * 6 + int(id_code[6]) * 7 + int(id_code[7]) * 8 +
                         int(id_code[8]) * 9 + int(id_code[9]) * 1) % 11
    if control_algorithm == int(id_code[10]) and control_algorithm < 10:
        return id_code
    if control_algorithm >= 10:
        return "Needs the second algorithm!"
    elif control_algorithm != int(id_code[10]):
        return "Incorrect ID code!"


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"

"""EX03 ID code part 2."""


def is_valid_gender_number(gender_number: int) -> bool:
    """Check if given value is a valid number for gender."""
    if gender_number == 0:
        return False
    elif gender_number > 6:
        return False
    elif gender_number < 1:
        return False
    else:
        return True


def get_gender(gender_ident: int) -> str:
    """Determine the gender from the input."""
    if gender_ident == 1 or gender_ident == 3 or gender_ident == 5:
        return "male"
    if gender_ident == 2 or gender_ident == 4 or gender_ident == 6:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if year_number > 99:
        return False
    elif year_number < 0:
        return False
    else:
        return True


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if month_number > 12:
        return False
    if month_number < 1:
        return False
    else:
        return True


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if birth_number > 999:
        return False
    if birth_number < 1:
        return False
    else:
        return True


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

"""EX03 ID code part 3."""


def is_leap_year(year_check: int) -> bool:
    """Check if given year is leap year."""
    if year_check % 400 == 0:
        return True
    elif year_check % 4 == 0 and year_check % 100 != 0:
        return True
    elif year_check % 100 == 0 and year_check % 400 != 0:
        return False
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    first_digits = 0
    if gender_number == 1 or gender_number == 2:
        first_digits = 18
    if gender_number == 3 or gender_number == 4:
        first_digits = 19
    if gender_number == 5 or gender_number == 6:
        first_digits = 20
    return first_digits * 100 + year_number


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if not is_valid_birth_number(birth_number):
        return "Wrong input!"
    if is_valid_birth_number(birth_number):
        if 0 < birth_number <= 10:
            return "Kuressaare"
        elif 11 <= birth_number <= 20:
            return "Tartu"
        elif 21 <= birth_number <= 220:
            return "Tallinn"
        elif 221 <= birth_number <= 270:
            return "Kohtla-Järve"
        elif 271 <= birth_number <= 370:
            return "Tartu"
        elif 371 <= birth_number <= 420:
            return "Narva"
        elif 421 <= birth_number <= 470:
            return "Pärnu"
        elif 471 <= birth_number <= 710:
            return "Tallinn"
        elif 711 <= birth_number <= 999:
            return "undefined"


if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
