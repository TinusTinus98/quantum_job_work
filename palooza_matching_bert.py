import pandas as pd

import bert_matching
import plot_tools
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/companies_sorted.csv")

# importation--------------------------------------------------------------------------
name = "matching_bert_1"
cols = ["name", "industry"]
df_official = pd.read_csv("data/companies_sorted_2.csv", usecols=cols)

df_to_match = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
# df_to_match=df_to_match["Title", "Description"]
print(df_to_match.head())
print(df_to_match.dtypes)

# matching-BERT--------------------------------------------------------------------------
# df = bert_matching.bert_match(df_official, "name", df_to_match, "employer", k=1)
# df.to_csv("data/quantuaplooza/" + name + ".csv")
# print(df.head())
# print(df.dtypes)

# plot-----------------------------------------------------------------------------------
# df = pd.read_csv("data/matching_bert/" + name + ".csv")
# plot_tools.plot_match(df, "official_job_name", "matching_test", 22, 15)
# plt.show()