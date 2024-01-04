import pandas as pd
import random
import string
from datetime import datetime, timedelta

max_date = 20241011111111

if isinstance(max_date, int) and len(str(max_date)) <= 8 and len(str(max_date)) >= 6:
      max_date = str(max_date)
      yyyy = max_date[0:4]
      if len(max_date[4:]) == 2:
            mm = max_date[4:5]
            dd = max_date[5:]
      elif len(max_date[4:]) == 4:
            mm = max_date[4:6]
            dd = max_date[6:]
      elif max_date[4:5] == '0':
            mm = max_date[4:6]
            dd = max_date[6:]
      else:
            mm = max_date[4:5]
            dd = max_date[5:]
      yyyy = int(yyyy)
      mm = int(mm)
      dd = int(dd)
      max_date = datetime(yyyy,mm,dd)
      
print(max_date)