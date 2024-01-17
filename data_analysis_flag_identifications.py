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


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Prechecks                                                --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

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
      df = pd.read_csv(f"{path}/{filename}{filetype}")

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Quality Checks                                      --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
#precheck_file.search_fields_with_partialname("ID")

datacheck = didc.Data_Check(df)
datacheck.id_unique_count_thresholds('External ID')
datacheck.active_ids('External ID', "Business Status")

