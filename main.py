"""
    Tictac
"""

import numpy as np


class Tictac:
    """Tictac module"""

    def __init__(self):
        self.board = np.zeros([3, 3], np.int8)
        self.color = -1

    def searchPossibleSteps(self):
        """search possible steps, return all steps available as an array"""
        return self == 0

    def play(self, x, y):
        """play at centain position"""
        if self.board[x][y] != 0:
            print 'Error, ' + str(x) + ',' + str(y) + ' is not a possible state'
            return
        else:
            self.board[x][y] = self.color
            self.color = self.color * -1
            (terminated, winner) = self.judgeTerminal()
            if terminated:
                return winner

    def judgeTerminal(self):
        """return terminal State and winner"""
        b = self.board
        diagSum1 = b[0][0] + b[1, 1] + b[2, 2]
        diagSum2 = b[0][2] + b[1, 1] + b[2, 0]
        if np.any(np.sum(b, 0) == 3) or np.any(np.sum(b, 1) == 3) or diagSum1 == 3 or diagSum2 == 3:
            return (True, 1)
        elif np.any(np.sum(b, 0) == -3) or np.any(np.sum(b, 1) == -3) or diagSum1 == -3 or diagSum2 == -3:
            return (True, -1)
        elif np.all(b != 0):
            return (True, 0)
        else:
            return (False, 0)

    def printBoard(self):
        print self.board
