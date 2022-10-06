import bert_matching
import plot_tools
import pandas as pd

name = "matching_1"
cols = ["job_name", "code"]
df_official = pd.read_csv("data/data_onetonline/jobs_metadata.csv", usecols=cols)
# print(df_official.head())
cols = ["Title", "Description"]
df_to_match = pd.read_csv("data/scrapped_data/LIX_quantum_185900.csv", usecols=cols)
# print(df_to_match.dtypes)
df = bert_matching.bert_match(df_official, "job_name", df_to_match, "Title", k=1)
df.to_csv("data/matching_bert/" + name + ".csv")
print(df.head())
print(df.dtypes)
plot_tools.plot_match(df, "official_job_name", "matching_test", 2)
