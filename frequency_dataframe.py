import matplotlib as plt
import numpy as np
import pandas as pd

matchs = pd.read_csv(
    "data/matching_bert/matching_BERT_faiss_onet_title_1.csv"
)  # ,usecols=["code", "job_name"]
print(matchs)


nb_mached_jobs = matchs.shape[0]
res = []
for code in matchs["match_code"].unique():
    df = matchs[matchs["match_code"] == code]
    res.append(
        {"quantity": df.shape[0], "job_name": df["official_match_title"].iloc[0]}
    )

df = pd.DataFrame(res)
df.to_csv("data/frequency_dataframe_title.csv")
