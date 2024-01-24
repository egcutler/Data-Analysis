import pandas as pa
import random


class Add_Foreign_Keys:
      def __init__(self, df1, df2):
            self.df1 = df1
            self.df2 = df2
      
      def foreignkey_random(self, db1_fk_field_name):
            db1_fk_list = self.df1[db1_fk_field_name]
            df2_update = self.df2
            for _ in range(len(self.df2)):
                  df2_update[db1_fk_field_name].append(random.choice(db1_fk_list))
            return df2_update
            
      
      def foreignkey_conditions(self, db1_fk):
            pass