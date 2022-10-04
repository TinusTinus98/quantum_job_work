import faiss
import numpy as np
import pandas as pd
import scipy.spatial
from sentence_transformers import SentenceTransformer
import pickle

jobs_names = pd.read_csv(
    "data/data_onetonline/jobs_metadata.csv", usecols=["code", "job_name"]
)
infile = open("pickle_files/scrapped_embeddings.p", "rb")
scrapped_embeddings = pickle.load(infile)
infile.close()
infile = open("pickle_files/scrapped.p", "rb")
scrapped = pickle.load(infile)
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
i = 0
for query, query_embedding in zip(scrapped, scrapped_embeddings):
    k = 1  # return 3 nearest neighbours
    distances, indices = index.search(np.asarray(query_embedding).reshape(1, 768), k)
    for idx in range(0, k):
        # print(official[indices[0, idx]], "(Distance: %.4f)" % distances[0, idx])
        job_name = official["job_name"][indices[0, idx]]
        match_code = official["code"][indices[0, idx]]
        res.append(
            {
                "scrapped_jobs": query,
                "official_match_title": job_name,
                "match_code": match_code,
                "distance": distances[0, idx],
            }
        )
    i += 1
df = pd.DataFrame(res)
df.to_csv("data/matching_bert/matching_BERT_faiss_onet_title_1.csv")
