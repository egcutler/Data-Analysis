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
      # Set the seed for reproducibilityS
      random.seed(seed_val)
      # Number of records
      return random.randint(min, max)

# Generate a DataFrame with a random ID Column
def table_generate_id_records(num_records, min_num = 1):
      return {'ID_Record': [random.randint(min_num, num_records) for _ in range(num_records)]}

# Random Integer Generator
def generate_random_int(min, max):
      return random.randint(min, max)

# Random Letter Generator
def generate_random_letter(num_letters):
      return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_letters))

# Random Weighted Generator
def generate_random_weighted_string_list(string_list, weight_list):
      return random.choices(string_list,weights = weight_list, k=1)[0]

# Function to convert date into datetime format
def function_date_int_to_datetime(date):
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
      first_name = random.choice(first_name_list)
      last_name = random.choice(last_name_list)
      return f"{first_name} {last_name}"

# Function to generate a random fake phone number
# (to ensure avoidance of pulling a real number, 
# all numbers are uplicated on the same random digit)
def generate_phone_number():
      digit = str(random.randint(1,9))
      return digit*10

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Legal Support Fields                                     --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


# Function to generate a random legal firm name
def generate_legal_firm_name(surnames, legal_terms):
    surname1 = random.choice(surnames)
    surname2 = random.choice(surnames)
    legal_term = random.choice(legal_terms)
    # Ensure that the two surnames are not the same
    while surname1 == surname2:
        surname2 = random.choice(surnames)
    return f"{surname1} & {surname2} {legal_term}"



# Function to generate a random legal type
def generate_legal_type_and_def(dict_leg_type):
      type = random.choice(list(dict_leg_type))
      type_def = dict_leg_type[type]
      return type, type_def

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Address Support Fields                                   --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# Function to generate a random address
def generate_random_address(street_names, city_names, states):
    street_name = random.choice(street_names)
    city_name = random.choice(city_names)
    state = random.choice(states)
    street_number = random.randint(100, 9999)
    zip_code = f"{random.randint(10000, 99999)}"
    return f"{street_number} {street_name} St., {city_name}, {state}, {zip_code}"

# Priorization function for weighted function support giving one element priority
def prioritize_element(item, priority_item):
      return (item != priority_item, item)

# Selecting a random value from a list with priorization on a single value
def generate_random_unique_weighted_list(random_list, priority_item, weight_pri = 10, weight_oth = 1):
      weight_list = []
      
      weight_list = [weight_pri if item == priority_item else weight_oth for item in random_list]
      return random.choices(random_list, weights=weight_list, k=1)[0]
