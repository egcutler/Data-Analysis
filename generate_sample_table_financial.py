import random
from datetime import datetime
import generate_tables_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Finance List for Support Functions               ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Finance description dictionary for random generator
finance_dict_desc = {
      'Rent' : ['Rent payment'],
      'Office' : ['Office supplies', 'Office furniture', 'Office Repair'],
      'Utilities' : ['Electricity bill', 'Internet bill', 'Water Bill'],
      'Software' : ['Coding Software', 'Document Software', 'Data Software', 'Media Software'],
      'Travel' : ['Travel reimbursement'],
      'Marketing' : ['Advertising campaign', 'Annual advertising'],
      'Employee' : ['Employee salaries', 'Contract Payment', 'Bonus'],
      'Other Expenses' : ['Shipping', 'Repairs']
}

# Finance account type list for random generator
finance_list_type = [
      'Savings', 'Checking'
]

# Finance payment method list for random generator
finance_list_payment_method = [
      'Bank transfer', 'Credit card', 'Bank transfer', 'Credit card', 
      'PayPal', 'Cash', 'Bank transfer', 'Credit card', 'Bank transfer', 
      'Bank transfer'
]

# Finance currency list for random generator
finance_list_cur = [
      'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'
]

# Finance status list for random generator
finance_list_approval_status = [
      'Approved', 'Rejected', 'Pending'
]

# Finance client name 3 list for random generator
finance_list_name_adjectives = [
    "Acme", "Apex", "Global", "Infinite", "Dynamic", "Epic", "Swift", "Mega", 
    "Prime", "Tech", "Fusion", "Alpha", "Omega", "Brilliant", "Vibrant", 
    "Ultimate", "Superior", "Elite", "Innovative", "Creative", "Excellent", 
    "Proactive", "Strategic", "Diverse", "Flexible", "Pioneer", "Visionary"
]
finance_list_name_nouns = [
    "Solutions", "Systems", "Enterprises", "Innovations", "Industries", 
    "Services", "Technologies", "Ventures", "Group", "Labs", "Corp", "Co", 
    "Networks", "Enterprises", "Enterprises", "Consulting", "Solutions", 
    "Dynamics", "Solutions", "Solutions", "Technologies", "Group", "Innovations", 
    "Enterprises", "Enterprises", "Enterprises", "Consulting"
]
finance_list_name_keywords = [
    "Advanced", "Digital", "Tech", "Innovative", "Global", "Sustainable", 
    "Creative", "Power", "Future", "Precision", "First", "Smart", "Synergy", 
    "Synergistic", "Strategic", "Revolutionary", "Cutting-Edge", "Dynamic", 
    "Dynamic", "Ingenious", "Transformative", "Inspire", "Inspiration", "Progressive", 
    "Evolve", "Evolution", "Impactful", "Forward", "Strive", "Strive", "Vision", "Visionary"
]

# Finance comments list for random generator
finance_comment_list = [
    'Monthly rent, For office stationery', 'Monthly bill, Business dinner', 
    'Annual subscription', 'Team travel expense', 'Online ads, New chairs & desks', 
    'Monthly internet', 'Monthly payroll processing', 'Quarterly tax payments',
    'Annual software licensing fees', 'Office renovation costs', 
    'Client entertainment expenses', 'Employee training and development', 
    'Insurance premiums, Monthly cleaning services', 'Marketing campaign expenses',
    'Technology upgrades, Hardware purchases', 'Legal consultation fees',
    'Utilities and maintenance', 'Conference and event sponsorships',
    'Employee health and wellness programs', 'Transportation and logistics costs',
    'Research and development investments', 'Charitable donations and sponsorships',
    'Security services, Emergency funds allocation'
]

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Financial Functions for Generator               ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Financial Account field
def generate_finance_account_field(num_records, len_id_char = 7):
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

# Generate the Financial Transction ID field
def generate_finance_trans_id_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("T" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Financial Date field
def generate_random_financial_date_field(num_records, min_date = datetime(2010,1,1), max_date = datetime.now()):
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Financial Description fields
def generate_random_financial_desc_fields(num_records):
      dict_list_cat = []
      dict_list_desc = []
      temp_list_cat = list(finance_dict_desc.keys())
      for _ in range(num_records):
            temp_random_cat = random.choice(temp_list_cat)
            dict_list_cat.append(temp_random_cat)
            dict_list_desc.append(random.choice(finance_dict_desc[temp_random_cat]))
      return dict_list_cat, dict_list_desc

# Generate the Financial Amount field
def generate_random_financial_ammount_field(num_records, financial_cat_list, min_emp = 50000, max_emp = 150000, min_oth = 100, max_oth = 10000):
      dict_list = []
      for x in range(num_records):
            if financial_cat_list[x] == "Employee":
                  dict_list.append(random.randint(min_emp, max_emp))
            else:
                  dict_list.append(random.randint(min_oth, max_oth))
      return dict_list

# Generate the Financial Account Type field
def generate_random_financial_type_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(finance_list_type))
      return dict_list

# Generate the Financial Client field
def generate_random_financial_client_name_field(num_records):
      dict_list = []
      for _ in range(num_records):
            adjective = random.choice(finance_list_name_adjectives)
            noun = random.choice(finance_list_name_nouns)
            keyword = random.choice(finance_list_name_keywords)
            dict_list.append(f"{adjective} {keyword} {noun}")
      return dict_list

# Generate the Financial Payment Method field
def generate_finance_payment_method_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(finance_list_payment_method))
      return dict_list

# Generate the Financial Currency field
def generate_finance_currency_field(num_records, priority_item = 'USD', weight_usd = 10, weight_oth = 1):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(finance_list_cur, priority_item, weight_usd, weight_oth))
      return dict_list

# Generate the Financial Balance field
def generate_finance_budget_field(num_records, min_budg = 1000, max_budg = 100000):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.randint(min_budg, max_budg))
      return dict_list

# Generate the Financial Budget Code field
def generate_finance_budget_code_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("B" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Financial Reference Number field
def generate_finance_reference_number_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("R" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Financial Approval Status field
def generate_finance_approval_status_field(num_records, weight_a = 10, weight_r = 1, weight_p = 1):
      dict_list = []
      weight_list = [weight_a, weight_r, weight_p]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(finance_list_approval_status,weight_list))
      return dict_list

# Generate the Financial Comments field
def generate_finance_comment_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(finance_comment_list))
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Financial Table                    ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the finance table
def generate_table_finance_build(dict, num_records):  
      dict['Finance Account'] = generate_finance_account_field(num_records)
      dict['Transaction ID'] = generate_finance_trans_id_field(num_records)
      # - - - Date Format: YYYYMMDD - - -
      dict['Financial Date'] = generate_random_financial_date_field(num_records)
      # - - - - - - - - - - - - - - - - -
      dict['Category'], dict['Description'] = generate_random_financial_desc_fields(num_records)
      dict['Amount'] = generate_random_financial_ammount_field(num_records, dict['Category'])
      dict['Amount Type'] = generate_random_financial_type_field(num_records)
      dict['Client Name'] = generate_random_financial_client_name_field(num_records)
      dict['Payment Method'] = generate_finance_payment_method_field(num_records)
      dict['Currency'] = generate_finance_currency_field(num_records)
      dict['Balance'] = generate_finance_budget_field(num_records)
      dict['Budget Code'] = generate_finance_budget_code_field(num_records)
      dict['Approval Status'] = generate_finance_approval_status_field(num_records)
      dict['Reference Number'] = generate_finance_reference_number_field(num_records)
      dict['Comments'] = generate_finance_comment_field(num_records)
      return dict

# Main function to run the finance table generator
def generate_table_finance(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      finance_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      finance_data = gtsf.table_generate_id_records(finance_num_records)
      finance_data = generate_table_finance_build(finance_data, finance_num_records)
      return finance_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 