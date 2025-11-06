# 2. Given a list of integers, write a function to find the largest and smallest number.



def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest    

print(find_largest_and_smallest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: (9, 1)