import pandas as pd
import numpy as np

df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
for i in range(df.shape[0]):
    if df["employerType"].iloc[i] == "U":
        df["sector"].iloc[i] = "university"

df.to_csv("data/quantumapalooza/quantumapalooza_eusnapshot_3.csv")
