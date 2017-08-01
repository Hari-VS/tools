import random

def random_array():
    return_array = []
    while len(return_array) < 4:
        random_number = random.randint(1, 9)
        if not random_number in return_array:
            return_array.append(random_number)
    return return_array

my_array = random_array()
print(str(my_array))
