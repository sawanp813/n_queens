"""Implementation of genetic algorithm for N-Queens Problem.

Functions:
sdhca(initial_state) - Takes an array of integers, initial_state, as
input which specifies the inital configuration of the chess board.
The algorithm returns the final state as determined by the pseudocode
and the cost of that state.
"""

import random
import statistics
from utils import h


def genetic(mr, popsize, niter):

    pop = []
    n = 7
    qp = 21  # 7 choose 2 - non-attacking queen pairs
    costs = []
    minH = 1000000

    # Generating initial population
    for i in range(popsize):
        s = [0, 0, 0, 0, 0, 0, 0]
        for j in range(n):
            s[j] = random.randint(0, n-1)
        pop.append(s)

    for t in range(niter):

        costs = []

        # Computing costs
        for w in range(popsize):
            stateCost = h(pop[w])
            if stateCost < minH:
                minH = stateCost

            costs.append(qp - stateCost)

        probs = []
        for c in range(popsize):
            p = (costs[c])/sum(costs)
            probs.append((p, pop[c]))

        # Sort probs array of tuples by the probability of each state
        probs = sorted(probs)

        # Generating parents
        pairs = []

        probabilities = []

        for tup in probs:
            probabilities.append(tup[0])

        origProbs = probabilities.copy()

        # ensure that two parents in a pair are not the same
        for k in range(2):
            # parents in a pair
            for y in range(2):
                k = random.random()
                if k < probabilities[0]:
                    pairs.append(probs[0][1])
                    probabilities[0] = 0
                elif k < probabilities[0]+probabilities[1]:
                    pairs.append(probs[1][1])
                    probabilities[1] = 0
                elif k < probabilities[0]+probabilities[1]+probabilities[2]:
                    pairs.append(probs[2][1])
                    probabilities[2] = 0
                else:
                    pairs.append(probs[3][1])
                    probabilities[3] = 0
                probabilities = [float(i) / sum(probabilities) for i in probabilities]

            probabilities = origProbs.copy()

        # Recombination
        newPop = []
        for l in range(2):
            recomb = random.randint(1, n-1)
            child1 = pairs[2*l][:recomb] + pairs[2*l+1][recomb:]
            child2 = pairs[2*l+1][:recomb] + pairs[2*l][recomb:]
            newPop.append(child1)
            newPop.append(child2)

        for po in range(popsize):
            z = random.random()
            if z < mr:
                x = random.randint(0, n-1)
                newPop[po][x] = random.randint(0, n-1)

        pop = newPop

    return minH


mr = 0.1
psize = 4
iterations = 100

nRuns = 10000

minHs = []
for run in range(nRuns):
    print("RunID: ", run)
    minHs.append(genetic(mr, psize, iterations))

print(statistics.mean(minHs))
