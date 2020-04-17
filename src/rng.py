import numpy as np
import random

def inspector1_component1_rng():
    return random_number_generator(np.array(open('../data/servinsp1.dat').read().splitlines()))

def inspector2_component2_rng():
    return random_number_generator(np.array(open('../data/servinsp22.dat').read().splitlines()))

def inspector2_component3_rng():
    return random_number_generator(np.array(open('../data/servinsp23.dat').read().splitlines()))

def workstation1_rng():
    return random_number_generator(np.array(open('../data/ws1.dat').read().splitlines()))

def workstation2_rng():
    return random_number_generator(np.array(open('../data/ws2.dat').read().splitlines()))

def workstation3_rng():
    return random_number_generator(np.array(open('../data/ws3.dat').read().splitlines()))

def random_2_3():
    return random.randint(2, 3)

def random_number_generator(data):
    floatData = data[0:300].astype(np.float)
    total = 0
    for fl in floatData:
        total += fl
    sample_mean = total / 300.00
    return np.random.exponential(sample_mean, 1)[0]