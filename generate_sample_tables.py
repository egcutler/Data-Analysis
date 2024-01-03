import pandas as pd
import random

# Generate a random record limit for the data frame
def generate_random_record_length(min = 500, max = 100000, seed_val = 50):
      # Set the seed for reproducibility
      random.seed(seed_val)
      # Number of records
      return random.randint(min, max)

# Generate a DataFrame with a random ID and Account Columns
def table_generate(num_records):
      data = {'ID_Record': [random.randint(1, num_records) for x in range(num_records)]}
      for x in data['ID_Record']:
            zero_count = len(str(num_records)) - len(str(x))
            if zero_count == 0:
                  data['Account'] = str(x)
            else:
                  zero_addon = '0' * zero_count
                  data['Account'] = zero_addon + str(x)
      return data
#------------------------------------------------------------------------------     

num_records = generate_random_record_length()
data = table_generate(num_records)
print(pd.DataFrame(data))


# Display the DataFrame
#print(df)
#df.to_csv("data archive/test.csv", index=False)
