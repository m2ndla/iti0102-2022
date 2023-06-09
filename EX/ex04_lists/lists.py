"""Car inventory. part 1."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    else:
        return all_cars.split(",")


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    all_makes = []
    if all_cars == "":
        return []
    cars = all_cars.split(",")
    for car in cars:
        unit = car.split(" ")
        if unit[0] in all_makes:
            continue
        else:
            all_makes.append(unit[0])
    return all_makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    all_models = []
    if all_cars == "":
        return []
    cars = all_cars.split(",")
    for car in cars:
        unit = car.split(" ", 1)
        if unit[1] in all_models:
            continue
        else:
            all_models.append(unit[1])
    return all_models


def search_by_make(all_cars: str, search: str) -> list:
    """Return the make search result regardless of case sensitivity."""
    cars = all_cars.split(",")
    result_list = []
    for car in cars:
        items = car.split(" ")
        if items[0].casefold() == search.casefold():
            result_list.append(car)
        else:
            continue
    return result_list


def search_by_model(all_cars: str, search: str) -> list:
    """Return all the model search result regardless of case sensitivity."""
    cars = all_cars.split(",")
    result_list = []
    for car in cars:
        car_lowercase = car.casefold()
        items = car_lowercase.split(" ")
        if search.casefold() in items[1:]:
            result_list.append(car)
        else:
            continue
    return result_list


"""Part 3."""


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    result_list = []
    if all_cars == "":
        return result_list
    cars = all_cars.split(",")
    for car in cars:
        items = car.split(" ", 1)
        make = items[0]
        model = items[1]
        if not result_list:
            result_list.append([make, [model]])
        else:
            for existing_make in result_list:
                if make == existing_make[0]:
                    if model in existing_make[1]:
                        break
                    else:
                        existing_make[1].append(model)
                        break
            else:
                result_list.append([make, [model]])
    return result_list


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    new_list = car_make_and_models(all_cars)
    if not car_list:
        return new_list
    print(new_list)
    models = []
    for car in car_list:
        models.append(car[0])
    for car in car_list:
        for new_car in new_list:
            if car[0] == new_car[0]:
                if len(new_car[1]) != 1 or len(new_car[1]) != 2:
                    for many_car in new_car[1]:
                        if many_car not in car[1]:
                            car[1].append(many_car)
                else:
                    car[1].append(new_car[1])
            elif new_car[0] not in models:
                models.append(new_car[0])
                print(new_car[1])
                car_list.append([new_car[0], new_car[1]])
    return car_list


"""Car inventory part 4."""


def makes_and_models_with_duplicates(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models, but with duplicates.

    example:
    input: "Audi A4,Audi A4,Skoda Superb,Skoda Octavia,Skoda Superb,Skoda Octavia,Audi A4"
    output: [['Audi', ['A4', 'A4', 'A4']], ['Skoda', ['Superb', 'Octavia', 'Superb', 'Octavia']]]
    """
    result_list = []
    if all_cars == "":
        return result_list
    cars = all_cars.split(",")
    for car in cars:
        items = car.split(" ", 1)
        make = items[0]
        model = items[1]
        if not result_list:
            result_list.append([make, [model]])
        else:
            for existing_make in result_list:
                if make == existing_make[0]:
                    existing_make[1].append(model)
                    break
            else:
                result_list.append([make, [model]])

    return result_list


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    final_list = []
    cars_list = makes_and_models_with_duplicates(all_cars)
    if all_cars == "":
        return final_list
    for car in cars_list:
        car_tuple = tuple([car[0], len(car[1])])
        final_list.append(car_tuple)
    return final_list


print(number_of_cars("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"))


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    cars_string = ""
    for car in cars:
        make = car[0]
        for model in car[1]:
            cars_string += make + " " + model + ","
    empty = ""
    final_string = cars_string[:-1] + empty
    return final_string


print(car_list_as_string([['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]))
