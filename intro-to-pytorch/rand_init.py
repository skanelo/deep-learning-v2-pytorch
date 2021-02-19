import torch

def initialize():
    """Auxiliary Function for variable initialization.

       Arguments:
       ----------

       Returns:
       features, weights, bias
    """
    
    ### Generate some data
    torch.manual_seed(7) # Set the random seed so things are predictable

    # Features are 5 random normal variables
    features = torch.randn((1, 5))
    # True weights for our data, random normal variables again
    weights = torch.randn_like(features)
    # and a true bias term
    bias = torch.randn((1, 1))

    return features, weights, bias