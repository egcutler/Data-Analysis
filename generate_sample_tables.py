import pandas as pd
import random
import string
from datetime import datetime, timedelta

# Generate a random record limit for the data frame
def generate_random_record_length(min = 500, max = 100000, seed_val = 50):
      # Set the seed for reproducibility
      random.seed(seed_val)
      # Number of records
      return random.randint(min, max)

# Generate a DataFrame with a random ID Column
def table_generate_id_records(num_records):
      return {'ID_Record': [random.randint(1, num_records) for _ in range(num_records)]}

# Random Integer Generator
def generate_random_int(min, max):
      return random.randint(min, max)

# Random Letter Generator
def generate_random_letter(num_letters):
      return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_letters))

# Random Weighted Generator
def generate_random_weighted_string_list(string_list, weight_list):
      return random.choices(string_list,weights = weight_list, k=1)[0]

# Lists of words for company name generation
adjectives = [
    "Acme", "Apex", "Global", "Infinite", "Dynamic", "Epic", "Swift", "Mega", 
    "Prime", "Tech", "Fusion", "Alpha", "Omega", "Brilliant", "Vibrant", 
    "Ultimate", "Superior", "Elite", "Innovative", "Creative", "Excellent", 
    "Proactive", "Strategic", "Diverse", "Flexible", "Pioneer", "Visionary"
]
nouns = [
    "Solutions", "Systems", "Enterprises", "Innovations", "Industries", 
    "Services", "Technologies", "Ventures", "Group", "Labs", "Corp", "Co", 
    "Networks", "Enterprises", "Enterprises", "Consulting", "Solutions", 
    "Dynamics", "Solutions", "Solutions", "Technologies", "Group", "Innovations", 
    "Enterprises", "Enterprises", "Enterprises", "Consulting"
]
keywords = [
    "Advanced", "Digital", "Tech", "Innovative", "Global", "Sustainable", 
    "Creative", "Power", "Future", "Precision", "First", "Smart", "Synergy", 
    "Synergistic", "Strategic", "Revolutionary", "Cutting-Edge", "Dynamic", 
    "Dynamic", "Ingenious", "Transformative", "Inspire", "Inspiration", "Progressive", 
    "Evolve", "Evolution", "Impactful", "Forward", "Strive", "Strive", "Vision", "Visionary"
]

# Function to generate a random company name
def generate_company_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    keyword = random.choice(keywords)
    return f"{adjective} {keyword} {noun}"

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
      

#----------------------------------------------------------------------------------
# Generate the business account field
def generate_field_account_field(dict_list_id, num_records):
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

# Generate the business branch field
def generate_field_branch_field(num_records):
      dict_list = []
      # Generating the Account Column
      for _ in range(num_records):
            dict_list.append( str(generate_random_int(0,9)) + generate_random_letter(3) )
      return dict_list

# Generate the Business Status field
def generate_random_status_field(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Business Company Name field
def generate_random_company_name_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(generate_company_name())
      return dict_list

# Generate the Business Account Type field
def generate_random_account_type_field(num_records, num_acct_types = 10):
      dict_list = []
      acct_type_list = []
      for _ in range(num_acct_types):
            acct_type_list.append(generate_random_letter(4))
      for _ in range(num_records):
            dict_list.append(random.choice(acct_type_list))
      return dict_list

# Generate the Business Creation Date field
def generate_random_creation_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      min_date = function_date_int_to_datetime(min_date)
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(generate_date(min_date, max_date))
      return dict_list

# ---
def generate_random_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(generate_date(created_date_list[x], max_date))
      return dict_list

# ---
def generate_random_closed_date_field(num_records, status_list, mod_date_list, max_date = datetime.now()):
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'CLOSED' or status_list[x] == 'HISTORY':
                  dict_list.append(generate_date(mod_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Business TAG field
def generate_random_tag_field(num_records, num_tag = 10):
      dict_list = []
      tag_list = []
      for _ in range(num_tag):
            tag_list.append(generate_random_letter(3))
      for _ in range(num_records):
            dict_list.append(random.choice(tag_list))
      return dict_list

# Generate the business security category field
def generate_random_system_cat_field(num_records, min_cat = 0, max_cat = 5):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.randint(min_cat, max_cat))
      return dict_list


#---------------------------------------------------------------------------------- 
# Generate the Business Table
def table_generate_branch_account(dict, num_records):  
      dict_list_id = dict['ID_Record']
      
      dict['Account'] = generate_field_account_field(dict_list_id, num_records)
      dict['Branch'] = generate_field_branch_field(num_records)
      dict['External ID'] = [branch + account for branch, account in zip(dict['Branch'], dict['Account'])]
      dict['Business Status'] = generate_random_status_field(num_records)
      dict['Company Name'] = generate_random_company_name_field(num_records)
      dict['Account Type'] = generate_random_account_type_field(num_records,9)
      #Date Format: YYYYMMDD
      dict['Creation Date'] = generate_random_creation_date_field(num_records)
      dict['Last Modified Date'] = generate_random_modified_date_field(num_records, dict['Creation Date'])
      dict['Closed Date'] = generate_random_closed_date_field(num_records, dict['Business Status'], dict['Last Modified Date'])
      dict['Business TAG'] = generate_random_tag_field(num_records,3)
      dict['Security Category'] = generate_random_system_cat_field(num_records)

      return dict

#------------------------------------------------------------------------------     

num_records = generate_random_record_length(1, 100000)
data = table_generate_id_records(num_records)
data = table_generate_branch_account(data, num_records)

# Convert to DataFram and export
df = pd.DataFrame(data)
print(df)
df.to_csv("data archive/test.csv", index=False)
