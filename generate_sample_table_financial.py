import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Finance List for Support Functions               ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

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

finance_list_type = [
      'Savings', 'Checking'
]

finance_list_payment_method = [
      
]

finance_list_cur = [
      'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'
]

finance_list_approval_status = [
      'Approved', 'Rejected', 'Pending'
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

# Generate the Financial Payment Method field

# Generate the Financial Currency field
def generate_finance_currency_field(num_records, priority_item = 'USD', weight_usd = 10, weight_oth = 1):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(finance_list_cur, priority_item, weight_usd, weight_oth))
      return dict_list

# Generate the Financial Balance field

# Generate the Financial Tax Amount field

# Generate the Financial Reference Number field

# Generate the Financial Budget Code field
def generate_finance_budget_code_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("B" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Financial Approval Status field
def generate_finance_approval_status_field(num_records, weight_a = 10, weight_r = 1, weight_p = 1):
      dict_list = []
      weight_list = [weight_a, weight_r, weight_p]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(finance_list_approval_status,weight_list))
      return dict_list

# Generate the Financial Comments field

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Financial Table                    ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_finance_build(dict, num_records):  
      dict['Finance Account'] = generate_finance_account_field(num_records)
      dict['Transaction ID'] = generate_finance_trans_id_field(num_records)
      dict['Financial Date'] = generate_random_financial_date_field(num_records)
      dict['Category'], dict['Description'] = generate_random_financial_desc_fields(num_records)
      dict['Amount'] = generate_random_financial_ammount_field(num_records, dict['Category'])
      dict['Amount Type'] = generate_random_financial_type_field(num_records)
      #dict['Client Name'] =
      #dict['Payment Method'] =
      dict['Currency'] = generate_finance_currency_field(num_records)
      #dict['Balance'] = 
      #dict['Tax Amount'] =
      #dict['Reference Number'] = 
      dict['Budget Code'] = generate_finance_budget_code_field(num_records)
      dict['Approval Status'] = generate_finance_approval_status_field(num_records)
      #dict['Comments'] =
      return dict

def generate_table_finance(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      finance_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      finance_data = gtsf.table_generate_id_records(finance_num_records)
      finance_data = generate_table_finance_build(finance_data, finance_num_records)
      return finance_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

finance_df = pd.DataFrame(generate_table_finance(1,1000))
finance_df.to_csv("data archive/finance data.csv", index=False)
print(finance_df)