import random

def generate_random_list(num_elements):
    random_list = [random.randint(5, 1200) for _ in range(num_elements)]
    return random_list

num_elements = 22
random_list = generate_random_list(num_elements)
print(random_list)
