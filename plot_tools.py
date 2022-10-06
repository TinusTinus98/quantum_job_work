import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes
from mpl_toolkits.axisartist.grid_finder import FixedLocator, MaxNLocator, DictFormatter


def plot_match(df0, col_labels, name_plot,limit=10, min_Y=1):
    df = pd.DataFrame(df0[col_labels])
    list_to_gather = []
    df = set_quantity(df, col_labels)
    df = gather(df, "quantity", col_labels, list_to_gather, "ok")
    print("number : ", df["quantity"].sum())
    df = df[df["quantity"] > min_Y]
    df = df.sort_values(by=["quantity"], ascending=False)
    labels = remove_space(df[col_labels], limit=limit)
    plot_bar(df["quantity"], labels, name_plot)


def plot_bar(Y, labels, name_plot):
    fig = plt.figure(figsize=(8, 4))
    fig.subplots_adjust(bottom=0.3)
    path_plot = "out/"
    X = [i for i in range(len(Y))]
    plt.bar(X, Y)
    plt.xticks(X, labels)
    plt.xticks(fontsize=8, rotation=90)
    plt.title("BERT matching")
    # plt.savefig(path_plot + name_plot, dpi=1200)


def set_quantity(df: pd.DataFrame, name_col: str):
    res = []
    for code in df[name_col].unique():
        df_code = df[df[name_col] == code]
        dic = {"quantity": df_code.shape[0]}
        for col_name in df.columns.values:
            dic[col_name] = df_code[col_name].iloc[0]
        res.append(dic)
    df = pd.DataFrame(res)
    return df


def gather(df, quantity_col, col_name, list_name, new_name):
    new = []  # "Astronomers", "Materials Scientists", "Physicists"
    quantity = 0
    for x in df[col_name].values:
        if x in list_name:
            new.append(new_name)
            quantity += df[df[col_name] == x][quantity_col].iloc[0]
        else:
            new.append(x)
    df2 = df.assign(new=new)
    return df2


def remove_space(bars, limit: int = 10):
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
    return labels
