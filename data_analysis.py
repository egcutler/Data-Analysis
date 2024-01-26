 # ---------------
import pandas as pd
import data_integrity_support_files as disf
import data_integrity_data_checks as didc
import numpy as np
import data_statistics as ds


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Precheck                                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def df_with_prechecks(path, filename, partial_name, filetype , field_list = []):
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
      
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Integrity and Data Analysis                         --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def closed_date_quality(df, date_field_cls, date_field_open = "", date_field_mod = ""):
      """
      Update a dataframe with data analysis columns compare Closed Date field date value against
      the date values of both/either a open (created) date field and a modified date field. If the
      Closed Date field has a value before the other date fields, it is flagged as closed dates
      should contain the latest date.
      :param df: dataframe
      :param date_field_cls: Closed Date field
      :param date_field_open: Open Date field
      :param date_field_mod: Modified Date field
      :return: updated df with both/either flagged Closed Date vs Modified Date flags and/or Open Date flags.
      """
      check = {
            'cls vs mod'  : 0,
            'cls vs open' : 0
      }
      if date_field_cls == "":
            raise Exception("No Closed Date field name was provided...")
      
      if date_field_mod != "":
            cls_mod_field = f"Flag {date_field_cls} on {date_field_mod}"
            df[cls_mod_field] = np.where((df[date_field_cls] < df[date_field_mod]), "Y", "N")
            check['cls vs mod'] = 1
            
      if date_field_mod != "":
            cls_op_field = f"Flag {date_field_cls} on {date_field_open}"
            df[cls_op_field] = np.where((df[date_field_cls] < df[date_field_open]), "Y", "N")
            check['cls vs open'] = 1
      
      if check['cls vs mod'] == 0 and check['cls vs open'] == 0:
            raise Exception(f"A Modified Date field or Open Date field is required as an argument...")
      else:
            stat_check = ds.Statistics_List(df)
            print('---------------------------------------')
            print('Data Analysis: Flagged Closed Dates')
            print(' ')
            
            if check['cls vs mod'] == 1 and check['cls vs open'] == 1:
                  cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                  cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                  print("Flag distributions ")
                  print(f"{cls_mod_field}: {stat_check.count_value_occurrences(cls_mod_unique_valus, cls_mod_field)}")
                  print(f"{cls_op_field}: {stat_check.count_value_occurrences(cls_op_unique_valus, cls_op_field)}")
                  print('---------------------------------------')
                  return df
            elif check['cls vs mod'] == 0 and check['cls vs open'] == 1:
                  cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                  print("Flag distributions ")
                  print(f"{cls_op_field}: {stat_check.count_value_occurrences(cls_op_unique_valus, cls_op_field)}")
                  print('---------------------------------------')
                  return df
            elif check['cls vs mod'] == 1 and check['cls vs open'] == 0:
                  cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                  print("Flag distributions ")
                  print(f"{cls_mod_field}: {stat_check.count_value_occurrences(cls_mod_unique_valus, cls_mod_field)}")
                  print('---------------------------------------')
                  return df

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Main Control                                             --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def data_analysis_closed_date_flags(path, filename, partial_name, filetype , field_list = [], date_field_cls = "", date_field_open = "", date_field_mod = ""):
      df = df_with_prechecks(path, filename, partial_name, filetype , field_list)
      data_integrity_check(df)
      df = closed_date_quality(df, date_field_cls, date_field_open, date_field_mod)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
partial_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID']
data_analysis_closed_date_flags(path, filename, partial_name, filetype , field_list, 'Closed Date', 'Creation Date', 'Modified Date')
