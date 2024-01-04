import random

def random_string_selection_with_weights(strings, weights):
    selected_string = random.choices(strings, weights=weights, k=1)[0]
    return selected_string

# Example usage with three strings and weights:
strings = ["Hello", "World", "Python"]
weights = [50, 30, 20]

# Generate 5 random selections
for _ in range(5):
    selected_value = random_string_selection_with_weights(strings, weights)
    print(f"Selected value: {selected_value}")
