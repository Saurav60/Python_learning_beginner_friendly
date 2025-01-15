#to upload a csv file 
import pandas as pd
df = pd.read_csv('file.csv')
average = df['column_name'].mean()
df['column_name'] = df['column_name'].fillna(average, inplace=True)


#function to count number of transactions 
