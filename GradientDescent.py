import numpy as np
from ComputeCost import *

def GradientDescent(X, Y, alpha, num_iters):
    ones_string = '1 ;' * X.shape[0]
    ones_string = ones_string[0:len(ones_string)-1]
    ones = np.matrix(ones_string)
    eX = np.concatenate((ones, X), axis = 1)
    theta_string = '0.0 ;' * eX.shape[1]
    theta_string = theta_string[0:len(theta_string)-1]
    T = np.matrix(theta_string)
    m = X.shape[0]
    J_Hist = []
    for iter in range(0, num_iters):
        H = eX * T
        temp = [0 for x in range(T.shape[0])]
        for index in range(0, T.shape[0]):
            temp[index] = T[index, 0] - alpha * (1.0 / m) * ((H - Y).T * eX[:, index])
        for index in range(0, T.shape[0]):
            T[index, 0] = temp[index]
        J = ComputeCost(eX, Y, T)
        J_Hist.append(J[0, 0])
    return (T, J_Hist)