import string as s

def is_palindrome(string: str) -> bool:
    if isinstance(string, str):
        string = string.lower()
        for symbol in string:
            if symbol in s.punctuation + s.whitespace:
                string = string.replace(symbol, '')
        revstr = ""
        for ind in range(len(string) - 1, -1, -1):
            revstr += string[ind]
        return string == revstr
    return "Это не строка"

assert is_palindrome(True) == "Это не строка"
assert is_palindrome(34.9) == "Это не строка"
assert is_palindrome("") == True
assert is_palindrome("s") == True
assert is_palindrome("f.....l,,.;l      f") == True
assert is_palindrome("9kgh3m 3h gk 9.") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("Лёша на полке, клопа, нашёл! ") == True
assert is_palindrome("Hello, world") == False
assert is_palindrome("Hi hi") == False
assert is_palindrome("ghjgh") == False