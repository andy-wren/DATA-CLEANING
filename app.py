import pandas as pd
import csv

df = pd.read_csv("final_merged_data.csv")
print(df.shape)

del df["luminosity"]
print(df.shape)
print(list(df))
df.to_csv('main.csv')
