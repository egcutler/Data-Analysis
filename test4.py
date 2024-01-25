import pandas as pd
import generate_random_dataset_support_functions as grdfs
import generate_random_dataset_business as grdb
import generate_random_dataset_legal as grdle
import generate_random_dataset_address as grda
import generate_random_dataset_employee as grde
import generate_random_dataset_tax as grdt
import generate_random_dataset_financial as grdf
import generate_random_dataset_log as grdlo
import generate_random_data_relationship as grdr
import generate_random_data_analysis_conditions as grdac

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generator the IDs and number of records          ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_basic(min_rand_record_lim = 1, max_rand_record_lim = 1000):
      num_records = grdfs.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      id_dict= grdfs.table_generate_id_records(num_records)
      return num_records, id_dict

num_records, id_dict = generate_table_basic(1, 10)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generator the random data tables                 ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Note: "id_dict_copy = id_dict.copy()" is repeated to avoid 
#        each log iteration copying over to the next.

# Random Business Table
id_dict_copy = id_dict.copy()
num = len(id_dict_copy['ID_Record'])
print(f'///// {id_dict_copy}')
print(f'///// {num}')
bus_df = pd.DataFrame(grdb.generate_table_business_general(id_dict_copy))

