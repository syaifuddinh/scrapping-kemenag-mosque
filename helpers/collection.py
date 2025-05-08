import numpy as np

def DivideCollection(array, n):
    row_size = len(array) // n

    result = np.array_split(array, n)
    result = [list(r) for r in result]
    return result