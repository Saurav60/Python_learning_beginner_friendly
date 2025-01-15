import pandas as pd
def running_total_of_list(sales):
    df = pd.DataFrame(sales, columns = ['sales'])
    df['running_total'] = df['sales'].cumsum()
    return df 

sales = [100, 200, 300, 400, 500]
result_df = running_total_of_list(sales)
print(result_df)