import pandas as pa
import random


class Data_Analysis_Inserts:
      def __init__(self, df):
            self.df = df

      def replicate_field_values_with_random(self, field_name, dup_option_perc = random.randint(10,30), num_to_dup_perc = random.randint(10,30)):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if dup_option_perc > 100 or dup_option_perc < 0.1:
                  raise Exception(f"dup_option_perc value of {dup_option_perc} is not between 0.1% - 100%")
            if num_to_dup_perc > 100 or num_to_dup_perc < 0.1:
                  raise Exception(f"num_to_dup_perc value of {num_to_dup_perc} is not between 0.1% - 100%")
            
            # Duplication option
            unique_values = list(set(self.df[field_name]))
            duplication_option_perc_num = round(len(unique_values) * (dup_option_perc/100))
            values_to_duplicate = random.sample(unique_values, duplication_option_perc_num)
            
            # Override values at the selected positions with the duplicated values
            duplication_field_perc_num = round(len(self.df[field_name]) * (num_to_dup_perc/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = random.choice(values_to_duplicate)
            return self.df

      
      def replicate_field_values_with_value(self, field_name, num_to_dup_perc = random.randint(10,20), value = ""):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if num_to_dup_perc > 100 or num_to_dup_perc < 0.1:
                  raise Exception(f"num_to_dup_perc value of {num_to_dup_perc} is not between 0.1% - 100%")
            
            # Override values at the selected positions with Null
            duplication_field_perc_num = round(len(self.df[field_name]) * (num_to_dup_perc/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = value
            return self.df
            
      

class Data_Analysis_Changes:
      def __init__(self, df):
            self.df = df
      
      def address_abbreviation_change(self):
            pass
      
      def company_abbreviation_change(self):
            pass
      
      def name_abbreviation_change(self):
            pass

      
class Data_Analysis_Err_Conditions:
      def __init__(self, df):
            self.df = df
      
      def closed_date_misalignment(self):
            pass
      
      def address_incorrect_format(self):
            pass
      
      def email_incorrect_format(self):
            pass
      