import pandas as pd
import numpy as np

df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")

out = [np.nan for _ in range(df.shape[0])]
df.insert(4,'europages', out )

df.to_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")