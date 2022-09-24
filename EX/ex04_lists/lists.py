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
        items = car.split(" ", 1)
        if search.casefold() in items[1].casefold():
            result_list.append(car)
        else:
            continue
    return result_list


print(search_by_model("Audi A4,Skoda Superb,Audi A4 B5,Skoda Octavia VR6", "Octavia vr6"))
