import numpy as np

def nearest_index_loop(arr, target):
    min_diff = float('inf')
    nearest_idx = -1
    for i, val in enumerate(arr):
        diff = abs(val - target)
        if diff < min_diff:
            min_diff = diff
            nearest_idx = i
    return nearest_idx

def nearest_index_numpy(arr, target):
    arr = np.array(arr)
    return np.argmin(np.abs(arr - target))
