"""Sorting."""
from collections import Counter


def sort_numbers_using_sort(numbers: list[int]):
    """
    Sort numbers in ascending order, using sort() list method.

    Perform sort() on the input list 'numbers', so that the values within the list are in ascending order
     (smallest to largest).
    NB: This function does not have to return value.

    :param numbers: List of integers in a random order.
    """
    numbers.sort()
    pass


def sort_numbers_using_sorted(numbers: list[int]) -> list:
    """
    Sort numbers in ascending order, using sorted() built-in function.

    Return a new sorted list with same values as 'numbers', but in ascending order (smallest to largest).
    NB: The input list 'numbers' must remain unchanged.

    :param numbers: List of integers in a random order.
    :return: Sorted list of numbers in ascending order.
    """
    new_numbers = sorted(numbers)
    return new_numbers


def sort_numbers_reversed(numbers: list[int]) -> list:
    """
    Sort numbers in descending order, using sorted() built-in function.

    Return a new sorted list with same values as 'numbers', but in descending order (smallest to largest).
    NB: The input list 'numbers' must remain unchanged.

    :param numbers: List of integers in a random order.
    :return: Sorted list of numbers in descending order.
    """
    new_numbers = sorted(numbers, reverse=True)
    return new_numbers


def sort_tuples_by_length(tuples: list[tuple]) -> list:
    """
    Sort tuples by their length in descending order, using sorted() built-in function.

    You are given a list of tuples, return a new list where the tuples are ordered based on the amount of elements
     within them (largest to smallest).
    NB: The content of each individual tuple must NOT change.

    Example:
      Input:                                               Output:
        [(1, 1), (1, 1, 1)]                         ->      [(1, 1, 1), (1, 1)]
        [(1, 1), (20000,), (10, 1), (4, 2, 1)]      ->      [(4, 2, 1), (1, 1), (10, 1), (20000,)]
        [([], [1, 2, 3]), ("Hello", 1000, 1, -60)]  ->      [("Hello", 1000, 1, -60), ([], [1, 2, 3])]

    :param tuples: List of tuples in a random order.
    :return: Sorted list of tuples in descending order based on their length.
    """
    sorted_tuples = sorted(tuples, key=len, reverse=True)
    return sorted_tuples


class Person:
    """
    Person class.

    This class is complete, you do not need to add anything new to it.
    """

    def __init__(self, name: str, age: int, height: float):
        """
        Person constructor.

        :param name: First name of the person.
        :param age: Age of the person.
        :param height: Height of the person.
        """
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self) -> str:
        """
        Person representation.

        You may change or remove this method, it is here purely for your convenience.

        :return: A way to represent the Person object as a str when printing it in a list.
        """
        return f"<name={self.name}, age={self.age}, height={self.height}>"


def sort_people_by_name(people: list[Person]) -> list:
    """
    Sort people by their name in alphabetical order.

    See examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    sorted_list = sorted(people, key=lambda x: x.name)
    return sorted_list


def sort_people_by_age_name_height(people: list[Person]) -> list:
    """
    Sort people by their age, name and height.

    Sort people by age, if two people happen to have the same age sort them by name.
    If even their name is the same, sort them by height.
    Everything in ascending order.

    See examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    height_list = sorted(people, key=lambda x: x.height)
    name_list = sorted(height_list, key=lambda x: x.name)
    age_list = sorted(name_list, key=lambda x: x.age)
    return age_list


def people_counter(people: list[Person]):
    return list(map(count, people))

def sort_people_by_popularity_of_name(people: list[Person]) -> list:
    """
    Sort people by the popularity of their name from most popular to least popular.

    The popularity of a name is determined by how many times that name appears in the provided "people" list.
    If a name appears in the list the same number of times as another name, then sort those people by their names
     alphabetically.

    See more examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    alpha_sort = sorted(people, key=lambda x: x.name)
    popularity_sort = sorted(alpha_sort, key=lambda x: (-list(map(lambda y: y.name, people)).count(x.name), x.name))
    return popularity_sort


if __name__ == '__main__':
    ellie = Person("Ellie", 20, 1.74)
    sebastian = Person("Sebastian", 15, 1.7)
    lukas = Person("Lukas", 19, 1.82)
    lukas2 = Person("Lukas", 19, 1.81)
    alex = Person("Alex", 19, 1.8)

    people = [ellie, sebastian, lukas, lukas2, alex]

    print(sort_people_by_name(people))  # -> [alex, ellie, lukas, lukas2, sebastian]
    print(sort_people_by_age_name_height(people))  # -> [sebastian, alex, lukas2, lukas, ellie]
    print(sort_people_by_popularity_of_name(people))  # -> [lukas, lukas2, alex, ellie, sebastian]
