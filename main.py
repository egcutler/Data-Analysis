import pandas as pd
import generate_random_dataset_support_functions as grdfs
import generate_random_dataset_business as grdb
import generate_random_dataset_legal as grdle
import generate_random_dataset_address as grda
import generate_random_dataset_employee as grde
import generate_random_dataset_tax as grdt
import generate_random_dataset_financial as grdf
import generate_random_dataset_log as grdlo
import data_integrity_support_files as disf

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

# Random Business Table
bus_df = pd.DataFrame(grdb.generate_table_business())
bus_df.to_csv("data archive/business data.csv", index=False)

# Random Legal Table
le_df = pd.DataFrame(grdle.generate_table_legal())
le_df.to_csv("data archive/legal data.csv", index=False)

# Random Address Table
addr_df = pd.DataFrame(grda.generate_table_address())
addr_df.to_csv("data archive/address data.csv", index=False)

# Random Employee Table
emp_df = pd.DataFrame(grde.generate_table_employee())
emp_df.to_csv("data archive/employee data.csv", index=False)

# Random Tax Table
tax_df = pd.DataFrame(grdt.generate_table_tax())
tax_df.to_csv("data archive/tax data.csv", index=False)

# Random Finance Table
finance_df = pd.DataFrame(grdf.generate_table_finance())
finance_df.to_csv("data archive/finance data.csv", index=False)

# Random Log Table
id_dict_copy = id_dict.copy()
log_df = pd.DataFrame(grdlo.generate_table_log_general(id_dict_copy, num_records))
log_df.to_csv("data archive/Log General Information.csv", index=False)
id_dict_copy = id_dict.copy()
log_df2 = pd.DataFrame(grdlo.generate_table_log_datachange(id_dict_copy, num_records))
log_df2.to_csv("data archive/Log Datachanges.csv", index=False)
id_dict_copy = id_dict.copy()
log_df3 = pd.DataFrame(grdlo.generate_table_log_filechange(id_dict_copy, num_records))
log_df3.to_csv("data archive/Log Filechanges.csv", index=False)
id_dict_copy = id_dict.copy()
log_df4 = pd.DataFrame(grdlo.generate_table_log_security(id_dict_copy, num_records))
log_df4.to_csv("data archive/Log Security Details.csv", index=False)
id_dict_copy = id_dict.copy()
log_df5 = pd.DataFrame(grdlo.generate_table_log_user_web_activity(id_dict_copy, num_records))
log_df5.to_csv("data archive/Log User Web Activity.csv", index=False)
id_dict_copy = id_dict.copy()
log_df6 = pd.DataFrame(grdlo.generate_table_log_user_server_activity(id_dict_copy, num_records))
log_df6.to_csv("data archive/Log User Server Activity.csv", index=False)
id_dict_copy = id_dict.copy()
log_df7 = pd.DataFrame(grdlo.generate_table_log_user_account_activity(id_dict_copy, num_records))
log_df7.to_csv("data archive/Log User Account Activity.csv", index=False)
id_dict_copy = id_dict.copy()
log_df8 = pd.DataFrame(grdlo.generate_table_log_errors(id_dict_copy, num_records))
log_df8.to_csv("data archive/Log Errors.csv", index=False)
id_dict_copy = id_dict.copy()
log_df9 = pd.DataFrame(grdlo.generate_table_log_error_codes(id_dict_copy, num_records))
log_df9.to_csv("data archive/Log Error Codes.csv", index=False)


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              File Prechecks                                   ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
partial_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID']

precheck_folder = disf.FolderPreCheck(path)
if precheck_folder.check_files_with_partial_name(partial_name, filetype):
      precheck_file = disf.FilePreCheck(path, filename, filetype)
      precheck_file.file_exist_precheck()
      precheck_file.fields_exist_precheck(field_list)
      id_lcase_check = precheck_file.check_fields_with_partialname("id")
      id_ucase_check = precheck_file.check_fields_with_partialname("ID")
      if id_lcase_check == False and id_ucase_check == False:
            raise Exception("Programm terminated...no valid ID fields present")
      
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Data Quality Check                               ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

