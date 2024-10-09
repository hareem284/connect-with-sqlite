# importing sql
import sqlite3
# importing pandas
import pandas as pd
connection=sqlite3.connect('basketball.sqlite')
print("connection established")
TABLE=pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';",connection)
print(TABLE)