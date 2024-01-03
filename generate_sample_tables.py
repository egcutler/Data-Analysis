import pandas as pd
import random


# Set the seed for reproducibility (optional)
random.seed(50)

# Number of records
num_records = 10000

# Generate a DataFrame with a random ID column
data = {'ID': [random.randint(1, 100000) for x in range(num_records)]}
df = pd.DataFrame(data)



# Display the DataFrame
print(df)
#df.to_csv("testtest.csv", index=False)