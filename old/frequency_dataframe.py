import matplotlib as plt
import numpy as np
import pandas as pd

matchs = pd.read_csv(
    "data/matching_bert/matching_BERT_faiss_onet_title_1.csv"
)  # ,usecols=["code", "job_name"]
print(matchs)


def set_quantity(df: pd.DataFrame, name_col: str):
    res = []
    for code in df[name_col].unique():
        df_code = df[df[name_col] == code]
        dic = {"quantity": df_code.shape[0]}
        for col_name in df.columns.values:
            dic[col_name] = df_code[col_name].iloc[0]
        res.append(dic)
    df = pd.DataFrame(res)
    return df


nb_mached_jobs = matchs.shape[0]
res = []
for code in matchs["match_code"].unique():
    df = matchs[matchs["match_code"] == code]
    res.append(
        {"quantity": df.shape[0], "job_name": df["official_match_title"].iloc[0]}
    )

df = pd.DataFrame(res)
df.to_csv("data/frequency_dataframe_title.csv")
