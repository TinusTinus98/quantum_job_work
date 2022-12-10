import pandas as pd
import numpy as np

df = pd.read_excel("data/quantumapalooza/Classeur1.xlsx")
out = []
for i, x in enumerate(df.iloc[:, 0]):

    splitted = x.split(" U ")
    if len(splitted) == 1:
        splitted = x.split(" O ")
        splitted = [splitted[0], "O", splitted[1]]
    else:
        splitted = [splitted[0], "U", splitted[1]]
    spin = splitted[2]
    sp = spin.split(" A ")
    if len(sp) == 1:
        sp = spin.split(" F ")
        if len(sp) == 2:
            sp = [sp[0], "F", sp[1]]
    else:
        sp = [sp[0], "A", sp[1]]
    if len(sp) == 1:
        sp = spin.split(" P ")
        if len(sp) == 2:
            sp = [sp[0], "P", sp[1]]
    if len(sp) == 1:
        sp = spin.split(" I ")
        if len(sp) == 2:
            sp = [sp[0], "I", sp[1]]
    spp = splitted[0].split()
    if i == 1420:
        spp = [spp[0], np.nan, spp[1]]
    else:
        sppp = " ".join(spp[2::])
        spp[2] = sppp
    spout = [
        spp[0].strip(),
        spp[1],
        spp[2].strip(),
        splitted[1],
        sp[0].strip(),
        sp[1],
        sp[2].split()[0],
    ]
    if i < 20:
        print(spout)
    out.append(spout)
    name = [
        "countRef",
        "openDate",
        "employer",
        "employerType",
        "jobTitle",
        "type",
        "countries",
    ]
    dict = {}
    for i, n in enumerate(name):
        dict[n] = spout[i]
    out.append(dict)
df = pd.DataFrame.from_dict(out)
df.to_csv("data/quantumapalooza/eusnapshot.csv")
print(out[0])
