import torch

def activation_func(x):
    """ Sigmoid activation function 
    
        Arguments
        ---------
        x: torch.Tensor
    """

    print("activation function has just been called!")
    return 1/(1+torch.exp(-x))