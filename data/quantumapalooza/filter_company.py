import pandas as pd
import numpy as np

df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
df['jobTitle']=df['jobTitle'].apply(str.lower)
df['employer']=df['employer'].apply(str.lower)
# for i in range(df.shape[0]):
#     if not df[df['sector'].inan()].iloc[i]:
#         df.loc[i,'sector']

for i in range(df.shape[0]):
    company_class_1 = np.nan
    google_results = df.loc[i,"sector"]
    keys = [
        "company",
        "business",
        "start-up",
        "startup",
        "manufacturer",
        "manufacture",
        "firm",
        "agency",
        "talent",
        "professional",
        "recruitment",
    ]
    keys_2 = ["consult", "sales", "market", "finance"]
    keys_3 = ["ltd", "gmbh"]
    if df.loc[i,"employerType"] == "U":
        company_class_1 = "university"
    else:
        for key in keys:
            if not df['sector'].isna().iloc[i]:
                if key.lower() in google_results:
                    company_class_1 = "company"
        if df.loc[i,"sector"] != "company":
            for key in keys_2:
                if key in df.loc[i,"jobTitle"]:
                    company_class_1 = "company"
        else:
            for key in keys_3:
                if key in df.loc[i,"employer"]:
                    company_class_1 = "company"
    df.loc[i,"company_class_1"] = company_class_1


df.to_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
