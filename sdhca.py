"""Implementation of steepest-descent hill-climbing algorithm.

Functions:
sdhca(initial_state) - Takes an array of integers, initial_state, as
input which specifies the inital configuration of the chess board.
The algorithm returns the final state as determined by the pseudocode
and the cost of that state.
"""


from utils import h, conflict


def sdhca(initial_state):

    current = initial_state
    n = len(current)
    currentVal = h(initial_state) # Value of 'current' state
    bestNeighbor = current.copy()
    neighborVal = 1000000 # Value of current neighbor being examined
    bestVal = neighborVal # Best value of neighbors seen so far
    count = 0

    while True:

        count += 1
        # Find the best neighbor of current state
        for i in range(len(current)):
            for j in range(n):

                # Copy current state to consider every neighbor
                currentNeighbor = current.copy()

                # Skip iteration if neighbor in consideration is same as current state
                if j == current[i]:
                    continue

                # Next neighbor in consideration
                currentNeighbor[i] = j # Examining a neighbor
                neighborVal = h(currentNeighbor)

                # Determines whether current neighbor is best neighbor seen so far
                if neighborVal < bestVal:
                    bestVal = neighborVal
                    bestNeighbor = currentNeighbor.copy()

        # Checking if 'best' neighbor is better than current state
        if bestVal < currentVal:
            currentVal = bestVal
            current = bestNeighbor
        else:
            return current, count


initial_state = [6, 2, 6, 0, 2, 1, 5]
print("Cost of initial state: ", h(initial_state))
sol, c = sdhca(initial_state)
