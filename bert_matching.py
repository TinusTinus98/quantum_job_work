import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


def bert_match(df_official, col_official, df_to_match, col_to_match, k=1):
    path = "data/matching_bert"
    embedder = SentenceTransformer("bert-base-nli-mean-tokens")
    official_embeddings = embedder.encode(list(df_official[col_official]))
    to_match_embeddings = embedder.encode(list(df_to_match[col_to_match]))
    print(type(to_match_embeddings))
    df = faiss_match(
        df_official, official_embeddings, df_to_match, to_match_embeddings, k
    )
    return df

def faiss_match(
    df_official: pd.DataFrame,
    official_embeddings: pd.DataFrame,
    df_to_match: pd.DataFrame,
    to_match_embeddings: pd.DataFrame,
    k: int = 1,
):
    d = official_embeddings[0].shape[0]
    index = faiss.IndexFlatL2(d)  # set the dimension of the vectors
    index.add(np.stack(official_embeddings, axis=0))  # train the datas
    res = []
    for i, query_embedding in enumerate(to_match_embeddings):
        space = np.asarray(query_embedding).reshape(1, d)
        distances, indices = index.search(space, k)
        for idx in range(0, k):
            dictionary = {
                "distance": distances[0, idx],
                "number_of_the_match": k,
            }
            for col_name in df_official.columns.values:
                dictionary["official_" + col_name] = df_official[col_name][
                    indices[0, idx]
                ]
            for col_name in df_to_match.columns.values:
                dictionary["matched_" + col_name] = df_to_match[col_name][i]
        res.append(dictionary)
    df = pd.DataFrame(res)
    return df
