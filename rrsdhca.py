"""Implementation of random-restart steepest descent hill climbing algorithm.

Functions:
rrsdhca(stop_criterion) - Takes an integer as a parameter which specifies
the maximum number of restarts allowed in a trial of the algorithm.
The function outputs the final state, whether it is a solution
or not, the number of restarts during execution and an array
containing the number of steps taken by each restart during
the algorithm's execution.

empirical(nIter, sc) - A meta-function that makes nIter calls to the
algorithm with a specified stop criterion sc. It returns an array
containing the number of restarts needed during each of the calls to
rrsdhca() and an array containing the number of steps taken in each
of the restarts across call to rrsdhca().
"""

import random
import statistics
from utils import h
from sdhca import sdhca


def rrsdhca(stop_criterion):

    goal = 0.0
    initial_state = [0, 0, 0, 0, 0, 0, 0]
    n = len(initial_state)
    bestState = initial_state
    bestVal = 100000
    restarts = []
    allSteps = []

    for i in range(stop_criterion):

        # print("Step Number: ", i)
        restarts.append(i)
        # Generating randomized initial state
        for j in range(n):
            initial_state[j] = random.randint(0, n - 1)

        # Running sdhca on initial state
        sol, steps = sdhca(initial_state)
        allSteps.append(steps)
        cost = h(sol)

        if cost < bestVal:
            bestState = sol
            bestVal = cost

        # If restarts == 0, no restarts were required to find a 'solution'
        if cost == goal:
            return sol, restarts, allSteps

    print("Solution not found")
    print("Final state: ", bestState)
    print("Cost of final state: ", bestVal)
    return None


def empirical(nIter, sc):

    totalRestarts = []
    totalSteps = []

    for i in range(nIter):
        solu, rs, ss = rrsdhca(sc)
        totalRestarts.append(rs[-1])

        totalSteps.append(sum(ss))

    return totalRestarts, totalSteps


stop_criterion = 100
output, Arestarts, Asteps = rrsdhca(stop_criterion)
print("number of restarts: ", Arestarts)
print("Number of steps: ", Asteps)


n = 1000
stop = 100
tR, tS = empirical(n, stop)
print("Total steps: ", tS)
avgR = statistics.mean(tR)
avgS = statistics.mean(tS)

print(avgR)  # Average number of restarts
print(avgS)  # Average number of steps across all restarts
