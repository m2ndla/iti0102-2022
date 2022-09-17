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
    control_algorithm = (int(id_code[0]) * 1 + int(id_code[1]) * 2 + int(id_code[2]) * 3 + int(id_code[3]) * 4
                         + int(id_code[4]) * 5 + int(id_code[5]) * 6 + int(id_code[6]) * 7 + int(id_code[7]) * 8
                         + int(id_code[8]) * 9 + int(id_code[9]) * 1) % 11
    if control_algorithm == int(id_code[10]) and control_algorithm < 10:
        return id_code
    elif control_algorithm >= 10:
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


def get_gender(gender_number: int) -> str:
    """Determine the gender from the input."""
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
        return "male"
    if gender_number == 2 or gender_number == 4 or gender_number == 6:
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

"""EX03 ID code part 4."""


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    code_numbers_only = (''.join(filter(str.isdigit, id_code)))
    if the_first_control_number_algorithm(code_numbers_only) == id_code:
        return True
    if the_first_control_number_algorithm(code_numbers_only) == "Needs the second algorithm!":
        second_algorithm = (int(code_numbers_only[0]) * 3 + int(code_numbers_only[1]) * 4
                            + int(code_numbers_only[2]) * 5 + int(code_numbers_only[3]) * 6
                            + int(code_numbers_only[4]) * 7 + int(code_numbers_only[5]) * 8
                            + int(code_numbers_only[6]) * 9 + int(code_numbers_only[7]) * 1
                            + int(code_numbers_only[8]) * 2 + int(code_numbers_only[9]) * 3) % 11
        if second_algorithm == 10 and int(id_code[10]) == 0:
            return True
        if second_algorithm == int(id_code[10]):
            return True
        if second_algorithm != int(id_code[10]):
            return False
    if the_first_control_number_algorithm(id_code) == "Incorrect ID code!":
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    full_year = get_full_year(gender_number, year_number)
    if month_number == 2:
        if is_leap_year(full_year):
            if 1 <= day_number <= 29:
                return True
        if not is_leap_year(full_year):
            if 1 <= day_number <= 28:
                return True
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8:
        if 1 <= day_number <= 31:
            return True
    if month_number == 10 or month_number == 12:
        if 1 <= day_number <= 31:
            return True
    if month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        if 1 <= day_number <= 30:
            return True
    if month_number > 12:
        return False
    else:
        return False


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    code_numbers_only = (''.join(filter(str.isdigit, id_code)))
    gender_number = int(code_numbers_only[0])
    year_number = int(code_numbers_only[1] + code_numbers_only[2])
    month_number = int(code_numbers_only[3] + code_numbers_only[4])
    day_number = int(code_numbers_only[5] + code_numbers_only[6])
    birth_number = int(code_numbers_only[7] + code_numbers_only[8] + code_numbers_only[9])
    if is_valid_gender_number(gender_number):
        if is_valid_day_number(gender_number, year_number, month_number, day_number):
            if is_valid_birth_number(birth_number):
                if is_valid_control_number(code_numbers_only):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def get_full_date(gender_number: int, day_number: int, month_number: int, year_number: int) -> str:
    """Get date in dd.mm.yyyy format."""
    full_year = get_full_year(gender_number, year_number)
    full_date = ""
    if day_number < 10:
        full_date = "0" + str(day_number) + "." + str(month_number) + "." + str(full_year)
    if month_number < 10:
        full_date = str(day_number) + "." + "0" + str(month_number) + "." + str(full_year)
    if day_number < 10 and month_number < 10:
        full_date = "0" + str(day_number) + "." + "0" + str(month_number) + "." + str(full_year)
    if day_number > 10 and month_number > 10:
        full_date = str(day_number) + "." + str(month_number) + "." + str(full_year)
    if is_valid_gender_number(gender_number):
        if is_valid_day_number(gender_number, year_number, month_number, day_number):
            return full_date


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    code_numbers_only = (''.join(filter(str.isdigit, id_code)))
    gender_number = int(code_numbers_only[0])
    year_number = int(code_numbers_only[1] + code_numbers_only[2])
    month_number = int(code_numbers_only[3] + code_numbers_only[4])
    day_number = int(code_numbers_only[5] + code_numbers_only[6])
    birth_number = int(code_numbers_only[7] + code_numbers_only[8] + code_numbers_only[9])
    gender = get_gender(gender_number)
    date = get_full_date(gender_number, day_number, month_number, year_number)
    place = get_birth_place(birth_number)
    if is_id_valid(code_numbers_only):
        return "This is a " + gender + " born on " + date + " in " + place + "."
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
