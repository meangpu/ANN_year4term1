from ANN_feAuxFixed1 import * 

def P2_predict(x):
  """
  x: np.array of shape (N,D)
  return y: np.array of shape (N,1)
  """

  dataName = "P2_NattapongData.npy"
  loaded_net = np.load(dataName, allow_pickle=True).tolist()
  yp = mlp2(loaded_net['c'], loaded_net['v'], 
          loaded_net['b'], loaded_net['w'], x, identity)

  realPredict = np.argmax(yp, axis=1).reshape((-1,1))

  return realPredict


if __name__ == '__main__':
    dat = np.load('P2data.npy', allow_pickle=True)
    X = dat[:,:-1].astype(np.float)
    Y = dat[:, -1]

    pbin = P2_predict(X)
    print(pbin.shape)
    print(pbin[:5])

