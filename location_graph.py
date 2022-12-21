import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scrapped_df = pd.read_csv("data/scrapped_data/LIX_quantum_185900.csv")
location = scrapped_df["Location"]
# print(scrapped_df["Location"])

splitted = [x.split(",") for x in location]
usa_regions = [
    " CA",
    " ON",
    " NY",
    " NH",
    " IL",
    " WI",
    " MI",
    " PA",
    " WA",
    " ME",
    " TX",
    " CO",
    " VA",
    " NC",
    " DC",
    " MA",
    " NM",
    "Blacksburg-Christiansburg-Radford Area",
    " NE",
    " SC",
    " OR",
    " VT",
]
dic_usa = {x: "USA" for x in usa_regions}
result = []
for i, x in enumerate(splitted):
    # print([y for y in x[-1]])
    if x[-1] in usa_regions:
        country = "USA"
    else:
        country = x[-1]
    result.append({"Country": country, "Town": x[0]})

df = pd.DataFrame(result)
print(df["Country"].unique())
print(df)

res = []
for x in df["Country"].unique():
    quantity = df[df["Country"] == x]["Country"].count()
    res.append({"quantity": quantity, "Country": x})

df2 = pd.DataFrame(res)
df2 = df2.sort_values(by=["quantity"], ascending=False)
number = df2["quantity"].sum()
print(df2)
X = [x for x in range(np.shape(df["Country"].unique())[0])]
Y = df2["quantity"]
print(number)
labels = df2["Country"]
plt.bar(X, Y)
plt.title("location plot (150 job posts)")
plt.xticks(X, labels)
plt.xticks(fontsize=8, rotation=0)
plt.show()
