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
      
      def not_target_record_change_record(self, field_name, field_perc_to_dup = random.randint(10,20), not_target_record="", change_record = ""):
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Generate index list for each record the targeted value occurs
            index_loc = []  
            for index in range(len(self.df)):
                  if not_target_record.lower() not in self.df.at[index, field_name].lower():
                        index_loc.append(index)

            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            # Remove duplicates
            index_positions_to_override = list(set(index_positions_to_override))
            # Override targeted values at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = change_record
            return self.df
      
      def target_records_change_record_diff_fields(self, target_field1, target_value1, change_field, change_value,\
                                                         target_field2 = "-----", target_value2 = "-----", \
                                                         target_field3 = "-----", target_value3 = "-----", \
                                                         target_field4 = "-----", target_value4 = "-----", \
                                                         field_perc_to_dup = random.randint(10,20)):
            # Required argument checks  
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if target_field1 not in self.df.columns:
                  raise ValueError(f"{target_field1} not in DataFrame")
            if change_field not in self.df.columns:
                  raise ValueError(f"{change_field} not in DataFrame")
            if not isinstance(change_value, self.df[change_field].dtype.type):
                  #raise ValueError(f"Data type of change value {type(change_value)} does not match the data type for field '{change_field}', which is {self.df[change_field].dtype}")
                  pass
            # Potential argument checks        
            if target_field2 != "-----" and target_field2 not in self.df.columns:
                  raise ValueError(f"{target_field2} not in DataFrame")
            if target_field3 != "-----" and target_field3 not in self.df.columns:
                  raise ValueError(f"{target_field3} not in DataFrame")
            if target_field4 != "-----" and target_field4 not in self.df.columns:
                  raise ValueError(f"{target_field4} not in DataFrame")
            if target_field2 == "-----" and target_field3 != "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}', 3 '{target_field3}', and 4 '{target_field4}' were entered, however Target Field 2 is missing")
            if target_field2 != "-----" and target_field3 == "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}', 2 '{target_field2}', and 4 '{target_field4}' were entered, however Target Field 3 is missing")
            if target_field2 == "-----" and target_field3 == "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}' and 4 '{target_field4}' were entered, however Target Field 2 and 3 are missing")

            # Determine case
            if target_field4 == "-----":
                  if target_field3 == "-----":
                        if target_field2 == "-----":
                              case_degree = 1
                        else:
                              case_degree = 2
                  else:
                        case_degree = 3
            else:
                  case_degree = 4
            
            # Generate index list for each record the targeted value occurs
            index_loc = [] 
            print(f'///// {case_degree}')
            if case_degree == 4: 
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower() and \
                           target_value3.lower() in self.df.at[index, target_field3].lower() and \
                           target_value4.lower() in self.df.at[index, target_field4].lower():
                              index_loc.append(index) 
            elif case_degree == 3:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower() and \
                           target_value3.lower() in self.df.at[index, target_field3].lower():
                              index_loc.append(index)
            elif case_degree == 2:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower():
                              index_loc.append(index)
            else:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower():
                              index_loc.append(index)
            print(f'///// {index_loc}')
            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            print(f'///// {index_positions_to_override}')
            # Override change field at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, change_field] = change_value
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
      