import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Log Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Log ID field
def generate_log_id_field(num_records, len_id_char = 9):
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

# Generate the Log Time Stamp field
def generate_log_timestamp_field(num_records, min_date = datetime(2010,1,1), max_date = datetime.now()):
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Log User ID field
def generate_log_userid_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("U" + "0"*zero_count + temp_dig_id)
      return dict_list



#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Log Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_log_build(dict, num_records):  
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
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
      return dict

def generate_table_log(min_rand_record_lim = 1, max_rand_record_lim = 1000):
      log_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      log_data = gtsf.table_generate_id_records(log_num_records)
      log_data = generate_table_log_build(log_data, log_num_records)
      return log_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# Random Finance Table
log_df = pd.DataFrame(generate_table_log())
log_df.to_csv("data archive/log data.csv", index=False)
print(log_df)