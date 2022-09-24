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
        unit = car.split(" ")
        if unit[1] in all_models:
            continue
        else:
            all_models.append(unit[1])
    return all_models
