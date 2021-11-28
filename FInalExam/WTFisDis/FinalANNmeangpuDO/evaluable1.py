import numpy as np
from P1 import P1_predict

if __name__ == '__main__':
  dat = np.load('P1data.npy', allow_pickle=True)
  X = dat[:,:-1].astype(float)
  Y = dat[:, -1]

  plabs = P1_predict(X)
  print(plabs)

  acc = np.mean(plabs == Y)
  print('Accuracy', acc)
