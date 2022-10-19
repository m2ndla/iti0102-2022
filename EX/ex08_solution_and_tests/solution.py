"""EX08 - Solution and tests."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time in range(18, 25) or (time in range(5, 18) and coffee_needed):
        return True
    elif time in range(1, 5):
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    if a == b == c != 5:
        return 5
    if a != b and a != c:
        return 1
    elif a == b or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    most_big_baskets = [0]
    if big_baskets != 0:
        for number in range(1, big_baskets + 1):
            if number * 5 <= ordered_amount:
                most_big_baskets.append(number)
            else:
                break
    needed = int(ordered_amount - int(most_big_baskets[-1] * 5))
    if big_baskets >= (ordered_amount / 5):
        if small_baskets >= (ordered_amount % 5):
            return needed
        else:
            if big_baskets > (ordered_amount / 5):
                return needed
    else:
        if small_baskets >= int(ordered_amount - big_baskets * 5):
            return needed
        else:
            return -1
