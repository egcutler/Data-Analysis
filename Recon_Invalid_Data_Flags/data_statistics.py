import Data_Statistics.data_statistics as ds
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Statistics                                               --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def standard_stats(df):
      standard_stats = ds.Statistics(df)
      print(' ')
      print('...Standard dataframe statistics')
      print('---------------------------------------')
      
      nulls_all = standard_stats.count_nulls_in_all_fields()
      count = 0
      for key, value in nulls_all.items():
            if value > 0:
                  count += 1
      print(f"...There are {count} fields containing one or more null values")
      for key, value in nulls_all.items():
            print(f"   {key} has {value} null records.")
      print('---------------------------------------')
