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

    # Find groups where of colours are adjacent to each other in initial state of game
    def findClusters( self ):
        visited = set()
        clusters = []
        for coord in self.grid.coords():
            cluster = self.searchCluster( coord, visited )
            if cluster: clusters.append( set(cluster) )
        return clusters

    def searchCluster( self, coord, visited ):
        if coord in visited: return None
        visited.add(coord)
        if self.grid.at(coord) == '0': return None
        cluster = set()
        cluster.add((self.grid.at(coord), coord))
        for neighbour in self.grid.neighbours( coord ):
            childBranch = self.searchCluster( neighbour, visited )
            if childBranch:
                cluster.update( childBranch )
        return cluster

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

    # Calculate how constrained this flow line is
    def constraints( self ):
        # Calucate by how close to the edge, and/or how much open space around it's two begining points
        pass

    # Converts a direction in to a coordinate direction
    def dirToCoord( c ):
        if c == 'u': return np.array((0, 1))
        if c == 'd': return np.array((0, -1))
        if c == 'l': return np.array((-1, 0))
        if c == 'r': return np.array((1, 0))

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

    # Generator for all neibours of the given coordinate
    def neighbours( self, coord ):
        for d in self.directions():
            newCoord = tuple(coord + d)
            if not self.outOfBound(newCoord):
                yield newCoord

    # Given a coord, return if out of bound or not
    def outOfBound( self, coord ):
        x, y = coord
        if x < 0 or y < 0 or x >= self.dim or y >= self.dim: return True
        return False

    # Generator for direction coords
    def directions( self ):
        yield np.array((0, 1))
        yield np.array((0, -1))
        yield np.array((-1, 0))
        yield np.array((1, 0))


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
    flowProblem = Flow(myGrid)
    print(flowProblem.findClusters())
    #print(flowProblem.searchCluster((4,0), set()))
    
    pass

if __name__ == '__main__':
    main()
