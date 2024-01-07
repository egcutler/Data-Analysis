import pandas as pd
import generate_sample_table_business as gstb
import generate_sample_table_legal as gstl
import generate_sample_table_address as gsta

bus_df = pd.DataFrame(gstb.generate_table_business())
bus_df.to_csv("data archive/business data.csv", index=False)

le_df = pd.DataFrame(gstl.generate_table_legal())
le_df.to_csv("data archive/legal data.csv", index=False)

addr_df = pd.DataFrame(gsta.generate_table_address())
addr_df.to_csv("data archive/address data.csv", index=False)
print(addr_df)