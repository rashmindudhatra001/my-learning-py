# 6. Write a function that takes a list of numbers and returns a dictionary with the number of occurrences of each number.

def count_occurrences(numbers_list):
    """
    Counts the occurrences of each number in a list and returns a dictionary.

    Args:
        numbers_list: A list of numbers.

    Returns:
        A dictionary where keys are the numbers from the list and values are
        their respective counts of occurrences.
    """
    occurrence_dict = {}
    for number in numbers_list:
        occurrence_dict[number] = occurrence_dict.get(number, 0) + 1
    return occurrence_dict

# Example usage:
my_numbers = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1]
occurrence_counts = count_occurrences(my_numbers)
print(f"The original list: {my_numbers}")
print(f"The occurrence counts: {occurrence_counts}")

another_list = [5, 5, 5, 0, 0, 7]
another_counts = count_occurrences(another_list)
print(f"Another list: {another_list}")
print(f"Its occurrence counts: {another_counts}")













































































