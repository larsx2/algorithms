def is_palindrome(s):
    lo, hi = 0, len(s)-1

    while lo <= hi:
        if s[lo] == s[hi]:
            lo += 1
            hi -= 1
        else:
            return False

    return True


if __name__ == "__main__":

    values = {
        "palindrome": [
            "abccba",
            "aba",
            "012345543210"
        ],
        "non_palindrome": [
            "abc",
            "home"
        ]
    }

    for value in values["palindrome"]:
        assert is_palindrome(value)

    for value in values["non_palindrome"]:
        assert not is_palindrome(value)
