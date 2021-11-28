import numpy as np

def sigmoid(a, safe=True):
    aa = a.copy()

    if safe:
      aa[aa < -709] = -709

    h = 1/(1 + np.exp(-aa))
    return h

def identity(a):
    return a

def get_predict(A2):
  A2 = A2.T
  return np.argmax(A2, 0).reshape((-1,1))

def get_accuracy(predictions, Y):
  return np.sum(predictions == Y) / Y.size


def mlp2(c, v, b, w, X, oact=identity):

    a = b.T + np.dot(X, w.T)            # a: array N x M
    z = sigmoid(a)                      # z: array N x M

    a2 = c.T + np.dot(z, v.T)           # a2: array N x K
    yhat = oact(a2)                     # yhat: array N x K

    return yhat

def mse_loss(x, y, yp):

    return np.mean((yp - y)**2)

def train_mlp2(c, v, b, w, X, Y, allY, lr1, lr2, nepochs, 
               oact=identity, loss=mse_loss, disp=False, 
               val=None, val_criteria=1):

  N, D = X.shape

  losses = []
  accuracy_list = []

  # For early stopping
  
  best_val_loss = np.inf
  best_params = (c, v, b, w)
  val_count = 0


  # Learning
  for i in range(nepochs):

      # Forward pass
      a = b.T + np.dot(X, w.T)            # a: array N x M
      z = sigmoid(a)                      # z: array N x M
      a2 = c.T + np.dot(z, v.T)           # a2: array N x K
      z2 = oact(a2)                       # z2: array N x K
      yhat = z2                           # yhat: array N x K
      # yhat = [[[0.1], [0.2], [0.6], [0.1]]

      # Backward pass
      delta2 = yhat - Y                   # delta2: array N x K
      OneVec = np.ones(N).reshape((1,-1)) # OneVec: array 1 x N
      dLc = np.dot( OneVec, delta2 ).T    # dLc: array K x 1
      dLv = np.dot( z.T, delta2 ).T       # dLv: array K x M
      H = np.multiply(1 - z, z)           # H: array N x M
      delta1 = np.dot(delta2, v) * H      # delta1: array N x M
      dLb = np.dot( OneVec, delta1 ).T    # dLb: array M x 1
      dLw = np.dot( X.T, delta1 ).T       # dLw: array M x D

      lossi = loss(X, Y, yhat)
      
      if np.isnan(lossi):  
          print('Reach NaN. Terminated.')
          break

      losses.append(lossi)
      accuracy_list.append(get_accuracy(get_predict(yhat), allY))
      

      c -= dLc * lr2
      v -= dLv * lr2
      b -= dLb * lr1
      w -= dLw * lr1

      if disp:
        if i % 5000 == 0:
            print('loss = %.4f' % lossi)

      if val is not None:
        # Do early stopping
        # Here, we use a simple strategy.

        # (1) Check validate set
        valx, valy = val
        valyp = mlp2(c, v, b, w, valx, oact)

        val_loss = loss(valx, valy, valyp)
        print(i, '* val loss=', val_loss)

        if val_loss < best_val_loss:
          best_val_loss = val_loss
          best_params = (c, v, b, w)
          val_count = 0

        elif val_loss > best_val_loss:
          val_count += 1

          if val_count >= val_criteria:
            print('Early stopping criteria is met at', i)
            c, v, b, w = best_params
            break
          # enf if val_criteria
        # enf if val_loss
      # end if val

  # end for i

  return c, v, b, w, losses, accuracy_list


def ReLU(Z):
    return np.maximum(Z, 0)

def ReLU_deriv(Z):
    return Z > 0

def train_mlp2_meangpu(b2, w2, b1, w1, X, Y, allY, lr1, lr2, nepochs, 
               oact=identity, loss=mse_loss, disp=False, 
               val=None, val_criteria=1):

  N, D = X.shape
  m, n = X.shape

  losses = []
  accuracy_list = []

  # For early stopping
  
  best_val_loss = np.inf
  best_params = (b2, w2, b1, w1)
  val_count = 0


  # Learning
  for i in range(nepochs):

      # Forward pass
      z1 = b1.T + np.dot(X, w1.T)            # a: array N x M
      a1 = ReLU(z1)                      # z: array N x M
      z2 = b2.T + np.dot(a1, w2.T)           # a2: array N x K
      a2 = softmax(z2)                       # z2: array N x K
      yhat = a2                           # yhat: array N x K
      # yhat = [[[0.1], [0.2], [0.6], [0.1]]

      # Backward pass
      print(Y)
      print(a2)
      dZ2 = a2 - Y                 # delta2: array N x K
      # w2 = (4, 4)
      # dZ2 = (3440, 4)

      print(w2.shape)
      print(dZ2.shape)

      dW2 = 1 / m * dZ2.dot(a1.T)
      db2 = 1 / m * np.sum(dZ2)
      
      dZ1 = w2.T.dot(dZ2) * ReLU_deriv(z1)
      
      dW1 = 1 / m * dZ1.dot(X.T)
      db1 = 1 / m * np.sum(dZ1)

      lossi = loss(X, Y, yhat)
      
      if np.isnan(lossi):  
          print('Reach NaN. Terminated.')
          break

      losses.append(lossi)
      accuracy_list.append(get_accuracy(get_predict(yhat), allY))
      

      b2 -= db2 * lr2
      w2 -= dW2 * lr2
      b1 -= db1 * lr1
      w1 -= dW1 * lr1

      if disp:
        if i % 5000 == 0:
            print('loss = %.4f' % lossi)

      if val is not None:
        # Do early stopping
        # Here, we use a simple strategy.

        # (1) Check validate set
        valx, valy = val
        valyp = mlp2(b2, w2, b1, w1, valx, oact)

        val_loss = loss(valx, valy, valyp)
        print(i, '* val loss=', val_loss)

        if val_loss < best_val_loss:
          best_val_loss = val_loss
          best_params = (b2, w2, b1, w1)
          val_count = 0

        elif val_loss > best_val_loss:
          val_count += 1

          if val_count >= val_criteria:
            print('Early stopping criteria is met at', i)
            b2, w2, b1, w1 = best_params
            break
          # enf if val_criteria
        # enf if val_loss
      # end if val

  # end for i

  return b2, w2, b1, w1, losses, accuracy_list


def cross_entropy(x, y, yp):
    
    return np.sum(-np.log(yp[y == 1]))+np.sum(-np.log(1-yp[y == 0]))


def onehot(y, classes=None):
  '''
  input y: N x 1
  classes: unique values of y, e.g., [0, 1, 2]
  output yhot: N x K
  '''

  if classes is None:
    classes = np.unique(y)

  K = len(classes)
  N = y.shape[0]
  codebook = np.diag(np.ones(K))

  yhot = codebook[y[:,0]]

  return yhot


def softmax(a):
  '''
  a: N x K
  '''
  amax = np.max(a, axis=1, keepdims=True)
  
  ea = np.exp(a - amax)

  s = np.sum(ea, axis=1, keepdims=True)
  z = ea/s
  return z

def cc_entropy(x, yonehot, yp, eps=1e-323, do_sum=True):
    '''
    yonehot: N x K  (in one-hot coding)
    yp: N x K
    '''
    Ln = -np.log(np.sum(yonehot * yp, axis=1, keepdims=True) + eps)

    if do_sum:
      return np.sum(Ln)

    return Ln              