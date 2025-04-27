import pandas as pd
import os

grocery_sales = pd.read_csv("grocery_sales.csv")

# Estracting data and merging 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

merged_df = extract(grocery_sales, "extra_data.parquet")
print(merged_df.head())

def transform(raw_data):
    raw_data=raw_data.fillna(0)
    raw_data['Month']=0
    clean_data =raw_data[raw_data['Weekly_Sales']>10000]
    columns_to_keep = ["Store_ID", "Month", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"]
    good_columns = [col for col in columns_to_keep if col in clean_data.columns]
    clean_data=clean_data[good_columns]
    return clean_data


clean_data = transform(merged_df)
print(clean_data.head())


