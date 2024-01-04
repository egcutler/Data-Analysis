import pandas as pd
import random
import string

# Generate a random record limit for the data frame
def generate_random_record_length(min = 500, max = 100000, seed_val = 50):
      # Set the seed for reproducibility
      random.seed(seed_val)
      # Number of records
      return random.randint(min, max)

# Generate a DataFrame with a random ID Column
def table_generate_id_records(num_records):
      return {'ID_Record': [random.randint(1, num_records) for _ in range(num_records)]}

#---
def generate_random_int(min, max):
      return random.randint(min, max)

#---
def generate_random_letter(num_letters):
      return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_letters))

# ---
def generate_random_weighted_string_list(string_list, weight_list):
      return random.choices(string_list,weights = weight_list, k=1)[0]
#----------------------------------------------------------------------------------
# ---
def generate_field_account(dict_list_id, num_records):
      dict_list = []
      # Generating the Account Column
      for x in dict_list_id:
            zero_count = len(str(num_records)) - len(str(x))
            if zero_count == 0:
                  dict_list.append(str(x))
            else: 
                  zero_addon = '0' * zero_count
                  dict_list.append(zero_addon + str(x))
      return dict_list

# ---
def generate_field_branch(num_records):
      dict_list = []
      # Generating the Account Column
      for _ in range(num_records):
            dict_list.append( str(generate_random_int(0,9)) + generate_random_letter(3) )
      return dict_list

# ---
def generate_randome_status(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(generate_random_weighted_string_list(status_list, weight_list))
      return dict_list



#---------------------------------------------------------------------------------- 
# Generate data table: Business
def table_generate_branch_account(dict, num_records):  
      dict_list_id = dict['ID_Record']
      
      dict['Account'] = generate_field_account(dict_list_id, num_records)
      dict['Branch'] = generate_field_branch(num_records)
      dict['External ID'] = [branch + account for branch, account in zip(dict['Branch'], dict['Account'])]
      dict['Business Status'] = generate_randome_status(num_records)

      return dict

#------------------------------------------------------------------------------     

num_records = generate_random_record_length()
data = table_generate_id_records(num_records)
data = table_generate_branch_account(data, num_records)

# Convert to DataFram and export
df = pd.DataFrame(data)
print(df)
df.to_csv("data archive/test.csv", index=False)
