import pandas as pd
from Data_Integrity import data_integrity_data_checks as didc
from Data_Integrity import data_integrity_support_files as disf

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Precheck                                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def file_prechecks(path, filename, partial_name, filetype , field_list = []):
      print(' ')
      print('...Checking file source features')
      print('---------------------------------------')
      precheck_folder = disf.FolderPreCheck(path)
      if precheck_folder.check_files_with_partial_name(partial_name, filetype):
            precheck_file = disf.FilePreCheck(path, filename, filetype)
            precheck_file.file_exist_precheck()
            precheck_file.fields_exist_precheck(field_list)
            id_lcase_check = precheck_file.check_fields_with_partialname("id", print_fails="Y")
            id_ucase_check = precheck_file.check_fields_with_partialname("ID", print_fails="Y")
            if id_lcase_check == False and id_ucase_check == False:
                  raise Exception("Programm terminated...no valid ID fields present")
            print('---------------------------------------')
            return pd.read_csv(f"{path}/{filename}{filetype}")
      

#precheck_file.search_fields_with_partialname("a")
def data_integrity_check(df, expected_types = ""):
      print(' ')
      print('...Checking data source attributes')
      print('---------------------------------------')
      datacheck = didc.Data_Check(df)
      datacheck.id_unique_count_thresholds('External ID')
      datacheck.active_ids('External ID', "Business Status")
      datacheck.null_check()
      datacheck.check_duplicate_rows()
      datacheck.check_multiple_data_types()
      if expected_types != "":
            datacheck.check_explicit_data_types(expected_types)
            
      datacheck.check_data_len_range('Company Name', max_len=64)
      print('---------------------------------------')
      datacheck_format = didc.Data_Check_Formats(df)
      #datacheck_format.check_employee_email_format_field('External ID')
      #datacheck_format.check_street_address_format_field('External ID')
      #datacheck_format.check_zip_code_format_field('External ID')
      #datacheck_format.check_ip_address_format_field('External ID')
      #datacheck_format.check_domain_name_format_field('External ID')
      