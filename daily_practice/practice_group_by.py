import pandas as pd 
dataset = {'restaurant_id':[101,101,102,102,103],
           'order_amount': [100,150,240,200,300],
           'order_date': ['05-08-2024','09-08-2024','10-08-2024','06-08-2024', '07-08-2024']}
df = pd.DataFrame(dataset)
df_grouped = df.groupby('restaurant_id')['order_amount'].sum().reset_index()
print(df_grouped)