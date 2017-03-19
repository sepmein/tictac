"""
    Tictac
"""

import numpy as np


class Tictac:
    """Tictac module"""

    def __init__(self):
        self.ended = False
        self.board = np.zeros([3, 3], np.int8)
        self.color = -1

    def search_possible_steps(self):
        """search possible steps, return all steps available as an array"""
        if self.ended:
            return False
        possible_steps_turple = (self.board == 0)
        possible_steps = np.transpose(possible_steps_turple.nonzero())
        return possible_steps

    def get_next_states(self):
        if self.ended:
            return False
        possible_steps = self.search_possible_steps()
        next_color = self.color * -1
        n = possible_steps.shape[0]
        next_states = np.zeros([n, 3, 3])
        for i in range(n):
            x, y = possible_steps[i]
            next_states[i][x][y] = next_color
        return next_states

    def play(self, x, y):
        """play at centain position"""
        if self.board[x][y] != 0:
            print 'Error, ' + str(x) + ',' + str(y) + ' is not a possible state'
            return
        else:
            self.board[x][y] = self.color
            self.color = self.color * -1
            (terminated, winner) = self.judge_terminal()
            if terminated:
                self.ended = True
                return winner

    def judge_terminal(self):
        """return terminal State and winner"""
        board = self.board
        diagsum1 = board[0][0] + board[1][1] + board[2][2]
        diagsum2 = board[0][2] + board[1][1] + board[2][0]
        if np.any(np.sum(board, 0) == 3) or np.any(np.sum(board, 1) == 3) \
                or diagsum1 == 3 or diagsum2 == 3:
            return (True, 1)
        elif np.any(np.sum(board, 0) == -3) or np.any(np.sum(board, 1) == -3) \
                or diagsum1 == -3 or diagsum2 == -3:
            return (True, -1)
        elif np.all(board != 0):
            return (True, 0)
        else:
            return (False, 0)

    def print_board(self):
        """print out the board"""
        print self.board

    def generate_and_store_game_by_policy(self, policy, db):
        """generate a game with policy"""
        while self.ended != True:
            actions = self.search_possible_steps()
            action = policy(self.board, actions)
            value = db.find_value(self.state)
            # next_state = self.play(action)
            # next_value = db.find_value(next_state)
            print self.board

    def reset(self):
        """reset"""
        self = self.__init__()
        return self
