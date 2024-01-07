import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Business Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

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
            dict_list.append( str(gtsf.generate_random_int(0,9)) + gtsf.generate_random_letter(3) )
      return dict_list

# Generate the Business Status field
def generate_random_status_field(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Business Company Name field
def generate_random_company_name_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_company_name())
      return dict_list

# Generate the Business Account Type field
def generate_random_account_type_field(num_records, num_acct_types = 10):
      dict_list = []
      acct_type_list = []
      for _ in range(num_acct_types):
            acct_type_list.append(gtsf.generate_random_letter(4))
      for _ in range(num_records):
            dict_list.append(random.choice(acct_type_list))
      return dict_list

# Generate the Business Creation Date field
def generate_random_creation_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Business Modified Date field
def generate_random_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(gtsf.generate_date(created_date_list[x], max_date))
      return dict_list

# Generate the Business Closed Date field
def generate_random_closed_date_field(num_records, status_list, mod_date_list, max_date = datetime.now()):
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'CLOSED' or status_list[x] == 'HISTORY':
                  dict_list.append(gtsf.generate_date(mod_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Business TAG field
def generate_random_tag_field(num_records, num_tag = 10):
      dict_list = []
      tag_list = []
      for _ in range(num_tag):
            tag_list.append(gtsf.generate_random_letter(3))
      for _ in range(num_records):
            dict_list.append(random.choice(tag_list))
      return dict_list

# Generate the Business Security Category field
def generate_random_system_cat_field(num_records, min_cat = 0, max_cat = 5):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.randint(min_cat, max_cat))
      return dict_list



#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 
#----------              Generate the Business Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_business_build(dict, num_records):  
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



def generate_table_business(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      bus_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      bus_data = gtsf.table_generate_id_records(bus_num_records)
      bus_data = generate_table_business_build(bus_data, bus_num_records)
      return bus_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 