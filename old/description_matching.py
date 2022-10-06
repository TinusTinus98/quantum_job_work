import faiss
import numpy as np
import pandas as pd
import scipy.spatial
from sentence_transformers import SentenceTransformer
import pickle

jobs_names = pd.read_csv(
    "data/data_onetonline/jobs_metadata.csv", usecols=["code", "job_name"]
)
infile = open("pickle_files/scrapped_work_activities.p", "rb")
scrapped_work_activities = pickle.load(infile)
infile.close()
infile = open("pickle_files/scrapped_embeddings.p", "rb")
scrapped_embeddings = pickle.load(infile)
infile.close()
infile = open("pickle_files/work_activities.p", "rb")
work_activities = pickle.load(infile)
infile.close()
infile = open("pickle_files/official_embeddings.p", "rb")
official_embeddings = pickle.load(infile)
infile.close()
infile = open("pickle_files/official.p", "rb")
official = pickle.load(infile)
infile.close()

d = 768
index = faiss.IndexFlatL2(d)
print(index.is_trained)
print(index.ntotal)  # print the number of vector
index.add(np.stack(official_embeddings, axis=0))
print(index.is_trained)
print(index.ntotal)  # print the number of vector

res = []
for query, query_embedding in zip(scrapped_work_activities, scrapped_embeddings):
    k = 1  # return 3 nearest neighbours
    distances, indices = index.search(np.asarray(query_embedding).reshape(1, 768), k)
    # print("\n======================\n")
    # print("Query:", query)
    # print("\nTop 5 most similar sentences in corpus:")
    for idx in range(0, k):
        # print(official[indices[0, idx]], "(Distance: %.4f)" % distances[0, idx])
        job_name = work_activities[official[indices[0, idx]]]
        res.append(
            {
                "scrapped_jobs": scrapped_work_activities[query],
                "official_match_title": job_name,
                "match_code": jobs_names[jobs_names["job_name"] == job_name][
                    "code"
                ].values[0],
                "distance": distances[0, idx],
            }
        )
df = pd.DataFrame(res)
df.to_csv("./matching_BERT_faiss_onet_lix_1.csv")

print(df)

print()
