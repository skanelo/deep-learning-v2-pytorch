import torch
from rand_init import initialize
from activation import activation_func

features, weights, bias = initialize()

## Calculate the output of this network using the weights and bias tensors
k = activation_func(torch.matmul(features, weights.view(5, 1)).add(bias))

print(k)

print(initialize.__doc__)