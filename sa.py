"""Implementation of simulated annealing algorithm

Functions:
sa() - Function that runs simulated annealing to solve
the 7-Queens problem. It returns the minimum cost encountered
across all generated states.
"""

import random
import math
import statistics
from utils import h, conflict


def sa():

    initial_state = [0, 0, 0, 0, 0, 0, 0]
    n = len(initial_state)
    minH = 100000

    # Generating initial state
    for j in range(len(initial_state)):
        initial_state[j] = random.randint(0, n-1)

    current_state = initial_state
    curCost = h(current_state)

    # Start of algorithm
    for i in range(100):

        T = 1-(i/100)

        if T == 0:
            break

        curNeighbor = current_state.copy()

        col = random.randint(0, n-1)
        row = random.randint(0, n-1)

        curNeighbor[col] = row
        nCost = h(curNeighbor)

        delta = curCost - nCost
        if delta > 0:
            current_state = curNeighbor
            curCost = nCost
            minH = nCost
        else:
            p = math.pow(math.e, -delta/T)
            x = random.random()
            if x <= p:
                current_state = curNeighbor
                curCost = nCost

    return minH

costs = []
numIter = 10000
for i in range(numIter):
    print("Iteration: ", i)
    H = sa()
    costs.append(H)

print("Empirical Average: ", statistics.mean(costs))
