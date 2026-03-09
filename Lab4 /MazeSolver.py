"""
Author: Gulraiz Khan
Filename: MazeSolver.py
Description: Implementation of a Mazer Solver class and its properties 
Date: Feb 23, 2026
"""

import sys, os 
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object (Stack or Queue)

    # Input: self, row, col
    # Output: Boolean 
    # Description: This method makes sure if the tile is visitable and valid to move to
    def tileIsVisitable(self, row, col):
        # First we check if the coordinates are actually inside the maze
        if 0 <= row < self.maze.num_rows and 0 <= col < self.maze.num_cols:
            # If true we look at the tile at that coordinate with row and column
            tile = self.maze.contents[row][col]
            # Then we check if the tile is not a wall and if we havn't already visited it before
            if not tile.getIsWall() and not tile.isVisited():
                # If the tile passes all these if statements then we return True, which means we can go there 
                return True
        # If the If statements are not true, then we return False meaning we can can't go there
        return False
        
    # Input: self
    # Output: goal tile or None  
    # Description: This method solves the maze using the search structure 
    def solve(self):
        # This starts the search and adds the initial starting tile to the search structure
        self.ss.add(self.maze.start)

        # This while loop searches as long as there are more tiles in our search structure
        while not self.ss.isEmpty():
            # This look at the next tile out to look at it 
            current = self.ss.remove()
            # This marks the tile so we know that we have visited it altready
            current.visit()

            # Through this If statement we check if we have arrived at the goal tile that we wanted
            # And then we return that 
            if current == self.maze.goal:
                return current
            
            # Through this we get the coordinates for the neighbors in the north, south, east, west
            current_row = current.getRow()
            current_col = current.getCol()

            neighbors = [
                # North
                (current_row - 1, current_col), 
                # South
                (current_row + 1, current_col),
                # East 
                (current_row, current_col + 1),
                # West
                (current_row, current_col - 1)
            ]

            # Then we look at each neighbor to see if there a valid path we can take
            for r, c in neighbors:
                # This if statement checks if the neighboring tile is valid to visit
                if self.tileIsVisitable(r, c):
                    neighbor_tile = self.maze.contents[r][c]
                    neighbor_tile.setPrevious(current)
                    self.ss.add(neighbor_tile)
        # We retunn None if the structure is empty and we didn't find a path to our goal
        return None

     # Add any other helper functions you might want here

    # Input: self
    # Output: path list or empty list 
    # Description: This method stores the list of the path that is taken to go from start to goal 
    def getPath(self):
        # We first start with an empty list to store the tiles
        # And we also set curr to the goal tile that we want to get to
        path = []
        curr = self.maze.goal

        # This if statement checks if the goal tile is not reached or has no previous tile
        # And if it isn't the starting tile. If this statement is true then we return the empty list meaning no path was found
        if curr.getPrevious() is None and curr != self.maze.start:
            return []
        
        # This while loop follows the previous pointers from the goal tile to the starting tile
        while curr is not None:
            path.append(curr)
            curr = curr.getPrevious()

        # At the end we return the list in reversed order so that we can go from the starting tile to the goal tile
        return path[::-1]

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()