import numpy as np
from P2 import P2_predict

if __name__ == '__main__':
    dat = np.load('P2data.npy', allow_pickle=True)
    X = dat[:,:-1].astype(float)
    Y = dat[:, -1].reshape((-1,1))

    pbin = P2_predict(X)

    acc = np.mean(pbin == Y)
    print('Accuracy = ', acc)

    # Compute F-score
    eps = 1e-12
    TP = np.sum( (pbin == 1)*(Y == 1) , axis=0).item()
    FP = np.sum( (pbin == 1)*(Y == 0) , axis=0 ).item()
    FN = np.sum( (pbin == 0)*(Y == 1) , axis=0 ).item()

    P = TP / (TP + FP + eps)
    R = TP / (TP + FN + eps)
    F = 2*P*R/(P +R + eps)

    print('\nTest F-score, F = {:.4f}'.format(F))
