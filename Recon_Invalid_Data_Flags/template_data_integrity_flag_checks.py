from Data_Integrity import data_integrity_data_checks as didc
from Data_Integrity import data_integrity_support_files as disf
from Data_Integrity import data_integrity_data_cleaning as didcl
import pandas as pd

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Precheck                                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def file_prechecks(path, filename, partial_name, filetype , field_list = []):
      print(' ')
      print('Checking file source features')
      print('---------------------------------------')
      precheck_folder = disf.FolderPreCheck(path)
      if precheck_folder.check_files_with_partial_name(partial_name, filetype):
            precheck_file = disf.FilePreCheck(path, filename, filetype)
            precheck_file.file_exist_precheck()
            precheck_file.fields_exist_precheck(field_list)
            id_check = precheck_file.check_fields_with_partialname("ID", print_fails="Y")
            if id_check == False:
                  raise Exception("Programm terminated...no valid ID fields present")
            print('---------------------------------------')
            return pd.read_csv(f"{path}/{filename}{filetype}")
      

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    DB Check                                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def data_integrity_check(df, field_id="", field_status = "", expected_types = "", field_len_check = "", \
                         field_email_check = "", field_street_address_check = "", field_zipcode_check = "", \
                         field_ip_check = "", field_domain_check = ""):
      print(' ')
      print('Checking data source attributes')
      print('---------------------------------------')
      datacheck = didc.Data_Check(df)
      if field_id != "" and field_id != None:
            datacheck.id_unique_count_thresholds(field_id)
      else:
            raise ValueError(f"Field ID Name was not provided.")
  
      if field_status != "" and field_status != None:
            datacheck.active_ids(field_id, field_status)
      
      datacheck.null_check()
      datacheck.check_duplicate_rows()
      datacheck.check_multiple_data_types()
      if expected_types != "" and expected_types != None:
            datacheck.check_explicit_data_types(expected_types)
      if field_len_check != "" and field_len_check != None:    
            datacheck.check_data_len_range(field_len_check, max_len=64)
            
      datacheck_format = didc.Data_Check_Formats(df)
      if field_email_check != "" and field_email_check != None:    
            datacheck_format.check_employee_email_format_field(field_email_check)
      if field_street_address_check != "" and field_street_address_check != None:
            datacheck_format.check_street_address_format_field(field_street_address_check)
      if field_zipcode_check != "" and field_zipcode_check != None:
            datacheck_format.check_zip_code_format_field(field_zipcode_check)
      if field_ip_check != "" and field_ip_check != None:
            datacheck_format.check_ip_address_format_field(field_ip_check)
      if field_domain_check != "" and field_domain_check != None:
            datacheck_format.check_domain_name_format_field(field_domain_check)
      print('---------------------------------------')

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    DB Cleanup                                               --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def clean_data(df):
      clean_data = didcl.Clean_Data(df)
      print(' ')
      print('Cleaning dataset')
      print('---------------------------------------')
      clean_data.drop_row_if_all_are_null(print_effected_records="Y")
      clean_data.remove_duplicates(print_effected_records="Y")
      clean_data.replace_inf_values(0, print_effected_records="Y")
      for col in df.columns:
            if "NAME" in col.upper():
                  clean_data.remove_whitespaces(col, print_effected_records="Y")
            
            if "STATUS" in col.upper():
                  clean_data.convert_column_uppercase(col, print_effected_records="Y")
                  
            if "STATE" in col.upper():
                  clean_data.convert_column_uppercase(col, print_effected_records="Y")
      print('---------------------------------------')
      