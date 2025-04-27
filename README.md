## Data Description

### `grocery_sales` Data
Contains sales data for stores, structured as follows:

- **index**: Unique ID of the row
- **Store_ID**: The store number
- **Date**: The week of sales
- **Weekly_Sales**: Sales for the given store

### `extra_data.parquet` Data
Contains complementary data for each store, structured as follows:

- **IsHoliday**: Whether the week contains a public holiday (1 if yes, 0 if no)
- **Temperature**: Temperature on the day of sale
- **Fuel_Price**: Cost of fuel in the region
- **CPI**: Prevailing consumer price index
- **Unemployment**: The prevailing unemployment rate
- **MarkDown1**, **MarkDown2**, **MarkDown3**, **MarkDown4**: Number of promotional markdowns
- **Dept**: Department Number in each store
- **Size**: Size of the store
- **Type**: Type of the store (depends on Size column)

---

## The idea is to merge these two data types



1. **Merge** the `grocery_sales` and `extra_data.parquet` datasets on the `Store_ID` and `Date` columns.
2. **Transform** the data to create a new DataFrame `clean_data` with the following columns:
   - `Store_ID`
   - `Month`: Extracted from the `Date` field
   - `Dept`: Department number from the `extra_data.parquet`
   - `IsHoliday`: Whether the week contains a public holiday
   - `Weekly_Sales`: Sales for the given store
   - `CPI`: Prevailing consumer price index
   - `Unemployment`: The prevailing unemployment rate

---

