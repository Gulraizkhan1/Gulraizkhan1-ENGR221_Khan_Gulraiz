"""
Author: Gulraiz Khan
Filename: randomWalker.py
Description: Implementation of random recursive functions involving sleepwalking
Date: March 23, 2026
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

# input: start(int), low(int), hi(int)
# output: steps(int) - the total numnber of steps taken to reach an edge
# description: This function is similar to the rwsteps() function above but it uses a while loop instead of recursion to recreate the sleepwalker's movement. 
# The function continues until the sleepwalker reaches or goes past the boundaries.
def rwstepsLoop(start, low, hi):
    steps = 0
    current_pos = start

    while low < current_pos < hi:
        walkway = "_" * (hi - low)
        S_index = current_pos - low
        walkway = walkway[:S_index] + "S" + walkway[S_index:]
        
        print(" " + walkway + " ", "    ", current_pos, low, hi)
        
        current_pos += rs()
        steps += 1

    walkway = "_" * (hi - low)
    S_index = current_pos - low
    walkway = walkway[:S_index] + "S" + walkway[S_index:]
    print(" " + walkway + " ", "    ", current_pos, low, hi)

    return steps


if __name__ == '__main__':
    print(rs())