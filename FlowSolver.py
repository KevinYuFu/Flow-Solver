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
        self.grid = grid
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
        # find direction options
        pass

    # Converts a direction in to a coordinate direction
    def dirToCoord( c ):
        if c == 'u': return (0, 0)
        if c == 'd': return (0, 0)
        if c == 'l': return (0, 0)
        if c == 'r': return (0, 0)

class Grid():
    def __init__( self, data ):
        if isinstance(data, str):
            self.readFromFile( data )
        if isinstance(data, list):
            self.matrix = matrix
        else:
            print( 'data type does not match')
            #Throw an error here

        self.dim = len(self.matrix)

    # generate grid from given file
    def readFromFile( self, fname ):
        with open(fname) as f:
            data = f.readlines()
        data = [x.strip() for x in data] 
        data = [list(x) for x in data]
        self.matrix = data

    # Generator for coordinates
    def coords( self ):
        for y in range(self.dim):
            for x in range(self.dim):
                yield (x, y)

    # Returns values at given coord
    def at( self, a, b=None ):
        if isinstance(a, tuple):
            x, y = a
            return self.matrix[y][x]
        return self.matrix[b][a]

    # print grid (in future, make this overide print statement)
    def printGrid( self ):
        for y in range( self.dim ):
            for x in range( self.dim ):
                print( self.at(x, y) , end='')
            print()


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
    myGrid = Grid('testProblems/5x5.txt')
    myGrid.printGrid()
    print(myGrid.matrix)
    pass

if __name__ == '__main__':
    main()
