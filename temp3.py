import random
import string

def generate_random_string():
    # Generate a random integer as the first character
    random_integer = random.randint(0, 9)

    # Generate three random letters
    random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))

    # Concatenate the random integer and letters
    result = str(random_integer) + random_letters

    return result

# Example usage:
random_value = generate_random_string()
print(random_value)