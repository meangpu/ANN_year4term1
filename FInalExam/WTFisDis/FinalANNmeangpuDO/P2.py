from ANN_feAux import * 

def P2_predict(x):
  """
  x: np.array of shape (N,D)
  return y: np.array of shape (N,1)
  """

  # WRITE YOUR CODE HERE!!!
  N, D = x.shape
  cutoff = 0.5
  yp = np.random.normal(0, 1, N).reshape((N,1)) # This is totally dummy.
  ybin = yp > cutoff

  return ybin


if __name__ == '__main__':
    dat = np.load('P2data.npy', allow_pickle=True)
    X = dat[:,:-1].astype(np.float)
    Y = dat[:, -1]

    pbin = P2_predict(X)
    print(pbin.shape)
    print(pbin[:5])

