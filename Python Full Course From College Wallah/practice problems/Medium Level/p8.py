# 8. Given a string, write a program to count the frequency of each character (ignore spaces).

def count_char_frequency(input_string):
    char_counts = {}  # Initialize an empty dictionary to store character counts
    for char in input_string:
        if char != ' ':  # Ignore spaces
            if char in char_counts:
                char_counts[char] += 1  # Increment count if character already exists
            else:
                char_counts[char] = 1  # Add character with count 1 if new
    return char_counts

# Example usage:
my_string = "hello world"
frequencies = count_char_frequency(my_string)
print(frequencies)











