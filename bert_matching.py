import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


def bert_match(
    df_official: pd.DataFrame,
    col_official: str,
    df_to_match: pd.DataFrame,
    col_to_match: str,
    k: int = 1,
) -> pd.DataFrame:
    """Take 2 dataframe and match one columns of each dataframe together using BERT tool and FAISS match

    Args:
        df_official (pd.DataFrame): the dataframe containing the reference data
        col_official (str): the columns of the reference dataframe you want to match
        df_to_match (pd.DataFrame): datafrane containing th data you want to match with the reference
        col_to_match (str): column of the to_mach dataframe you want to use
        k (int, optional): number of match by row of the to_match dataframe. Defaults to 1.

    Returns:
        pd.DataFrame: a dataframe containing the content of the to_match dataframe where information on the matchs were added
    """
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
) -> pd.DataFrame:
    """Take 2 pandas dataframe and 2 corresponding embeddings and return the matching using FAISS method

    Args:
        df_official (pd.DataFrame): the dataframe containing the reference data
        official_embeddings (pd.DataFrame): embeddings of the reference data
        df_to_match (pd.DataFrame): datafrane containing th data you want to match with the reference
        to_match_embeddings (pd.DataFrame): embeddings of the reference data
        k (int, optional): number of match per row. Defaults to 1.

    Returns:
        pd.DataFrame: a dataframe containing the content of the to_match dataframe where information on the matchs were added
    """
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
