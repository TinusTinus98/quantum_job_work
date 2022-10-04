import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

embedder = SentenceTransformer("bert-base-nli-mean-tokens")

df = pd.read_csv("data/data_onetonline/detailed_work_activities.csv")

jobs_names = pd.read_csv(
    "data/data_onetonline/jobs_metadata.csv", usecols=["code", "job_name"]
)

work_activities = {}
for job_code in df["code"].unique():
    activities = df[df["code"] == job_code]["detailed_work_activity"].values
    text = " ".join(activities)
    work_activities[text] = jobs_names[jobs_names["code"] == job_code][
        "job_name"
    ].values[0]


official = list(work_activities.keys())
official_embeddings = embedder.encode(official)


scrapped_df = pd.read_csv("data/scrapped_data/LIX_quantum_185900.csv")
scrapped_work_activities = dict(
    zip(scrapped_df["Description"].values, scrapped_df["Title"].values)
)
scrapped_embeddings = embedder.encode(list(scrapped_work_activities.keys()))

outfile = open("pickle_files/scrapped_embeddings.p", "wb")
pickle.dump(scrapped_embeddings, outfile)
outfile.close()
outfile = open("pickle_files/scrapped_work_activities.p", "wb")
pickle.dump(scrapped_work_activities, outfile)
outfile.close()
outfile = open("pickle_files/work_activities.p", "wb")
pickle.dump(work_activities, outfile)
outfile.close()
outfile = open("pickle_files/official_embeddings.p", "wb")
pickle.dump(official_embeddings, outfile)
outfile.close()
outfile = open("pickle_files/official.p", "wb")
pickle.dump(official, outfile)
outfile.close()
