import pandas as pa
import random
from generate_random_dataset_address import addr_abbr_dict

class Data_Analysis_Inserts:
      def __init__(self, df):
            self.df = df

      def create_duplicates_within_field_random(self, field_name, dup_option_perc = random.randint(10,30), field_perc_to_dup = random.randint(10,30)):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if dup_option_perc > 100 or dup_option_perc < 0.1:
                  raise Exception(f"dup_option_perc value of {dup_option_perc} is not between 0.1% - 100%")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Duplication option
            unique_values = list(set(self.df[field_name]))
            duplication_option_perc_num = round(len(unique_values) * (dup_option_perc/100))
            values_to_duplicate = random.sample(unique_values, duplication_option_perc_num)
            
            # Override values at the selected positions with the duplicated values
            duplication_field_perc_num = round(len(self.df[field_name]) * (field_perc_to_dup/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = random.choice(values_to_duplicate)
            return self.df

      
      def insert_value_by_override_perc(self, field_name, field_perc_to_dup = random.randint(10,20), value = ""):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Override values at the selected positions with Null
            duplication_field_perc_num = round(len(self.df[field_name]) * (field_perc_to_dup/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = value
            return self.df
            
      

class Data_Analysis_Changes:
      def __init__(self, df):
            self.df = df
            
      def target_value_change_value(self, field_name, field_perc_to_dup = random.randint(10,20), target_value="", change_value = ""):
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Generate index list for each record the targeted value occurs
            index_loc = []  
            for index in range(len(self.df)):
                  if target_value.lower() in self.df.at[index, field_name].lower():
                        index_loc.append(index)
            
            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            # Remove duplicates
            index_positions_to_override = list(set(index_positions_to_override))
            # Override targeted values at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = self.df.at[index, field_name].replace(target_value, change_value)
            return self.df
      
      def address_abbreviation_change(self, field_name, field_perc_to_dup = random.randint(10,20)):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            index_loc = []
            addr_list = list(addr_abbr_dict.keys())
            addr_list = [value.lower() for value in addr_list]
            for index in range(len(self.df)):
                  df_value = self.df.at[index, field_name].lower()
                  for addr_type in addr_list:
                        if addr_type in df_value:
                              index_loc.append(index)
            
            # Override values at the selected positions with address abbreviations
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            index_positions_to_override = list(set(index_positions_to_override))
            for index in index_positions_to_override:
                  original_value = self.df.at[index, field_name]
                  for full, abbr in addr_abbr_dict.items():
                        # If abbreviation is a list, choose the first one or randomly
                        abbr_value = abbr[0] if isinstance(abbr, list) else abbr
                        # Replace with abbreviation (both lowercase for case-insensitive matching)
                        self.df.at[index, field_name] = original_value.lower().replace(full.lower(), abbr_value.lower())
                        original_value = self.df.at[index, field_name]
                  self.df.at[index, field_name] = self.df.at[index, field_name].title()
                  
            return self.df
            
      


      
class Data_Analysis_Err_Conditions:
      def __init__(self, df):
            self.df = df
      
      def closed_date_misalignment(self):
            pass
      
      def address_incorrect_format(self):
            pass
      
      def email_incorrect_format(self):
            pass
      