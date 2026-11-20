import random

rng = random.Random(42)

def generate_control(length):
    return "".join(
        rng.choices("ABC", k=length)
    )