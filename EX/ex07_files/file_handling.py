"""File handling. Part 1."""


import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(f"{filename}") as text:
        data = text.read()
    return data


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    lst = []
    new_lst = []
    with open(f"{filename}") as text:
        for line in text:
            lst.append(line)
    for item in lst:
        new_lst.append(item.replace("\n", ""))
    return new_lst


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    lst = []
    with open(f"{filename}") as file:
        reader = csv.reader(file, delimiter=",")
        for line in reader:
            lst.append(line)
    return lst


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    import os.path
    file_exists = os.path.exists(f"{filename}")
    if not file_exists:
        with open(f"{filename}", "w") as file:
            file.write(f"{contents}")
    else:
        with open(f"{filename}", "a") as text:
            text.write(f"{contents}")
    pass


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(f"{filename}", "w") as file:
        for line in lines:
            new_line = str(line) + "\n"
            file.write(f"{new_line}")
    with open(f"{filename}", "r+") as text:
        content = text.read()
        content = content.rstrip("\n")
        text.seek(0)
        text.write(content)
        text.truncate()
    pass


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(f"{filename}", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for line in data:
            writer.writerow(line)
    pass


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    result = [["name", "town", "date"]]
    towns = []
    dates = []
    dates_list = read_file_contents_to_list(dates_filename)
    towns_list = read_file_contents_to_list(towns_filename)
    for date in dates_list:
        dates.append(date.split(":"))
    for town in towns_list:
        towns.append(town.split(":"))
    for row in dates:
        result.append([row[0], "-", row[1]])
    for line in towns:
        for item in result:
            if line[0] in item:
                item[1] = line[1]
                break
        else:
            result.append([line[0], line[1], "-"])
    write_csv_file(csv_output_filename, result)
    pass


"""Part 2."""


def create_dictionary(name: str, age: str, sex: str) -> dict:
    """
    Helping function: Creates dictionary in suitable form.

    :param name: Name.
    :param age: Age.
    :param sex: Sex.
    :return: Returns dict in correct form.
    """
    dct = {"name": name, "age": age, "sex": sex}
    return dct


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    result = []
    file = read_csv_file(filename)
    for person in file[1:]:
        name = person[0]
        age = person[1]
        sex = person[2]
        result.append(create_dictionary(name, age, sex))
    return result


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    pass
