import pandas as pd
import generate_random_dataset_support_functions as grdfs
import generate_random_dataset_business as grdb
import generate_random_dataset_legal as grdle
import generate_random_dataset_address as grda
import generate_random_dataset_employee as grde
import generate_random_dataset_tax as grdt
import generate_random_dataset_financial as grdf
import generate_random_dataset_log as grdlo
import generate_random_data_relationship as grdr
import generate_random_data_analysis_conditions as grdac

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
bus_df = pd.DataFrame(grdb.generate_table_business(1, 100))

# Random Legal Table
le_df = pd.DataFrame(grdle.generate_table_legal(1, 100))

# Random Address Table
addr_df = pd.DataFrame(grda.generate_table_address(1, 100))

# Random Employee Table
emp_df = pd.DataFrame(grde.generate_table_employee(1, 100))

# Random Tax Table
tax_df = pd.DataFrame(grdt.generate_table_tax(1, 100))

# Random Finance Table
finance_df = pd.DataFrame(grdf.generate_table_finance(1, 100))

# Random Log Table
# "id_dict_copy = id_dict.copy()" is repeated to avoid each log iteration copying over to the next.
id_dict_copy = id_dict.copy()
log_df_g = pd.DataFrame(grdlo.generate_table_log_general(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_dc = pd.DataFrame(grdlo.generate_table_log_datachange(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_fc = pd.DataFrame(grdlo.generate_table_log_filechange(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_sec = pd.DataFrame(grdlo.generate_table_log_security(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_wa = pd.DataFrame(grdlo.generate_table_log_user_web_activity(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_sa = pd.DataFrame(grdlo.generate_table_log_user_server_activity(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_ac = pd.DataFrame(grdlo.generate_table_log_user_account_activity(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_le = pd.DataFrame(grdlo.generate_table_log_errors(id_dict_copy, num_records))
id_dict_copy = id_dict.copy()
log_df_ec = pd.DataFrame(grdlo.generate_table_log_error_codes(id_dict_copy, num_records))


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Insert Foreign Keys for Data Linkage             ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Establishing the Business DB link by inserting its ID into other DBs
df_foreignkey_bus = grdr.Foreign_Keys(bus_df, db_fk_field_name='External ID', foreign_key_abbreviation_pre="Bus ")
le_df = df_foreignkey_bus.add_foreignkey_random(le_df,col_placement=3)
addr_df = df_foreignkey_bus.add_foreignkey_random(addr_df,col_placement=3)

# Establishing the Legal DB link by inserting its ID into other DBs
df_foreignkey_le = grdr.Foreign_Keys(le_df, db_fk_field_name='Legal Account', foreign_key_abbreviation_post=" ID")
addr_df = df_foreignkey_le.add_foreignkey_random(addr_df,col_placement=4)
tax_df = df_foreignkey_le.add_foreignkey_random(tax_df, col_placement=3)
finance_df = df_foreignkey_le.add_foreignkey_random(finance_df, col_placement=3)

# Establishing the Tax DB link by inserting its ID into other DBs
df_foreignkey_tax = grdr.Foreign_Keys(tax_df, db_fk_field_name='Tax Account', foreign_key_abbreviation_post=" ID")
finance_df = df_foreignkey_tax.add_foreignkey_random(finance_df, col_placement=3)


# Creating an intermediary Business-Legal Table:
df_intermediary = grdr.Intermediary_Data()
emp_interdb_df = df_intermediary.create_2db_relationship_df_random(df1=emp_df, df1_id_field_name='Employee ID', \
                                                                   df2=le_df, df2_id_field_name='Legal Account')





      
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Modidify Data for Realistic Attributes           ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------




#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Create Data Integirty Error Conditions           ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Store Datasets                                   ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
pathway_output = "data archive/"
# Random Business Table
bus_df.to_csv(pathway_output + "business data.csv", index=False)

# Random Legal Table
le_df.to_csv(pathway_output + "legal data.csv", index=False)

# Random Address Table
addr_df.to_csv(pathway_output + "address data.csv", index=False)

# Random Employee Table
emp_df.to_csv(pathway_output + "employee data.csv", index=False)

# Random Tax Table
tax_df.to_csv(pathway_output + "tax data.csv", index=False)

# Random Finance Table
finance_df.to_csv(pathway_output + "finance data.csv", index=False)

# Log Tables
log_df_g.to_csv(pathway_output + "Log General Information.csv", index=False)
log_df_dc.to_csv(pathway_output + "Log Datachanges.csv", index=False)
log_df_fc.to_csv(pathway_output + "Log Filechanges.csv", index=False)
log_df_sec.to_csv(pathway_output + "Log Security Details.csv", index=False)
log_df_wa.to_csv(pathway_output + "Log User Web Activity.csv", index=False)
log_df_sa.to_csv(pathway_output + "Log User Server Activity.csv", index=False)
log_df_ac.to_csv(pathway_output + "Log User Account Activity.csv", index=False)
log_df_le.to_csv(pathway_output + "Log Errors.csv", index=False)
log_df_ec.to_csv(pathway_output + "Log Error Codes.csv", index=False)

# Intermediary DBs
emp_interdb_df.to_csv(pathway_output + "Employee System.csv", index=False)