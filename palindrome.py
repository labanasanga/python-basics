def is_palindrome(s):
    s = s.replace ("hello","world "). lower()
    return s == s[::-1]

string = input("Enter a string: ")
print(is_palindrome(string))









