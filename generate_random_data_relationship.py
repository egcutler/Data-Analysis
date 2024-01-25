import pandas as pd
import random


class Foreign_Keys:
      def __init__(self, df, db_fk_field_name, foreign_key_abbreviation = ""):
            self.df = df
            self.db_fk_field_name = db_fk_field_name
            self.foreign_key_abbreviation = foreign_key_abbreviation
      
      def add_foreignkey_random(self, df2, col_placement = 3):
            if self.db_fk_field_name not in self.df.columns:
                  raise ValueError(f"{self.db_fk_field_name} not in first DataFrame")
            
            db_fk_list = self.df[self.db_fk_field_name].tolist()
            random_fk_values = [random.choice(db_fk_list) for _ in range(len(df2))]
            
            if self.db_fk_field_name in df2.columns:
                  df2 = df2.drop(columns=self.db_fk_field_name)
            
            df2.insert(col_placement - 1, self.foreign_key_abbreviation + self.db_fk_field_name, random_fk_values)
            return df2
            
      
      def add_foreignkey_conditions(self):
            pass
      

class Intermediary_Data:
      def __init__(self, df1, df1_id_field_name, df2, df2_id_field_name):
            self.df1 = df1
            self.df2 = df2
            self.df1_id_field_name = df1_id_field_name
            self.df2_id_field_name = df2_id_field_name
      
      # Two databases establishing a data relationship where the db1 IDs - db2 IDs are randomized 
      def two_db_rel_new_con_rand(self): #two_db_
            new_relationship_df = pd.DataFrame()
            new_relationship_df[self.df1_id_field_name] = self.df1[self.df1_id_field_name]
            random_df2_id_list = [random.choice(self.df2[self.df2_id_field_name]) for _ in range(len(self.df1))]
            new_relationship_df[self.df2_id_field_name] = random_df2_id_list
            return new_relationship_df
            
      
      # Two databases establishing a data relationship where the db1 IDs - db2 IDs are randomized 
      def two_db_rel_new_con_type(self):
            pass