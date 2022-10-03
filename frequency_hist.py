import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stats = pd.read_csv("frequency_dataframe.csv")  # ,usecols=["code", "job_name"]

number_jobs = stats["quantity"].sum()
stats = stats[stats["quantity"] > 1]
# print(stats)
name_fig = "fig"
path_plot = ""


#### gathering R&D jobs--------------------------
new_job_name = []
rd_target = ["Astronomers", "Materials Scientists", "Physicists"]
quantity = 0
for x in stats["job_name"].values:
    if x in rd_target:
        new_job_name.append("RD")
        quantity += stats[stats["job_name"] == x]["quantity"].iloc[0]
    else:
        new_job_name.append(x)
stats = stats.assign(new_job_name=new_job_name)
stats = stats[stats["new_job_name"] != "RD"]
stats = stats[["quantity", "new_job_name"]]
print(stats)

stats = stats.append({"quantity": quantity, "new_job_name": "RD"}, ignore_index=True)
stats["quantity"] = stats["quantity"] / number_jobs * 100
stats = stats.sort_values(by=["quantity"], ascending=False)
print(stats)
bars = stats["new_job_name"]

#### remove space and put several lines--------------------------------
limit = 8
labels = []
for i, x in enumerate(bars):
    value = 0
    new_c = ""
    for c in x:
        if value > limit and c == " ":
            new_c = new_c + "\n"
            value = 0
        else:
            new_c = new_c + c
            value += 1
    labels.append(new_c)

# graph ---------------------------------------------------
Y = stats["quantity"]
X = [i for i in range(len(Y))]

plt.bar(X, Y)
plt.xticks(X, labels)
plt.xticks(fontsize=8, rotation=0)
plt.show()


# plt.xlabel("debt-equity ratio")
# plt.ylabel("percentage among 47473 one-step change")
# plt.title(name_fig)
# plt.savefig(path_plot + name_fig)
