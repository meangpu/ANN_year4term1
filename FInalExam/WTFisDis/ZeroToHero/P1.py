import numpy as np
from ANN_feAux import * 

def P1_predict(x):
  """
  x: np.array of shape (N,D)
  return y: list of classes
  """

  # Load weights
  loaded_net = np.load('P1_NattapongData.npy', allow_pickle=True).tolist()

  # Run network
  Yp = mlp2(loaded_net['c'], loaded_net['v'], 
          loaded_net['b'], loaded_net['w'], x, identity)

  # Post-process the output
  realPredict = np.argmax(Yp, axis=1).reshape((-1,1))

  class_labels = ['A', 'B', 'C', 'D']

  predicted_labels = [class_labels[int(n)] for n in realPredict]

  return predicted_labels


if __name__ == '__main__':
  dat = np.load('P1data.npy', allow_pickle=True)
  X = dat[:,:-1].astype(np.float)
  Y = dat[:, -1]

  print(X.shape)
  print(Y.shape)
  print(X[:5,:])
  print(Y[:5])
