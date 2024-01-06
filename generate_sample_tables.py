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

# Company Name Part1: lists of words for company name generation
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

# Company Name Part2: function to generate a random company name
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
      
# Company Name Part1: Lists of words for legal firm name generation
surnames = [
    "Anderson", "Baker", "Carter", "Davis", "Evans", "Fisher", "Garcia", 
    "Harris", "Jackson", "King", "Lewis", "Martin", "Nelson", "Owens", 
    "Parker", "Quinn", "Roberts", "Smith", "Taylor", "Underwood", "Vasquez", 
    "Williams", "Young", "Zimmerman"
]

legal_terms = [
    "Legal", "Law", "Justice", "Advocates", "Solicitors", "Counsel", 
    "Barristers", "Attorneys", "Partners", "Associates", "Consultants", 
    "Advisors", "Counselors", "Litigators", "Defenders", "Prosecutors"
]

# Company Name Part2: function to generate a random legal firm name
def generate_legal_firm_name():
    surname1 = random.choice(surnames)
    surname2 = random.choice(surnames)
    legal_term = random.choice(legal_terms)
    # Ensure that the two surnames are not the same
    while surname1 == surname2:
        surname2 = random.choice(surnames)
    return f"{surname1} & {surname2} {legal_term}"

# Type Part 1: list of words for legal type generator

dict_leg_type = {
      'BANK' : 'Bank Division',
      'CREDIT' : 'Credit Account',
      'TRADR' : 'Trader credential account',
      'AFFRS' : 'Affairs',
      'AFF' : 'Available Funds File',
      'CORP' : 'Corporation Division',
      'AG' : 'Agriculture',
      'ADVIS' : 'Legal Advisor',
      'BENE' : 'Beneficiary credentail for investment',
      'AGENT' : 'An agent bank acts as a bank performing some \
specific duties on behalf of another party',
      'GUNTE' : 'The bank guarantee means that the lender will \
ensure that the liabilities of a debtor will be met. In other \
words, if the debtor fails to settle a debt, the bank will cover it',
      'TTEE' : 'In the case of the certificate of deposit, the \
trustee is most likely someone charged with taking care of the \
money until the person it is intended for comes of an age to receive it',
      'AFD' : 'Allowance For Depreciation'
}


# Type Part 2: function to generate a random legal type
def generate_legal_type_and_def():
      type = random.choice(list(dict_leg_type))
      type_def = dict_leg_type[type]
      return type, type_def


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#----------              Business Functions for Generator                ---------- 

# Generate the Business Account field
def generate_account_field(dict_list_id, num_records):
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

# Generate the Business Branch field
def generate_random_branch_field(num_records):
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

# Generate the Business Modified Date field
def generate_random_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(generate_date(created_date_list[x], max_date))
      return dict_list

# Generate the Business Closed Date field
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

# Generate the Business Security Category field
def generate_random_system_cat_field(num_records, min_cat = 0, max_cat = 5):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.randint(min_cat, max_cat))
      return dict_list



#----------              Legal Functions for Generator                   ---------- 
# Generate the Legal ID Field
def generate_legal_account_field(num_records, len_id_char = 8):
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

def generate_legal_firm_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(generate_legal_firm_name())
      return dict_list

def generate_legal_type_and_def_field(num_records):
      dict_list_type = []
      dict_list_def = []
      for _ in range(num_records):
            le_type, le_type_def = generate_legal_type_and_def()
            dict_list_type.append(le_type)
            dict_list_def.append(le_type_def)
      return dict_list_type, dict_list_def

# Generate the Legal Status field
def generate_legal_status_field(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Legal Creation Date field
def generate_legal_creation_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      min_date = function_date_int_to_datetime(min_date)
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(generate_date(min_date, max_date))
      return dict_list

# Generate the Legal Modified Date field
def generate_legal_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(generate_date(created_date_list[x], max_date))
      return dict_list

# Generate the Legal Closed Date field
def generate_legal_closed_date_field(num_records, status_list, mod_date_list, max_date = datetime.now()):
      max_date = function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'CLOSED' or status_list[x] == 'HISTORY':
                  dict_list.append(generate_date(mod_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Legal Tax Category Field
def generate_legal_tax_cat_field(num_records):
      dict_list=[]
      le_tax_cat_list = ['G','M','N','I','D','Ba', 'Bt']
      for _ in range(num_records):
            dict_list.append(random.choice(le_tax_cat_list))
      return dict_list

# Generate the Legal IRS TIN ID field
def generate_legal_irs_tin_id_field(num_records, len_id_char = 7):
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
            dict_list.append(generate_random_int(min, max))
      return dict_list

# Generate the Legal MPID field
def generate_legal_mpid_field(num_records, len_id_char = 7):
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
            dict_list.append(generate_random_int(min, max))
      return dict_list

# Generate the Legal GIIN ID field
def generate_legal_giin_id_field(num_records, len_id_char = 7):
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
            dict_list.append(generate_random_int(min, max))
      return dict_list



#----------              Tax Functions for Generator                     ---------- 


#----------              Employee Functions for Generator                ---------- 

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

#----------              Generate the Business Table                     ---------- 
def generate_table_business(dict, num_records):  
      dict_list_id = dict['ID_Record']
      dict['Account'] = generate_account_field(dict_list_id, num_records)
      dict['Branch'] = generate_random_branch_field(num_records)
      dict['External ID'] = [branch + account for branch, account in zip(dict['Branch'], dict['Account'])]
      dict['Business Status'] = generate_random_status_field(num_records)
      dict['Company Name'] = generate_random_company_name_field(num_records)
      dict['Account Type'] = generate_random_account_type_field(num_records,9)
      # Date Format: YYYYMMDD
      dict['Creation Date'] = generate_random_creation_date_field(num_records)
      dict['Modified Date'] = generate_random_modified_date_field(num_records, dict['Creation Date'])
      dict['Closed Date'] = generate_random_closed_date_field(num_records, dict['Business Status'], dict['Modified Date'])
      # - - - - - - - - - - -
      dict['Business TAG'] = generate_random_tag_field(num_records,3)
      dict['Security Category'] = generate_random_system_cat_field(num_records)
      return dict

bus_num_records = generate_random_record_length(1, 10)
bus_data = table_generate_id_records(bus_num_records)
bus_data = generate_table_business(bus_data, bus_num_records)

bus_df = pd.DataFrame(bus_data)
#print(bus_df)
bus_df.to_csv("data archive/business data.csv", index=False)



#----------              Generate the Legal Table                       ---------- 
def generate_table_legal(dict, num_records):
      dict_list_id = dict['ID_Record']
      
      dict['Legal Account'] = generate_legal_account_field(num_records, 8)
      dict['Legal Firm'] = generate_legal_firm_field(num_records)
      dict['Legal Type'], dict['Legal Type Def'] = generate_legal_type_and_def_field(num_records)
      dict['Legal Status'] = generate_legal_status_field(num_records)
      # Date Format: YYYYMMDD
      dict['LE Creation Date'] = generate_legal_creation_date_field(num_records)
      dict['LE Modified Date'] = generate_legal_modified_date_field(num_records, dict['LE Creation Date'])
      dict['LE Closed Date'] = generate_legal_closed_date_field(num_records, dict['Legal Status'], dict['LE Modified Date'])
      dict['Legal Tax Category'] = generate_legal_tax_cat_field(num_records)
      dict['IRS TIN ID'] = generate_legal_irs_tin_id_field(num_records)
      dict['MPID'] = generate_legal_mpid_field(num_records, 6)
      dict['GIIN ID'] = generate_legal_giin_id_field(num_records, 6)
      return dict

      

le_num_records = generate_random_record_length(1, 10)
le_data = table_generate_id_records(le_num_records)
le_data = generate_table_legal(le_data, le_num_records)

le_df = pd.DataFrame(le_data)
print(le_df)
le_df.to_csv("data archive/legal data.csv", index=False)



# Generate the Tax Table
def generate_table_tax():
      pass




# Generate the Employee Table
def generate_table_emp():
      pass

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 
# Convert to DataFram and export