import random

def generate_code():
    lettters = ['A','B','C','D']
    return random.choice(lettters) + random.choice(lettters) + random.choice(lettters)