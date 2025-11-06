# 3. Write a program to check if a given string is a palindrome (reads same forwards and backwards).


def check_palondrome(text):
    # cleaning the str

    cleaned_str = (text.replace(" ", "")).lower()
    # checking palindrome
    reversed_str = cleaned_str[::-1]
    return cleaned_str == reversed_str





string = input("Enter a string: ")
if check_palondrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')