import sys

def is_palindrome(s):
    s = s.replace(" ", "")   
    s = s.lower()
    return s == s[::-1]


if len(sys.argv) > 1:
    for test in sys.argv[1:]:
        if is_palindrome(test):
            print("True")
        else:
            print("False")
else:
    print("Please provide strings to check for palindromes.")
