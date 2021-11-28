import numpy as np
from ANN_feAux import * 

def P1_predict(x):
  """
  x: np.array of shape (N,D)
  return y: list of classes
  """

  # WRITE YOUR CODE HERE!!!
  # Load params

  # paremeter 
  loaded_par = np.load('P1_dummypar.npy', allow_pickle=True).tolist()
  # Caution! you have to supply the data file! P1_dummypar.npy

  # Load weights
  loaded_net = np.load('P1_meang.npy', allow_pickle=True).tolist()
  # Caution! you have to supply the data file! P1_dummyweights0.npy

  # Pre-process the input
  px = x * loaded_par['p1']

  # Run network
  Yp = mlp2(loaded_net['c'], loaded_net['v'], 
          loaded_net['b'], loaded_net['w'], px, identity)

  # Post-process the output
  postY = Yp + loaded_par['p2']
  class_labels = ['A', 'B', 'C', 'D']
  predicted_labels = [class_labels[int(n)] for n in np.round(postY)]

  return predicted_labels


if __name__ == '__main__':
  dat = np.load('P1data.npy', allow_pickle=True)
  X = dat[:,:-1].astype(np.float)
  Y = dat[:, -1]

  print(X.shape)
  print(Y.shape)
  print(X[:5,:])
  print(Y[:5])
