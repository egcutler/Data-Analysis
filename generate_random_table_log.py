import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              --- Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Address - field
def generate_TTT__field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append()
      return dict_list





#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the --- Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_TTT_build(dict, num_records):  
      pass
      #dict['Log ID'] =
      #dict['Time Stamp'] =
      #dict['User ID'] =
      #dict['Event Type'] =
      #dict['Description'] =
      #dict['IP Address'] =
      #dict['Hostname']
      #dict['Severity Level'] =
      #dict['Status'] =
      #dict['Reference ID'] =
      #dict['Old Value'] =
      #dict['New Value'] =
      #dict['Error Code'] =
      #dict['Error Message'] =
      #dict['Module'] =
      #dict['Source'] =

def generate_table_TTT(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      addr_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      addr_data = gtsf.table_generate_id_records(addr_num_records)
      addr_data = generate_table_TTT_build(addr_data, addr_num_records)
      return addr_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 