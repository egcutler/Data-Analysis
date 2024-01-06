import pandas as pd
import random
import string
from datetime import datetime, timedelta

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

