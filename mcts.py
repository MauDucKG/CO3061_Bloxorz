import time
from math import *


class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, map=[], xo_objects_states={}, is_splitted=False, parent=None):
        if not ((data[0] < data[2]) or ((data[0] == data[2]) and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.map = map_copy(map)
        self.xo_objects_states = dict(xo_objects_states)
        self.is_splitted = is_splitted
        self.wins = 0
        self.visits = 0
        self.children = []
        self.parent = parent

    def UCTSelectChild(self):
        s = sorted(self.childNodes, key=lambda c: c.wins /
                   c.visits + sqrt(2*log(self.visits)/c.visits))[-1]
        return s

    def expand(self):
        actions = self.state.get_actions()
        for action in actions:
            new_state = self.state.execute_action(action)
            child = Node(new_state, parent=self)
            self.children.append(child)

    def simulate(self):
        current_state = self.state
        while not current_state.is_terminal():
            action = random.choice(current_state.get_actions())
            current_state = current_state.execute_action(action)
        return current_state.get_winner()

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)


def mcts(state):
    current_state = Node

    start = time.time()
    while len(state.states) != 0:
        # if time.time() - start > 15:
        #     break
        current_state = state.states.pop(0)
        state.set_player_position(current_state)
        if state.check_goal():
            break
        state.add_valid_state(current_state, -120)
    pointer = current_state
    path = []
    # Backtracking all the previous moves to reach this goal state
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node
    # And print them out
    # for p in path:
    #     print(p.data)
    return path
