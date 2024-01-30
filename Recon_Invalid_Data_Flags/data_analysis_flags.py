import Data_Statistics.data_statistics as ds
import pandas as pd
import numpy as np



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
            closed_check_list = ['CLOSED', 'C']
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