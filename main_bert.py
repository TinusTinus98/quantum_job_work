import bert_matching
import plot_tools
import pandas as pd
import matplotlib.pyplot as plt

# importation--------------------------------------------------------------------------
name = "matching_4"
cols = ["job_name", "code"]
df_official = pd.read_csv("data/data_onetonline/jobs_metadata.csv", usecols=cols)

df_to_match = pd.read_csv("data/consortium/data_1st_WS_ok.csv")
# df_to_match=df_to_match["Title", "Description"]
print(df_to_match.head())
print(df_to_match.dtypes)

# matching-BERT--------------------------------------------------------------------------
df = bert_matching.bert_match(df_official, "job_name", df_to_match, "title", k=1)
df.to_csv("data/matching_bert/" + name + ".csv")
print(df.head())
print(df.dtypes)

# plot-----------------------------------------------------------------------------------
df = pd.read_csv("data/matching_bert/" + name + ".csv")
plot_tools.plot_match(df, "official_job_name", "matching_test", 22, 15)
plt.show()
