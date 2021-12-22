import json
import requests
import pandas as pd

def tokenterm(df):
    params = {"interval": "daily", "data_granularity": "project"}
    headers = {"Authorization": "Bearer 1ca4d5eb-9360-437d-a877-9b73fd1a4f80"}
    dct = {}
    arr = []
    for i in df.index:
        s = 'https://api.tokenterminal.com/v1/projects/' + df['name'][i].lower() + '/metrics'
        r = requests.get(s, params=params, headers=headers)
        try:
            k = r.json()[0]
        except KeyError:
            k =  r.json()
        finally:
            print(k)
            dft = pd.json_normalize(k)
            print(dft.head(1))
            if df['name'][i] in dct.keys():
                dct[df['name'][i]].append(dft)
            else:
                dct[df['name'][i]] = [dft]
                dct[df['name'][i]][0]['name']=df['name'][i]

    print(dct)
    return dct