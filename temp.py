import random

def generate_random_ip():
    # Generate four random numbers in the range 0-255
    random_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return random_ip

# Generate and print a random IP address
random_ip_address = generate_random_ip()
print(random_ip_address)