import random

# Address Components
street_names = [
    "Maple", "Oak", "Pine", "Cedar", "Elm", "Willow", "Peach", "Cherry", 
    "Magnolia", "Walnut", "Poplar", "Aspen", "Birch", "Spruce", "Hickory",
    "Sycamore", "Chestnut", "Laurel", "Redwood", "Sequoia", "Cypress"
]

street_types = [
    'Street', 'Lane', 'Road', 'St.', 'Ln.', 'Rd.'
]

city_names = [
    "Springfield", "Rivertown", "Meadowville", "Eaglewood", "Sunnyvale", 
    "Greenfield", "Kingsport", "Fairview", "Lakeview", "Ridgecrest", "Westbrook",
    "Easton", "Harborview", "Brookfield", "Cliffside", "Rockville", "Mapleton",
    "Hilltop", "Lakeside", "Rainbow City", "Sunset Hills"
]
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Function to generate a random address
def generate_address():
    street_number = random.randint(100, 9999)
    street_name = random.choice(street_names)
    street_type = random.choice(street_types)
    street = f"{street_number} {street_name} {street_type}"
    city_name = random.choice(city_names)
    state = random.choice(states)
    zip_code = f"{random.randint(10000, 99999)}"
    address = f"{street}, {city_name}, {state}, {zip_code}"
    return address

# Example usage
random_address = generate_address()
print(random_address)
