
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd

df = pd.read_excel('Downloads\2019-20-australian-government-contract-data.xlsx')
df.head()

df['Applicable Start Date'] = pd.to_datetime(df['Applicable Start Date'], format='%Y-%m-%d')

filtered_df = df.loc[(df['Applicable Start Date'] >= '2022-01-01')]

if filtered_df['Amendments Value'] != '':
    price = filtered_df['Amendments Value']/filtered_df['Duration Years']
else:
    price = filtered_df['Value']/filtered_df['Duration Years']
    

