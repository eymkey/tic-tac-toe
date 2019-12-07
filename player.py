import random


class RandomPlayer():
    def __init__(self):
        pass

    def move(self, state):
        moves = self.get_available_moves(state)
        move = random.choice(moves)
        return move

    def get_available_moves(self, state):
        list_of_moves = []

        for index_y, y in enumerate(state):
            for index_x, x in enumerate(y):
                if state[index_y, index_x] == 0:
                    list_of_moves.append((index_x, index_y))

        return list_of_moves
