import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import os
import sys
import math
import random

Brands = ['audi', 'bmw', 'chevrolet', 'honda', 'lexus', 'toyota', 'volkswagon', 'benz']


def load_training_set(inputPath):
    training_set = np.load(inputPath)
    features = training_set['arr_0']
    brands = training_set['arr_1']

    return features, brands


def get_probs(features, brands):
    prob_ones = np.zeros((8, 2500))
    prob_zeros = np.zeros((8, 2500))

    for i in range(8):
        car_index = i + 1
        ind = np.where(brands == car_index)[0]
        p_bi = len(ind) / len(brands)
        for j in range(features.shape[1]):
            num_ones = 0
            num_zeros = 0
            for index in ind:
                if features[index][j] == 1:
                    num_ones += 1
                else:
                    num_zeros += 0.01
            prob_ones[i][j] = (num_ones / (num_ones + num_zeros)) * p_bi
            prob_zeros[i][j] = 1 - prob_ones[i][j]
    for i in range(8):
        plt.figure()
        plt.imshow(np.reshape(prob_zeros[i, :], (50, 50)))
    plt.show()
    return prob_ones


def get_likelihood(prob_ones, prob_zeros, brand, input):
    

features, brands = load_training_set('nb_data.npz')
get_probs(features, brands)
