import Data_Statistics.data_statistics as ds
import pandas as pd
import numpy as np
import re



# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Integrity and Data Analysis                         --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class Data_Analysis_Flags:
      def __init__ (self, df):
            self.df = df
            
      def closed_date_other_date_flag(self, date_field_cls = "", date_field_open = "", date_field_mod = "", print_flags = "Y"):
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
                  cls_mod_field = f"Flag {date_field_cls} vs {date_field_mod}"
                  self.df[cls_mod_field] = np.where((self.df[date_field_cls] < self.df[date_field_mod]), "Y", "N")
                  check['cls vs mod'] = 1
                  
            if date_field_open != "":
                  cls_op_field = f"Flag {date_field_cls} vs {date_field_open}"
                  self.df[cls_op_field] = np.where((self.df[date_field_cls] < self.df[date_field_open]), "Y", "N")
                  check['cls vs open'] = 1
            
            if check['cls vs mod'] == 0 and check['cls vs open'] == 0:
                  raise Exception(f"A Modified Date field or Open Date field is required as an argument...")
            else:
                  stat_check = ds.Statistics(self.df)
                  if check['cls vs mod'] == 1 and check['cls vs open'] == 1:
                        cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                        cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                        if print_flags == "Y":
                              print(f"...{cls_mod_field}: {stat_check.count_values_field_dict(cls_mod_unique_valus, cls_mod_field)}")
                              print(f"...{cls_op_field}: {stat_check.count_values_field_dict(cls_op_unique_valus, cls_op_field)}")
                        
                        return self.df
                  elif check['cls vs mod'] == 0 and check['cls vs open'] == 1:
                        cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                        if print_flags == "Y":
                              print(f"...{cls_op_field}: {stat_check.count_values_field_dict(cls_op_unique_valus, cls_op_field)}")
                        
                        return self.df
                  elif check['cls vs mod'] == 1 and check['cls vs open'] == 0:
                        cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                        if print_flags == "Y":
                              print(f"...{cls_mod_field}: {stat_check.count_values_field_dict(cls_mod_unique_valus, cls_mod_field)}")
                        
                        return self.df

      def closed_date_status_flag(self, status_field, closed_date_field, print_flags = "Y"):
            """
            Mark rows based on the conditions:
            - "Y" if the closed date field is not null and the status field is 'ACTIVE' or 'A'
            - "Y" if the closed date field is null and the status field is 'CLOSED' or 'C'
            - "N" for all other cases

            :param df: pandas DataFrame
            :param status_field: Name of the status field (column)
            :param closed_date_field: Name of the closed date field (column)
            :return: DataFrame with an additional column 'Mark' containing "Y" or "N" based on the conditions
            """
            active_check_list = ['ACTIVE', 'A']
            closed_check_list = ['CLOSED', 'C', 'INACTIVE', 'I']
            def check_conditions(row):
                  if (pd.notnull(row[closed_date_field]) and row[status_field].upper() in active_check_list) or \
                  (pd.isnull(row[closed_date_field]) and row[status_field].upper() in closed_check_list):
                        return 'Y'
                  else:
                        return 'N'
            # apply() with axis=1 is necessary because the check_conditions function needs to access multiple columns 
            # of data for each row. By setting axis=1, pandas passes each row (as a Series) to the function.
            self.df['Flag Closed Date vs Status'] = self.df.apply(check_conditions, axis=1)
            if print_flags == "Y":
                  stat_check = ds.Statistics(self.df)
                  cls_stat_unique_valus = stat_check.list_unique_values('Flag Closed Date vs Status')
                  print(f"...Flag Closed Date vs Status: {stat_check.count_values_field_dict(cls_stat_unique_valus, 'Flag Closed Date vs Status')}")
            
            return self.df
      
      def flag_non_standard_addresses(self, address_field, print_flags="Y"):
            """
            Flags rows in the DataFrame where the street address does not follow a standard format.

            Args:
                  address_field (str): The name of the column in the DataFrame containing street addresses.
                  print_flags (str, optional): If set to 'Y', prints the count of unique flag values. Defaults to 'Y'.

            Returns:
                  pandas.DataFrame: The DataFrame with an additional column 'Flag Street Address'.
            """
            # Updated regex pattern to match standard address format (number followed by two words)
            pattern = r"^\d+\s[A-Za-z]+(\s[A-Za-z]+)?"
            # Function to flag non-standard addresses
            def check_address(address):
                  if pd.notna(address) and address != '' and not re.match(pattern, address):

                        return 'Y'  # Non-standard address
                  else:
                        return 'N'  # Standard address

            # Apply the function to the address field
            self.df['Flag Street Address'] = self.df[address_field].apply(check_address)
            # Print flag statistics if required
            if print_flags.upper() == "Y":
                  stat_check = ds.Statistics(self.df)
                  str_addr_flag_unique_values = stat_check.list_unique_values('Flag Street Address')
                  print(f"...Flag Street Addresses: {stat_check.count_values_field_dict(str_addr_flag_unique_values, 'Flag Street Address')}")

            return self.df
                  