import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

embedder = SentenceTransformer("bert-base-nli-mean-tokens")

df = pd.read_csv("data/data_onetonline/detailed_work_activities.csv")

jobs_names = pd.read_csv(
    "data/data_onetonline/jobs_metadata.csv", usecols=["code", "job_name"]
)
# print(list(jobs_names["job_name"]))
official = jobs_names

official_embeddings = embedder.encode(list(jobs_names["job_name"]))


scrapped_df = pd.read_csv("data/scrapped_data/LIX_quantum_185900.csv")
scrapped = scrapped_df["Title"]
scrapped_embeddings = embedder.encode(list(scrapped_df["Title"].values))

outfile = open("pickle_files/scrapped_embeddings.p", "wb")
pickle.dump(scrapped_embeddings, outfile)
outfile.close()
outfile = open("pickle_files/scrapped.p", "wb")
pickle.dump(scrapped, outfile)
outfile.close()
outfile = open("pickle_files/official_embeddings.p", "wb")
pickle.dump(official_embeddings, outfile)
outfile.close()
outfile = open("pickle_files/official.p", "wb")
pickle.dump(official, outfile)
outfile.close()
