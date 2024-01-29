import pandas as pd
import numpy as np
import Data_Statistics.data_statistics as ds



# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Integrity and Data Analysis                         --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class Data_Analysis_Flags:
      def __init__ (self, df):
            self.df = df
            
      def closed_date_quality(self, date_field_cls = "", date_field_open = "", date_field_mod = ""):
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
                  stat_check = ds.Statistics_List(self.df)
                  print('Data Analysis: Flagged Closed Dates')
                  print(' ')
                  
                  if check['cls vs mod'] == 1 and check['cls vs open'] == 1:
                        cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                        cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                        print("Flag distributions ")
                        print(f"{cls_mod_field}: {stat_check.count_value_occurrences(cls_mod_unique_valus, cls_mod_field)}")
                        print(f"{cls_op_field}: {stat_check.count_value_occurrences(cls_op_unique_valus, cls_op_field)}")
                        return self.df
                  elif check['cls vs mod'] == 0 and check['cls vs open'] == 1:
                        cls_op_unique_valus = stat_check.list_unique_values(cls_op_field)
                        print("Flag distributions ")
                        print(f"{cls_op_field}: {stat_check.count_value_occurrences(cls_op_unique_valus, cls_op_field)}")
                        return self.df
                  elif check['cls vs mod'] == 1 and check['cls vs open'] == 0:
                        cls_mod_unique_valus = stat_check.list_unique_values(cls_mod_field)
                        print("Flag distributions ")
                        print(f"{cls_mod_field}: {stat_check.count_value_occurrences(cls_mod_unique_valus, cls_mod_field)}")
                        return self.df

