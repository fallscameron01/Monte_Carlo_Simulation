"""
Plays many games of Craps to find the probability of winning.
Uses numpy to increase speed.
"""

import numpy as np

def roll(iterations):
    return np.random.randint(1, 7, size=iterations) + np.random.randint(1, 7, size=iterations)

