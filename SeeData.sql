sqlite3
.load csv
CREATE VIRTUAL TABLE grocery USING csv(filename='grocery_sales.csv');