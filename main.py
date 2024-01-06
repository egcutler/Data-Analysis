import pandas as pd
import generate_sample_table_business as gstb

bus_df = pd.DataFrame(gstb.generate_table_business())
bus_df.to_csv("data archive/business data.csv", index=False)