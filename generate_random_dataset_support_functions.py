import pandas as pd
import random
import string
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Standard Support Fields                                  --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# Generate a random record limit for the data frame
def generate_random_record_length(min = 500, max = 100000, seed_val = 50):
      """
      Generate a random integer within a specified range to determine the record length.
      :param min: Minimum value for the record length (default 500).
      :param max: Maximum value for the record length (default 100000).
      :param seed_val: Seed value for random number generator (default 50).
      :return: A random integer within the specified range.
      """
      # Set the seed for reproducibilityS
      random.seed(seed_val)
      # Number of records
      return random.randint(min, max)

# Generate a DataFrame with a random ID Column
def table_generate_id_records(num_records, min_num = 1):
      """
      Generate a dictionary with a key 'ID_Record' containing a list of random integers.
      :param num_records: Number of records to generate.
      :param min_num: Minimum value for the random integers (default 1).
      :return: Dictionary with generated random integers.
      """
      return {'ID_Record': [random.randint(min_num, num_records) for _ in range(num_records)]}

# Random Integer Generator
def generate_random_int(min, max):
      """
      Generate a random integer within a specified range.
      :param min: Minimum value for the random integer.
      :param max: Maximum value for the random integer.
      :return: A random integer within the specified range.
      """
      return random.randint(min, max)

# Random Letter Generator
def generate_random_letter(num_letters):
      """
      Generate a string of random uppercase letters.
      :param num_letters: Number of letters to generate.
      :return: A string of random uppercase letters.
      """
      return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_letters))

# Random Weighted Generator
def generate_random_weighted_string_list(string_list, weight_list):
      """
      Generate a random string from a list of strings, weighted by a corresponding list of weights.
      :param string_list: List of strings to choose from.
      :param weight_list: Corresponding weights for each string in the string_list.
      :return: A randomly chosen string based on the specified weights.
      """
      return random.choices(string_list,weights = weight_list, k=1)[0]

# Function to convert date into datetime format
def function_date_int_to_datetime(date):
      """
      Convert an integer date format into a datetime object.
      :param date: Date in integer format (yyyymmdd).
      :return: Corresponding datetime object.
      :raises Exception: If the date cannot be converted to datetime.
      """
      if isinstance(date, int) and len(str(date)) <= 8 and len(str(date)) >= 6:
            date = str(date)
            yyyy = date[0:4]
            if len(date[4:]) == 2:
                  mm = date[4:5]
                  dd = date[5:]
            elif len(date[4:]) == 4:
                  mm = date[4:6]
                  dd = date[6:]
            elif date[4:5] == '0':
                  mm = date[4:6]
                  dd = date[6:]
            else:
                  mm = date[4:5]
                  dd = date[5:]
            yyyy = int(yyyy)
            mm = int(mm)
            dd = int(dd)
            return datetime(yyyy,mm,dd)
      elif isinstance(date, datetime):
            return date
      else:
            raise Exception(f'{date} cannot be converted to datetime')
      
# Function to generate random date
def generate_date(min_date, max_date):
      """
      Generate a random date within a specified date range.
      :param min_date: Minimum date in the range.
      :param max_date: Maximum date in the range.
      :return: A random date within the specified range.
      :raises Exception: If min_date or max_date is not a datetime object.
      """
      if not isinstance(min_date, datetime):
            raise Exception("min_date is not in the format of datetime objects")
      if not isinstance(max_date, datetime):
            raise Exception("min_date is not in the format of datetime objects")
      date_range = max_date - min_date
      random_days = random.randint(0, date_range.days)
      random_date = min_date + timedelta(days=random_days)
      return random_date

# Function to generate a full name
def generate_full_name(first_name_list, last_name_list):
      """
      Generate a random full name combining a first name and a last name from the provided lists.
      :param first_name_list: List of possible first names.
      :param last_name_list: List of possible last names.
      :return: A randomly generated full name.
      """
      first_name = random.choice(first_name_list)
      last_name = random.choice(last_name_list)
      return f"{first_name} {last_name}"

# Function to generate a random fake phone number
# (to ensure avoidance of pulling a real number, 
# all numbers are uplicated on the same random digit)
def generate_phone_number():
      """
      Generate a fake phone number with all digits being the same random digit.
      :return: A string representing a fake phone number.
      """
      digit = str(random.randint(1,9))
      return digit*10

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Log Functions for Generator                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to generate a random log IP Address
def generate_log_ip_address():
    """
    Generate a random IP address.
    :return: A string representing a random IP address.
    """
    random_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return random_ip

def generate_log_hostname():
    """
    Generate a random hostname.
    :return: A string representing a random hostname.
    """
    chars = string.ascii_lowercase + string.digits
    length = random.randint(7, 15)
    hostname = ''.join(random.choice(chars) for _ in range(length))
    hostname += '.com'
    return hostname

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Legal Support Fields                                     --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


# Function to generate a random legal firm name
def generate_legal_firm_name(surnames, legal_terms):
    """
    Generate a random legal firm name.
    :param surnames: List of possible surnames.
    :param legal_terms: List of possible legal terms.
    :return: A string representing a legal firm name.
    """
    surname1 = random.choice(surnames)
    surname2 = random.choice(surnames)
    legal_term = random.choice(legal_terms)
    # Ensure that the two surnames are not the same
    while surname1 == surname2:
        surname2 = random.choice(surnames)
    return f"{surname1} & {surname2} {legal_term}"



# Function to generate a random legal type
def generate_legal_type_and_def(dict_leg_type):
      """
      Generate a random legal type and its definition from a dictionary.
      :param dict_leg_type: Dictionary of legal types and their definitions.
      :return: A tuple containing a random legal type and its definition.
      """
      type = random.choice(list(dict_leg_type))
      type_def = dict_leg_type[type]
      return type, type_def

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Address Support Fields                                   --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
addr_street_type_list = [
    'Road',
    'Street',
    'Avenue',
    'Boulevard',
    'Drive',
    'Court',
    'Lane',
    'Terrace',
    'Place',
    'Circle',
    'Highway',
    'Square',
    'Trail',
    'Parkway',
    'Alley',
    'Center',
    'Mill',
    'Gardens'
    'Crescent',
    'Crossing',
    'Loop'
]

# Function to generate a random address
def generate_random_address(street_names, city_names, states):
    """
    Generate a random address.
    :param street_names: List of possible street names.
    :param city_names: List of possible city names.
    :param states: List of possible states.
    :return: A string representing a random address.
    """
    street_name = random.choice(street_names)
    street_type = random.choice(addr_street_type_list)
    city_name = random.choice(city_names)
    state = random.choice(states)
    street_number = random.randint(100, 9999)
    zip_code = f"{random.randint(10000, 99999)}"
    return f"{street_number} {street_name} {street_type}, {city_name}, {state}, {zip_code}"

# Priorization function for weighted function support giving one element priority
def prioritize_element(item, priority_item):
      """
      Determine if an item is equal to a priority item, used for sorting purposes.
      :param item: Item to compare.
      :param priority_item: Item to prioritize.
      :return: Tuple indicating whether the item is the priority item or not, and the item itself.
      """
      return (item != priority_item, item)

# Selecting a random value from a list with priorization on a single value
def generate_random_unique_weighted_list(random_list, priority_item, weight_pri = 10, weight_oth = 1):
      """
      Generate a random choice from a list, giving priority to a specific item.
      :param random_list: List of items to choose from.
      :param priority_item: Item to prioritize in the list.
      :param weight_pri: Weight for the priority item (default 10).
      :param weight_oth: Weight for other items in the list (default 1).
      :return: A randomly chosen item from the list, with priority given to the priority item.
      """
      weight_list = []
      weight_list = [weight_pri if item == priority_item else weight_oth for item in random_list]
      return random.choices(random_list, weights=weight_list, k=1)[0]
