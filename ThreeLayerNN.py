import numpy as np

INPUT_LAYER_COUNT = 3200
HIDDEN_LAYER_COUNT = 1600
OUTPUT_LAYER_COUNT = 8

def sigmoid(z):
    return np.divide(1.0, 1.0 + np.exp(-1 * z))

def initialize_theta(l_in, l_out):
    eps_init = 0.12
    return np.rand(l_out, 1 + l_in) * 2 * eps_init - eps_init

def costFunc()

