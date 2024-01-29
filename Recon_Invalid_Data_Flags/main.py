import data_integrity_checks as dic
import data_analysis_flags as daf
import pandas as pd


path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
filename = 'business data'
partial_file_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID', 'Creation Date', 'Modified Date', 'Closed Date']
expected_types = {
      'Branch': str,             
      'External ID': str,
      'Account': int,            
      'Business Status': str,           
      'Creation Date': str        
}

# Check the file source is there and contains the required information
df = dic.file_prechecks(path, filename, partial_file_name, filetype , field_list)
# Check the data inside the file source
dic.data_integrity_check(df, expected_types)
# Perform the data analysis flag checks
df_flags = daf.Data_Analysis_Flags(df)
#print(df.columns)
df = df_flags.closed_date_quality(date_field_cls='Closed Date', date_field_mod='Modified Date', date_field_open='Creation Date')
