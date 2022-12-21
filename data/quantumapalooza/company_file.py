import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
isnan = df["europages"].isna()
dic = {"nom":[]}
for i in tqdm(range(df.shape[0])):
    if df.loc[i,'company_class_1']=='company' or not isnan[i]:
        nom = df.loc[i,'employer']
        dic['nom'].append(df.loc[i,'employer'])
df = pd.DataFrame.from_dict(dic)
df.to_csv("data/quantumapalooza/companies.csv")