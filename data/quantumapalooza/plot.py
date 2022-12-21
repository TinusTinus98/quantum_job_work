import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
google_results = df["company_class_1"]

nb_company = google_results[google_results == "company"].count()
nb_uni = google_results[google_results == "university"].count()
nb_class = df.loc[(df["company_class_1"].notna()) & (df["sector"].notna()),"sector"].count()
nb_class_europages = nb_not_class = df.loc[(df["sector"].isna() == True) & (df["europages"].isna() == False),"employer"].count()
nb_not_class_eurclass = df.loc[(df["sector"].isna() == False) & (df["europages"].isna() == False),"employer"].count()
nb_eur = nb_class_europages + nb_not_class_eurclass

nb_not_class = df.loc[(df["sector"].isna() == False)& (df["europages"].isna() == True)& (df["company_class_1"].isna() == True),"employer"].count()

nb_others = google_results.shape[0] - nb_company - nb_uni - nb_eur - nb_not_class

data = [nb_uni, nb_company, nb_eur, nb_not_class, nb_others]
labels = [
    "university",
    "companies",
    "companies with europages",
    "not classified",
    "others",
]

colors = sns.color_palette("pastel")[0:5]
plt.pie(data, labels=labels, colors=colors, autopct="%.0f%%")
plt.show()
