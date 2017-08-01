import random

# this script outputs four random integers between 1 and 9 for an
# arithmetic game

def random_array():
    # create array of four random numbers
    return_array = []
    while len(return_array) < 4:
        random_number = random.randint(1, 9)
        if not random_number in return_array:
            return_array.append(random_number)
    return return_array

my_array = random_array()
print(str(my_array))
