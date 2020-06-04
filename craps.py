"""
Plays many games of Craps to find the probability of winning.
Uses numpy to increase speed.
"""

import numpy as np

def roll(iterations):
    return np.random.randint(1, 7, size=iterations) + np.random.randint(1, 7, size=iterations)

def playGames(numGames):
    # Part 1
    games = roll(numGames)

    ## Initial Wins (7, 11)
    wins = np.where((games == 7) | (games == 11))
    games = np.delete(games, wins)
    numWins = np.size(wins)

    ## Initial Losses (2, 3, 12)
    losses = np.where((games == 2) | (games == 3) | (games == 12))
    games = np.delete(games, losses)
    numLosses = np.size(losses)

    # Part 2
    while(np.size(games) != 0):
        # Reroll for each game not won/lost
        newRolls = roll(np.size(games))

        # Win if same on reroll
        wins = np.where(games == newRolls)
        numWins += np.size(wins)
        games = np.delete(games, wins)
        newRolls = np.delete(newRolls, wins)

        # Lose if reroll is 7
        losses = np.where(newRolls == 7)
        numLosses += np.size(losses)
        games = np.delete(games, losses)

    return (numWins, numLosses)


NUM_GAMES = 1000000
results = playGames(NUM_GAMES)
print(results[0] / NUM_GAMES)
print(results[1] / NUM_GAMES)