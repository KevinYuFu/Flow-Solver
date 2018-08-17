# Flow Solver

# Solve Flow as a CSP
#
#   Variables: each colour on the grid is a variable
#   Domain: the domain of each colour are possible paths to connect itself
#   Constraints are that no colour overlaps
#
# Additions rules:
#   A solved flow grid much have no empty cells.
#   For any cells with colour c, no more than 2 of its neigbours may also be colour c.

import numpy as np
import heapq

# CSP Class
class Flow():
    def __init__( self, grid ):
        Variables = []
        pass

    # Selects a Variable and a Path to attempt
    def selectPath():
        pass

    # Assigns Path onto the grid
    def assignPath():
        pass

    # Removes Path from the grid given a Variable
    def unassignPath():
        pass

class FlowLine():
    def __init__( self, myid, coord1, coord2, grid ):
        self.id = myid
        self.grid = grid
        self.x1, y1 = coord1
        self.x2, y2 = coord2
        self.visited = []

    # Finds a feasible path that will connect the two points
    def findPath( self ):
        pass


def solveFlow( problem ):
    if problem.isComplete():
        return problem

    while ( True ):
        # Problem instance picks a variable and Path to try
        variable, value = problem.selectPath()

        # if no more options, fail and exit
        if variable is None: return

        # test the selected path.
        problem.assign( variable, value )
        nextState = solveCSP( problem )
        if nextState:
            return nextState
        problem.unassign( variable )

    return False


# Main
def main():
    pass

if __name__ == '__main__':
    main()
