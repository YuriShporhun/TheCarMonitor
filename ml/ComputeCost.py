import numpy as np

def ComputeCost(eX, Y, T):
    m = Y.shape[0]
    H = eX * T
    J = sum(np.power((H - Y), 2))
    J = J * (1.0 / (2 * m))
    return J
