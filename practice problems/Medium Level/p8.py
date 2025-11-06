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












# 🧠 Hard Level

# Write a program to implement a stack using a class (with push, pop, peek operations) and then use it to reverse a string.

# Write a function to sort a list of integers using merge sort (implement from scratch, do not use built-in sort).

# Given a directed graph represented as an adjacency list, write a function to perform Depth First Search (DFS) and Breadth First Search (BFS) from a given start node.

# Write a function to solve the Knapsack Problem (0/1 knapsack) using dynamic programming.

# Write a program that reads a large text file (say ~100 MB) and computes the top 10 most frequent words, ignoring case and punctuation.