# "" -> "" - V
# "a" -> "a" - V
# "ab" -> "ba" - X
# "xx" -> "xx" - V
# "121" -> "121" - V
# "222" -> "222" - V
# "aba" -> "aba" - V
# "baba" -> "abab" - X
# "123" -> "321" - X
# "1234321" -> "1234321" - V

def is_polindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True

    first = s[0]
    last = s[len(s)-1]  # OR s[-1]

    if first == last:
        return is_polindrome(s[1:-1])
    else:
        return False


print(is_polindrome(""))  # T
print(is_polindrome("a"))  # T
print(is_polindrome("x"))  # T
print(is_polindrome("xy"))  # F
print(is_polindrome("aa"))  # T
print(is_polindrome("aba"))  # T
print(is_polindrome("abc"))  # F
print(is_polindrome("abba"))  # T
print(is_polindrome("abca"))  # F
print(is_polindrome("1234321"))  # T
print(is_polindrome("12345321"))  # F

