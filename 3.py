import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def main(data):
    tau = (1 + len(data)) // 4
    X_T = np.array(data.cost)[np.arange(tau) + np.arange(len(data) - tau + 1)[:, np.newaxis]]
    mat = np.dot(X_T.T, X_T) / len(data)
    vals, vecs = np.linalg.eig(mat)
    Y = np.dot(vecs.T, X_T.T)

    r = (1 + len(data)) // 16
    X_new = np.dot(vecs[:, :r], Y[:r])

    tmp_X = np.fliplr(X_new)
    smooth = np.array([np.mean(tmp_X.diagonal(tmp_X.shape[1] - 1 - i)) for i in range(len(data))])

    vecs_ast = vecs[:tau - 1, :r]
    vecs_tau = vecs[-1, :r]
    Q = X_T[-1, 1:]

    res = np.array(data.cost)
    p = len(data) // 4
    for i in range(p):
        x_new = np.dot(np.dot(vecs_tau, vecs_ast.T), Q) / (1 - np.dot(vecs_tau, vecs_tau.T))
        res = np.append(res, x_new)
        Q = np.append(Q, x_new)[1:]
    return res, smooth


if __name__ == '__main__':
    plt.plot(main(pd.read_csv('wheat.csv', delimiter=';', names=['date', 'cost']))[0])
    plt.show()