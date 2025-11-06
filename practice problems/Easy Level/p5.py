# 5.Given a list of numbers, use list comprehension to create a new list of only even numbers.

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

even_number_list = [num for num in list_of_numbers if num % 2 == 0]

print (even_number_list)  # Output: [2, 4, 6, 8, 10]