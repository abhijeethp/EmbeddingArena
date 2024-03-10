import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class CosineSimilarity:
    def __init__(self):
        pass

    def name(self):
        return "cosine"

    def score(self,embedding_1, embedding_2):
        embedding_1 = np.array([embedding_1])
        embedding_2 = np.array([embedding_2])
        similarity_score = cosine_similarity(embedding_1, embedding_2)
        return similarity_score[0][0]