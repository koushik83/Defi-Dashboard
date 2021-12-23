import pandas as pd
from tokentermscript import tokenterm

# reads from the master list from Defillama of all protocols 

df = pd.read_csv("/Users/avisihag/Desktop/Crypto/filea.csv")

# Select the top 20 of each 
df1 = df.groupby(["category"]).head(20).reset_index(drop=True)

grouped_df = df.groupby('category')

dictionary = tokenterm(df1)

df3 = pd.DataFrame(columns=['project', ''])

for key, item in dictionary:
    if not "message" in item[0]:
        df3.append(item[0].filter(items=[]))
