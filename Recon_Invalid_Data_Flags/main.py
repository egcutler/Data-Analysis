import template_data_integrity_flag_checks as difc
import template_data_analysis_flags as daf
import template_data_flag_statistics as ds
import pandas as pd


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------         Case 1: Business Table Flag Check                                   --------------
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
print(f"=============  {filename}  =============")
# Check the file source is there and contains the required information
bus_df = difc.file_prechecks(path, filename, partial_file_name, filetype , field_list)

# Check the data inside the file source
difc.data_integrity_check(bus_df, field_id='External ID', expected_types=expected_types,field_status='Business Status', field_len_check='Company Name')

# Data Cleanup
difc.clean_data(bus_df)

# Perform additional data statistics
ds.standard_stats(bus_df)

# Perform the data analysis flag checks
print(' ')
print('Data Analysis Flags')

print('---------------------------------------')
bus_df_flags = daf.Data_Analysis_Flags(bus_df)
print('Flagged Closed Dates')
bus_df = bus_df_flags.closed_date_other_date_flag(date_field_cls='Closed Date', date_field_mod='Modified Date', date_field_open='Creation Date')
print('Flagged Closed Dates vs Status')
bus_df = bus_df_flags.closed_date_status_flag(status_field='Business Status', closed_date_field='Closed Date')
print('---------------------------------------')
print(f"========================================")
print(' ')
# Output
output_path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
output_filename = 'Business Data With Flags'
output_filetype = '.csv'
bus_df.to_csv(output_path + "/" + output_filename + output_filetype, index=False)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------         Case 2: Legal Table Flag Check                                      --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
filename = 'legal data'
partial_file_name = 'legal'
filetype = '.csv'
field_list = ['Legal Account', 'LE Creation Date', 'LE Modified Date', 'LE Closed Date']
expected_types = {           
      'Legal Account': str,           
      'Legal Status': str,           
      'LE Creation Date': str,
      'LE Modified Date': str,
      'LE Closed Date': str        
}
print(f"=============  {filename}  =============")
# Check the file source is there and contains the required information
le_df = difc.file_prechecks(path, filename, partial_file_name, filetype , field_list)

# Check the data inside the file source
difc.data_integrity_check(le_df, field_id='Legal Account', expected_types=expected_types,field_status='Legal Status', field_len_check='Legal Firm')

# Data Cleanup
difc.clean_data(le_df)

# Perform additional data statistics
ds.standard_stats(le_df)

# Perform the data analysis flag checks
print(' ')
print('Data Analysis Flags')
print('---------------------------------------')
le_df_flags = daf.Data_Analysis_Flags(le_df)
print('Flagged Closed Dates')
le_df = le_df_flags.closed_date_other_date_flag(date_field_cls='LE Closed Date', date_field_mod='LE Modified Date', date_field_open='LE Creation Date')
print('Flagged Closed Dates vs Status')
le_df = le_df_flags.closed_date_status_flag(status_field='Legal Status', closed_date_field='LE Closed Date')
print('---------------------------------------')
print(f"========================================")
print(' ')
# Output
output_path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
output_filename = 'Legal Data With Flags'
output_filetype = '.csv'
le_df.to_csv(output_path + "/" + output_filename + output_filetype, index=False)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------         Case 3: Address Table Flag Check                                    --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
filename = 'address data'
partial_file_name = 'address'
filetype = '.csv'
field_list = ['Address ID']
expected_types = {           
      'Address ID': int,           
      'Address Street': str     
}
print(f"=============  {filename}  =============")
# Check the file source is there and contains the required information
addr_df = difc.file_prechecks(path, filename, partial_file_name, filetype , field_list)

# Check the data inside the file source
difc.data_integrity_check(addr_df, field_id='Address ID', expected_types=expected_types,\
                          field_street_address_check='Address Street', field_zipcode_check = 'Zip Code')

# Data Cleanup
difc.clean_data(addr_df)

# Perform additional data statistics
ds.standard_stats(addr_df)

# Perform the data analysis flag checks
print(' ')
print('Data Analysis Flags')
print('---------------------------------------')
addr_df_flags = daf.Data_Analysis_Flags(addr_df)
print('Flagged Street Addresses')
addr_df = addr_df_flags.flag_non_standard_addresses(address_field='Address Street')
print('---------------------------------------')
print(f"========================================")
print(' ')
# Output
output_path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
output_filename = 'Address Data With Flags'
output_filetype = '.csv'
addr_df.to_csv(output_path + "/" + output_filename + output_filetype, index=False)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------         Case 4: Employee Table Flag Check                                    --------------
# ---------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------- 

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
filename = 'employee data'
partial_file_name = 'employee'
filetype = '.csv'
field_list = ['Employee ID', 'Emp First Name', 'Emp Last Name']
expected_types = {           
      'Employee ID': int,           
      'Emp First Name': str,           
      'Emp Last Name': str     
}
print(f"=============  {filename}  =============")
# Check the file source is there and contains the required information
emp_df = difc.file_prechecks(path, filename, partial_file_name, filetype , field_list)

# Check the data inside the file source
difc.data_integrity_check(emp_df, field_id='Employee ID', expected_types=expected_types,field_status='Employee Status', field_len_check='Employee Email')

# Data Cleanup
difc.clean_data(emp_df)

# Perform additional data statistics
ds.standard_stats(emp_df)

# Perform the data analysis flag checks
print(' ')
print('Data Analysis Flags')
print('---------------------------------------')
emp_df_flags = daf.Data_Analysis_Flags(emp_df)
print('Flagged Emails')
emp_df = emp_df_flags.flag_non_standard_email(email_field='Employee Email')
print('---------------------------------------')
print(f"========================================")
print(' ')
# Output
output_path = (r'/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive')
output_filename = 'Employee Data With Flags'
output_filetype = '.csv'
emp_df.to_csv(output_path + "/" + output_filename + output_filetype, index=False)