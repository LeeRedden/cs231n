import numpy as np
import matplotlib.pyplot as plt
import math

import sys # for debugging


def init_two_layer_model(input_size, hidden_size, output_size):
  """
  Initialize the weights and biases for a two-layer fully connected neural
  network. The net has an input dimension of D, a hidden layer dimension of H,
  and performs classification over C classes. Weights are initialized to small
  random values and biases are initialized to zero.

  Inputs:
  - input_size: The dimension D of the input data
  - hidden_size: The number of neurons H in the hidden layer
  - ouput_size: The number of classes C

  Returns:
  A dictionary mapping parameter names to arrays of parameter values. It has
  the following keys:
  - W1: First layer weights; has shape (D, H)
  - b1: First layer biases; has shape (H,)
  - W2: Second layer weights; has shape (H, C)
  - b2: Second layer biases; has shape (C,)
  """
  # initialize a model
  model = {}
  model['W1'] = 0.00001 * np.random.randn(input_size, hidden_size)
  model['b1'] = np.zeros(hidden_size)
  model['W2'] = 0.00001 * np.random.randn(hidden_size, output_size)
  model['b2'] = np.zeros(output_size)
  return model

def two_layer_net(X, model, y=None, reg=0.0):
  """
  Compute the loss and gradients for a two layer fully connected neural network.
  The net has an input dimension of D, a hidden layer dimension of H, and
  performs classification over C classes. We use a softmax loss function and
  L2 regularization the the weight matrices.

  Inputs:
  - X: Input data of shape (N, D). Each X[i] is a training sample.
  - model: Dictionary mapping parameter names to arrays of parameter values.
    It should contain the following:
    - W1: First layer weights; has shape (D, H)
    - b1: First layer biases; has shape (H,)
    - W2: Second layer weights; has shape (H, C)
    - b2: Second layer biases; has shape (C,)
  - y: Vector of training labels. y[i] is the label for X[i], and each y[i] is
    an integer in the range 0 <= y[i] < C. This parameter is optional; if it
    is not passed then we only return scores, and if it is passed then we
    instead return the loss and gradients.
  - reg: Regularization strength.

  Returns:
  If y not is passed, return a matrix scores of shape (N, C) where scores[i, c]
  is the score for class c on input X[i].

  If y is not passed, instead return a tuple of:
  - loss: Loss (data loss and regularization loss) for this batch of training
    samples.
  - grads: Dictionary mapping parameter names to gradients of those parameters
    with respect to the loss function. This should have the same keys as model.
  """

  # unpack variables from the model dictionary
  W1,b1,W2,b2 = model['W1'], model['b1'], model['W2'], model['b2']
  N, D = X.shape

  # compute the forward pass
  scores = None
  #############################################################################
  # TODO: Perform the forward pass, computing the class scores for the input. #
  # Store the result in the scores variable, which should be an array of      #
  # shape (N, C).                                                             #
  #############################################################################
  N, D = X.shape
  C = b2.shape
  C = C[0]
  
  # compute the forward pass
  scores = np.ones((N,C))
  
  for i in range(0,1):
    # (H)    = (D) * (D,H) + (H)
    layer1D = np.dot( X , W1 )
    layer1B = layer1D + b1
    layer1 = np.maximum( 0, layer1B )
    
    # (C)    = (H) * (H,C) + (C) 
    layer2D = np.dot( layer1, W2 ) 
    layer2B = layer2D + b2 
    
    scores = layer2B
  #############################################################################
  #                              END OF YOUR CODE                             #
  #############################################################################
  
  # If the targets are not given then jump out, we're done
  if y is None:
    return scores

  # compute the loss
  loss = None
  #############################################################################
  # TODO: Finish the forward pass, and compute the loss. This should include  #
  # both the data loss and L2 regularization for W1 and W2. Store the result  #
  # in the variable loss, which should be a scalar. Use the Softmax           #
  # classifier loss. So that your results match ours, multiply the            #
  # regularization loss by 0.5                                                #
  #############################################################################
  
  # data loss
  dataLoss = 0
  
  for i in range(0, N):
    maxInstance = np.max(scores[i,])
    den = 0
    for j in range(0, C):
      den += np.exp( scores[(i,j)] - maxInstance )
    dataLoss -= np.log( np.exp( scores[i,y[i]] - maxInstance ) / den )
  dataLoss =  dataLoss/N    
  
  # L2 loss
  regLoss = math.pow( np.linalg.norm( W1, 'fro' ), 2 ) + math.pow( np.linalg.norm( W2, 'fro' ), 2 )
  #regLoss = 0.5 * reg * sum( np.sum(W*W) for W in [W1,W2] )
  #regLoss = regLoss/N
  
  #print loss
  loss = dataLoss + 0.5 * reg * regLoss
  #############################################################################
  #                              END OF YOUR CODE                             #
  #############################################################################

  # compute the gradients
  grads = {}
  #############################################################################
  # TODO: Compute the backward pass, computing the derivatives of the weights #
  # and biases. Store the results in the grads dictionary. For example,       #
  # grads['W1'] should store the gradient on W1, and be a matrix of same size #
  #############################################################################
#    # (H)    = (D) * (D,H) + (H)
#    layer1D = np.dot( X[i] , W1 )
#    layer1B = layer1D + b1
#    layer1 = np.maximum( 0, layer1B )

#    # (C)    = (H) * (H,C) + (C) 
#    layer2D = np.dot( layer1, W2 ) 
#    layer2B = layer2D + b2 

#    scores[i] = layer2B

#  target = np.zeros( scores.shape )
#  for ii in range( 0, y.size ):
#    target[ ii, y[ii] ] = 1;
#
#  d_layer2B = scores - target # problem computing d_b2, possibly target is wrong
#  
#  d_layer2D = d_layer2B #np.ones( layer2B.shape ); 
#  d_b2 = d_layer2B #np.ones( layer2B.shape );
#  
#  d_layer1 = np.dot( W2, d_layer2D.T )
#  d_W2 = np.dot( layer1.T, d_layer2D )
#  d_layer1B = d_layer1.T
#  d_layer1B[ layer1B < 0 ] = 0
#  d_layer1D = d_layer1B
#
#  d_b1 = d_layer1B
#  d_x = np.dot( W1, d_layer1D.T )
#  d_W1 = np.dot( X.T, d_layer1D )
#
#  grads['W1'] = d_W1
#  grads['b1'] = d_b1.mean(0)
#  grads['W2'] = d_W2
#  grads['b2'] = d_b2.mean(0)  # d_b1 is 2D 

# from https://github.com/ddetone/cs231n/blob/master/assignment2/cs231n/classifiers/neural_net.py
  fc1 = np.dot(X,W1) + b1
  relu = np.maximum(0,fc1)
  scores = np.dot(relu,W2) + b2 #Same as fc2
  
  
  expsc = np.exp(scores)
  sumsc = np.sum(expsc, axis=1)
  logsc = np.log(sumsc)
  softmax = -scores[np.arange(N), y] + logsc
  
  
  loss = np.sum(softmax)/N + 0.5*reg*(np.sum(W1*W1) + np.sum(W2*W2))
  
  # Initialize stuffs to zero
  dscores = np.zeros_like(scores)
  dW1 = np.zeros_like(W1)
  db1 = np.zeros_like(b1)
  dW2 = np.zeros_like(W2)
  db2 = np.zeros_like(b2)

  # backprop loss
  dsoftmax = np.ones(N)/N
  dW1 += reg * W1
  dW2 += reg * W2
  # backprop softmax
  dscores[np.arange(N), y] -= dsoftmax
  
  dlogsc = dsoftmax
  # backprop logsc
  dsumsc = dlogsc / sumsc
  # backprop sumsc
  dexpsc = np.outer(dsumsc, np.ones(C))
  # backprop expsc
  dscores += np.exp(scores) * dexpsc
  # backprop scores
  drelu = np.dot(dscores, W2.T) #W2 * dscores 
  dW2 += np.dot(relu.T, dscores) #relu * dscores
  db2 += np.dot(dscores.T, np.ones(N)) #dscores
  # backprop relu
  ind_fc1 = np.zeros_like(fc1)
  ind_fc1[fc1>0] = 1
  dfc1 = ind_fc1 * drelu
  # backprop fc1
  dW1 += np.dot(X.T, dfc1) #X * dfc1
  db1 += np.dot(dfc1.T, np.ones(N)) #dfc1

  grads['W1'] = dW1
  grads['b1'] = db1
  grads['W2'] = dW2
  grads['b2'] = db2
  
  #############################################################################
  #                              END OF YOUR CODE                             #
  #############################################################################

  return loss, grads

