import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Address - field
def generate_emp__field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append()
      return dict_list





#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Employee Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_employee_build(dict, num_records):  
      pass

def generate_table_employee(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      addr_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      addr_data = gtsf.table_generate_id_records(addr_num_records)
      addr_data = generate_table_employee_build(addr_data, addr_num_records)
      return addr_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 