"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string.

    The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    string = ""
    if not s:
        return s
    if s[0].isupper():
        return s
    else:
        if len(s) == 1:
            return s.capitalize()
        lst = list(s)
        first = str(lst[0])
        string += first.capitalize()
        for char in lst[1::]:
            string += char
        return string


def has_seven(nums):
    """
    Whether the list has three 7s and no repeated consecutive elements.

    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if not nums:
        return False
    lst = []
    if nums.count(7) == 3:
        for num in nums:
            if not lst:
                lst.append(num)
            elif num == lst[-1]:
                return False
            else:
                lst.append(num)
        return True
    else:
        return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """
    lst = []
    if not initial_list:
        for i in range(amount):
            lst.append(initial_list)
        return lst
    else:
        for i in range(amount):
            return lst


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    dct = {}
    if not call_log:
        return dct
    call_list = call_log.split(",")
    for call in call_list:
        people = call.split(":")
        amount = len(people)
        for i in range(amount):
            if i == amount:
                break
            if people[i] not in dct:
                dct[people[i]] = [people[i + 1]]
                if len(people) <= 2:
                    break
            else:
                if people[i + 1] not in dct[people[i]]:
                    dct[people[i]].append(people[i + 1])
                    if len(people) <= 2:
                        break
    return dct


print(has_seven([7, 1, 7, 1, 1, 7]))
print(has_seven([7, 1, 7, 1, 7]))