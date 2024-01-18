import os
import extract_transfer_load as etl
import numpy as np
import exceptions as err

path = (r'C:\Users\ericg\Projects\Data Analyst Projects\Data Sample Files')
filename = "Client Business Data"
filetype = ".xlsx"
field = "File Name That Is Not Present"
fields = ['Business Account IDs', 'Creation Date', 'Last Modification Date', 'Closed Date']
sheet_name = "sheet1"
# -  -  -  -  -  -  -  -  -  -  -  -  Sample Demonstrating Error Check-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# Example test with improper pathway
# path = (r'C:\Users\ericg\Projects\Data Analyst Projects\Data Sample Files Test')
# Example test with improper fields:
# fields = ['Client Account ID', 'Creation Date', 'Last Modification Date', 'Closed Date', 'testing A', 'testing B']
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Pre Check:
precheck = err.FilePreCheck(path, filename, filetype)
precheck.file_exist_precheck()
precheck.fields_exist_precheck(fields)
# File Extract:
df = etl.file_extract_simple(path, filename, filetype)
# Post Checks:
postcheck = err.FilePostCheck(df)
postcheck.id_numbers('Business Account IDs')
postcheck.active_ids('Business Account IDs', 'Client Account Activity')
postcheck.id_integrity('Business Account IDs')
# Flag accounts that are still being modified after closure
data_flag = df
data_flag['Flag'] = np.where((data_flag['Closed Date'] < data_flag['Last Modification Date']) | (data_flag['Closed Date'] < data_flag['Creation Date']), "Y", "N")

data_flag.to_excel("Client Business Flag Update.xlsx", index=False)
path_generate = r'C:\Users\ericg\PycharmProjects\DataAnalyst\Flags\Client Business Flag Update.xlsx'
os.startfile(path_generate)
