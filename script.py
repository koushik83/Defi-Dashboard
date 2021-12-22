import pandas as pd
from tokentermscript import tokenterm

df = pd.read_csv("/Users/avisihag/Desktop/Crypto/filea.csv")

df1 = df.groupby(["category"]).head(2).reset_index(drop=True)
#print(df1)

grouped_df = df.groupby('category')

# for key, item in grouped_df:
#     print(grouped_df.get_group(key), "\n\n")


dictionary = tokenterm(df1)

df3 = pd.DataFrame(columns=['project', ''])

for key, item in dictionary:
    if not "message" in item[0]:
        df3.append(item[0].filter(items=[]))