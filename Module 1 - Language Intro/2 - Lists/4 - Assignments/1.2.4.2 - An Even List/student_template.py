import random
from statistics import median

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
# Find the length of the list
list_length = len(even_list)
print("The length of the list is", list_length)

# Found the middle indices in the list
mid_upper = list_length // 2
mid_lower = mid_upper - 1
print("The two middle list indices are", mid_lower, "and", mid_upper)

# Correlated the lower middle index to the number in the list
list_mid_low = even_list[mid_lower]
print(list_mid_low)

# Correlated the upper middle index to the number in the list
list_mid_up = even_list[mid_upper]
print(list_mid_up)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (list_mid_up + list_mid_low) / 2

# the average of middle elements is
print("The average is: ", middle_average)
