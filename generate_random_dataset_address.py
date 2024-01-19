import pandas as pd
import random
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Address List for Support Functions              ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Address (street line, city, state and country) Components for random generator
street_names = [
    "Maple", "Oak", "Pine", "Cedar", "Elm", "Willow", "Peach", "Cherry", 
    "Magnolia", "Walnut", "Poplar", "Aspen", "Birch", "Spruce", "Hickory",
    "Sycamore", "Chestnut", "Laurel", "Redwood", "Sequoia", "Cypress"
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

country_abbreviations = [
      'US', 'UK', 'CAN', 'AUS', 'GER', 'FRA', 'JPN', 'CHN', 'RUS', 'BRA', 'IND'
]


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Address Functions for Generator                 ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Address Account field
def generate_address_account_field(num_records, len_id_char = 8):
      dict_list = []
      if type(len_id_char) == str:
            if len_id_char.isdigit():
                  zeros_req = int(len_id_char)-1
            else:
                  return Exception(f'Cannot convert the numeric string to a numeric value: {len_id_char}')
      else:
            zeros_req = len_id_char - 1
            
      zeros = "0" * zeros_req
      min = int("1"+zeros)
      max = int("9"*len_id_char) 
      for _ in range(num_records):
            dict_list.append(random.randint(min, max))
      return dict_list

# Generate the Address line fields
def generate_address_fields(num_records):
      dict_addr_street_list = []
      dict_addr_city_list = []
      dict_addr_state_list = []
      dict_addr_zipcode_list = []
  
      for _ in range(num_records):
            addr = gtsf.generate_random_address(street_names, city_names, states).split(", ")
            dict_addr_street_list.append(addr[0])
            dict_addr_city_list.append(addr[1])
            dict_addr_state_list.append(addr[2])
            dict_addr_zipcode_list.append(addr[3])
      return dict_addr_street_list, dict_addr_city_list, dict_addr_state_list, dict_addr_zipcode_list

# Generate the Address Original Country field
def generate_address_original_country_field(num_records, priority_item = 'US', weight_us = 10, weight_oth = 1):
      dict_list = [] 
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(country_abbreviations, priority_item, weight_us, weight_oth))
      return dict_list
     
# Generate the Address Registered Country field 
def generate_address_registered_country_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append('US')
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Address Table                      ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the address table
def generate_table_address_build(dict, num_records):  
      dict['Address ID'] = generate_address_account_field(num_records)
      dict['Address Street'], dict['City'], dict['State'], dict['Zip Code'] = generate_address_fields(num_records)
      dict['Registered Country'] = generate_address_registered_country_field(num_records)
      dict['Original Country'] = generate_address_original_country_field(num_records, weight_us=20)
      return dict

# Main function to run the address table generator
def generate_table_address(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      addr_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      addr_data = gtsf.table_generate_id_records(addr_num_records)
      addr_data = generate_table_address_build(addr_data, addr_num_records)
      return addr_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 