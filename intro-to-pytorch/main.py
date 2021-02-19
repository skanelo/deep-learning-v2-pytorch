import torch

## Calculate the output of this network using the weights and bias tensors
k = activation(torch.matmul(features, weights.view(5, 1)).add(bias))

print(k)