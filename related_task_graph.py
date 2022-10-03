import matplotlib
import matplotlib.cm as cmx
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

# Building graph from csv file
df = pd.read_csv("./data_onetonline/related_occupations.csv")
nodes = np.unique(np.concatenate([df["code"].values, df["related"].values]))

df = df[df["code"] != df["related"]]
df["color"] = df["code"].str.split("-").str[0].astype(int)

G = nx.Graph()

for node in nodes:
    G.add_node(node)
for row in range(df.shape[0]):
    G.add_edge(df.iloc[row]["code"], df.iloc[row]["related"])


# Creating the colors for the node of the same family
color = [int(node.split("-")[0]) for node in G.nodes()]
mini = min(color)
normalized_color = [e - mini for e in color]

unique_colors = np.unique(color)
color_idx_matching = {i: list(unique_colors).index(i) for i in color}

legends = pd.read_csv("./data_onetonline/job_codes.csv")
ColorLegend = dict(zip(legends["description"], legends["code"]))
values = [color_idx_matching[int(node.split("-")[0])] for node in G.nodes()]
jet = cm = plt.get_cmap("jet")
cNorm = colors.Normalize(vmin=0, vmax=max(values))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)


# Creating the legend
f = plt.figure(1, figsize=(15, 15))
ax = f.add_subplot(1, 1, 1)
for label in ColorLegend:
    if ColorLegend[label] in color_idx_matching:
        c = color_idx_matching[ColorLegend[label]]
    else:
        c = 22
    ax.plot(
        [0],
        [0],
        color=scalarMap.to_rgba(c),
        label=label,
    )


# Ploting the graph with the colors
pos = nx.spring_layout(G)
nx.draw_networkx(
    G,
    pos,
    cmap=jet,
    vmin=0,
    vmax=max(values),
    node_color=values,
    with_labels=True,
    font_size=1,
    ax=ax,
    node_size=50,
)
f.set_facecolor("w")
plt.legend()
plt.savefig("related_jobs.svg")
print()
