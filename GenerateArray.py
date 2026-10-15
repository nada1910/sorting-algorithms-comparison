import random
def generate_array(size):
    return random.choices(range(1, 101), k=size)