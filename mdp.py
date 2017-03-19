"""
	imports
"""
from tictac import Tictac
from pymongo import MongoClient
from random import random

"""
	Markov Decision Process
	Conponents:
		state - store values
		action
		state_action pair - store rewards and quality
			reward
			q function of (s,a)
		# policies
	Retrive and Store these component to mongodb
"""


DEFAULT_REWARD = 0
DEFAULT_VALUE = 0
GAMMA = 0.9

""" DB interfaces """


class DB:
    """DB interface"""

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.tictac
        self.states = self.db.states
        self.actions = self.db.actions
        self.state_action = self.db.state_action

    def find_state(self):
        """find state"""
        pass

    def store_state(self):
        """store state"""
        pass

    def find_action(self):
        """"find action"""
        pass

    def store_action(self):
        """store action"""
        pass

    def find_state_action(self):
        """find state action"""
        pass

    def store_state_action(self):
        """store state action"""
        pass

    def find_reward(self):
        """find reward"""
        pass

    def store_reward(self):
        """store reward"""
        pass

    def find_value(self):
        """find value"""
        pass

    def store_value(self):
        """store value"""
        return 0

        def get_next_state(self, state, action):
            """get next state"""
            pass

        def get_next_states(self, state, actions):
            """get next states"""
        pass


class Policy:
    """define the policy"""

    def __init__(self, gamma, tao):
        self.gamma = gamma or 0.9
        self.tao = tao or 0.1

    def pai(self, state, actions, db):
        """given a state s and actions collection A, calculate the right action a"""
        # at some rate select random action
        # return optimal policy otherwise
        if random() < tao:
            random_index = int(len(actions) * random())
            return actions[random_index]
        else:
            (action, Q) = bellman_value_equation(state, actions, db)
            return action


"""Value Network"""


def bellman_quality_equation(state, action, gamma, db):
    """
            Bellman quality equation, simplified version
            Q(s,a) = R(s,a) + gamma * simga(T(s, a, s') * V(s'))
    """
    reward = db.find_reward(state, action)
    next_state = db.get_next_state(state, action)
    next_state_value = db.get_value(next_state)
    return reward + gamma * next_state_value


def bellman_value_equation(state, actions, gamma, db):
    """
            compute Bellman value function for the given state and actions
            V(s) = max of a(R(s,a) + gamma * sigma(T(s, a, s') * V(s')))
    """
    rewards = db.get_reward(state, actions)
    next_states = db.get_next_state(state, action)
    next_values = db.get_value(next_states)
    return rewards + gamma * next_values

"""
    value network
"""
class Value:
    def __init__(self):
        return 0

    def
