import pandas as pd

path = r'/root/workspace/github.com/egcutler/Data-Analysis/data archive'
filename = 'business data'
filetype = '.csv'

# Correctly concatenates the path and the filename
full_path = f"{path}/{filename}{filetype}"

# Reads the CSV file into a DataFrame
df = pd.read_csv(full_path)

# Prints the data types of each column

print(df.dtypes)