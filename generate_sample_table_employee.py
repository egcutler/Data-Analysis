import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Employee ID field
def generate_emp_id_field(num_records, len_id_char = 7):
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





#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Employee Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_employee_build(dict, num_records):  
      
      dict['Employee ID'] = generate_emp_id_field(num_records)
      
      return dict

def generate_table_employee(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      emp_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      emp_data = gtsf.table_generate_id_records(emp_num_records)
      emp_data = generate_table_employee_build(emp_data, emp_num_records)
      return emp_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

emp_df = pd.DataFrame(generate_table_employee())
emp_df.to_csv("data archive/address data.csv", index=False)
print(emp_df)