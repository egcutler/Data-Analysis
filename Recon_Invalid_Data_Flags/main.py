import data_integrity_flag_checks as difc
import data_analysis_flags as daf
import data_flag_statistics as ds
import pandas as pd


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    --- Table Flag Check                                --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


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
df = difc.file_prechecks(path, filename, partial_file_name, filetype , field_list)

# Check the data inside the file source
difc.data_integrity_check(df, expected_types)

# Perform additional data statistics
ds.standard_stats(df)

# Perform the data analysis flag checks
print(' ')
print('Data Analysis Flags')
print('---------------------------------------')
print('Flagged Closed Dates')
df_flags = daf.Data_Analysis_Flags(df)
df = df_flags.closed_date_other_date_flag(date_field_cls='Closed Date', date_field_mod='Modified Date', date_field_open='Creation Date')
df = df_flags.closed_date_status_flag(status_field='Business Status', closed_date_field='Closed Date')
print('---------------------------------------')

# Flag stats
print(' ')
print('Data Statistics Flags')
print('---------------------------------------')
ds.flags_stats(df)
print('---------------------------------------')


# Output
output_path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
output_filename = 'Business Data Flag'
output_filetype = '.csv'
df.to_csv(output_path + "/" + output_filename + output_filetype, index=False)


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    --- Table Flag Check                                --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------