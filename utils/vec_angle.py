import numpy as np


def vec_angle(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """2つのベクトル間の角度[rad]を計算する
    Args:
        vec1 (np.ndarray): ベクトル1
        vec2 (np.ndarray): ベクトル2
    Returns:
        float: 2つのベクトル間の角度[rad]
    """
    cos_theta = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return np.arccos(round(cos_theta, 3))
