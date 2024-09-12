"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""
from sys import stdin

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE
random_a_std = np.std(random_list_A)
random_b_std = np.std(random_list_B)
print("List A is", random_a_std, "and List B is", random_b_std)

longer_list = []

if random_a_std > random_b_std:
    longer_list = random_list_A
else:
    longer_list = random_list_B

if random_a_std > random_b_std:
    print("List A has a larger deviation than List B")
else:
    print("List B has a larger deviation than List A")

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList
longest_list_is = longer_list
print(longest_list_is)

### YOUR CODE HERE
