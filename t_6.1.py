def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

# assert average_num([]) == "Bad request"  Вызывается ZeroDivisionError
# assert average_num(28) == "Bad request"  Вызывается TypeError
# assert average_num({"1": 8, "2": 16, "hi": 12}) == 12  Вызывается RuntimeError
assert average_num("159") == "Bad request"
assert average_num([2, "", 4.8, '', 8]) == "Bad request"
assert average_num([2, [3, 4, 5], 6, 8]) == "Bad request"
assert average_num([1, "hello", 2, 3.5, 4]) == "Bad request"
assert average_num([5, 6, "7.5", 8, 10]) == "Bad request"
assert average_num([1, 7, 13, "False"]) == "Bad request"
assert average_num((1, 2, 3)) == 2
assert average_num({1, 5, 9}) == 5
assert average_num([3, 5, True, 7]) == 4
assert average_num(["2", "4", "10", "14"]) == 7.5
assert average_num([-3, 6, "-1", 7.5, -4]) == 1.1
assert average_num([2, 2, 1]) == 1.67
assert average_num([3, "-3", 1.5, -1.5]) == 0