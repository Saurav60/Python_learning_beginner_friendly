import pandas as pd 
from datetime import datetime,timedelta
def purchase_in_five_months(df):
    current_date = datetime.now()
    six_month_ago = current_date - timedelta(days=6*30)

    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    recent_purchases = df[df['purchase_date']> six_month_ago]
    purchase_count = recent_purchases.groupby(['customer_id']).size()
    customers_with_more_than_5_purchases = purchase_count[purchase_count > 2].index.tolist()
    return customers_with_more_than_5_purchases

data = {
    'customer_id': [1, 1, 2, 1, 2, 1, 2, 1],
    'purchase_date': ['2024-05-10', '2024-06-15', '2024-07-20', '2024-02-15', '2024-08-01', '2024-09-05', '2024-10-10', '2024-11-25']
}
df = pd.DataFrame(data)
result = purchase_in_five_months(df)
print(result)