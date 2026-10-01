import numpy as np


def cosine_similarity(v1, v2):
    if len(v1) != len(v2) or len(v1) == 0:
        return False
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return False
    return float(np.dot(v1, v2) / (norm_v1 * norm_v2))