# ---------------
import pandas as pd
from pathlib import Path
import pandas as pd
import generate_tables_support_functions as gtsf
import generate_sample_table_business as gstb
import generate_sample_table_legal as gstl
import generate_sample_table_address as gsta
import generate_sample_table_employee as gste
import generate_sample_table_tax as gstt
import generate_sample_table_financial as gstf
import generate_random_table_log as grtl
import data_integrity_support_files as disf
import data_integrity_data_checks as didc


path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
partial_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID']

def df_with_prechecks():
      print('---------------------------------------')
      precheck_folder = disf.FolderPreCheck(path)
      if precheck_folder.check_files_with_partial_name(partial_name, filetype):
            precheck_file = disf.FilePreCheck(path, filename, filetype)
            precheck_file.file_exist_precheck()
            precheck_file.fields_exist_precheck(field_list)
            id_lcase_check = precheck_file.check_fields_with_partialname("id")
            id_ucase_check = precheck_file.check_fields_with_partialname("ID")
            if id_lcase_check == False and id_ucase_check == False:
                  raise Exception("Programm terminated...no valid ID fields present")
            print('---------------------------------------')
            return pd.read_csv(f"{path}/{filename}{filetype}")
      

#precheck_file.search_fields_with_partialname("a")
def data_integrity_check(df):
      print('---------------------------------------')
      datacheck = didc.Data_Check(df)
      datacheck.id_unique_count_thresholds('External ID')
      datacheck.active_ids('External ID', "Business Status")
      datacheck.null_check()
      datacheck.check_duplicate_rows()
      datacheck.check_multiple_data_types()
      expected_types = {
            'Branch': str,             
            'External ID': str,
            'Account': int,            
            'Business Status': str,           
            'Creation Date': str        
      }
      datacheck.check_explicit_data_types(expected_types)
      datacheck.check_data_len_range('Company Name', max_len=64)
      print('---------------------------------------')
      datacheck_format = didc.Data_Check_Formats(df)
      #datacheck_format.check_employee_email_format_field('External ID')
      #datacheck_format.check_street_address_format_field('External ID')
      #datacheck_format.check_zip_code_format_field('External ID')
      #datacheck_format.check_ip_address_format_field('External ID')
      #datacheck_format.check_domain_name_format_field('External ID')

def main():
      df = df_with_prechecks()
      data_integrity_check(df)
      
main()
