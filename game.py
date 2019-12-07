import numpy as np
from player import RandomPlayer
from ui import UI
import time
import random

class Game():
    def __init__(self, player1, player2, rounds, ui=None, log=False):
        self.rounds = rounds
        self.statistics = np.zeros(3, dtype=np.int64)
        self.ui = ui
        self.log = log

        self.player1 = player1
        self.player2 = player2
        self.state = np.zeros((3,3), dtype=np.int32)
        self.turn = 1

    def reset(self):
        self.state = np.zeros((3,3), dtype=np.int32)
        self.turn = random.randrange(1,3)

    def move(self):
        if self.turn == 1:
            while True:
                players_move = self.player1.move(self.state)
                if self.move_is_valid(players_move):
                    x, y = players_move
                    self.state[y, x] = self.turn
                    self.turn = 2
                    break

        elif self.turn == 2:
            while True:
                players_move = self.player2.move(self.state)
                if self.move_is_valid(players_move):
                    x, y = players_move
                    self.state[y, x] = self.turn
                    self.turn = 1
                    break

    def move_is_valid(self, players_move):
        x, y = players_move
        if type(x) == int and type(y) == int:
            if 2 >= x >= 0 and 2 >= y >= 0:
                if self.state[y, x] == 0:
                    return True
        return False

    def is_game_running(self):
        winning_situations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0,3,6), (1,4,7), (2,5,8), (0, 4, 8), (2, 4, 6)]
        current_state = self.state.flatten()

        for winning_situation in winning_situations:
            pos1, pos2, pos3 = winning_situation
            if current_state[pos1] == current_state[pos2] == current_state[pos3] and current_state[pos1] != 0:
                return False, current_state[pos1]

        # check for a tie
        empty_fields = np.sum([1 if position == 0 else 0 for position in current_state])
        if empty_fields == 0:
            return False, 0

        return True, None

    def start(self):
        for _ in range(1,self.rounds+1):
            self.reset()

            running = True
            winner = 0

            while running:
                self.move()
                if self.ui is not None:
                    self.ui.render(self)
                    time.sleep(0.05)
                running, winner = self.is_game_running()

            if self.log: print(f"Player {winner} Wins")
            self.statistics[winner] += 1

        return self.statistics


ui = UI()
randomPlayer1 = RandomPlayer()
randomPlayer2 = RandomPlayer()
game1 = Game(randomPlayer1, randomPlayer2, 20, ui=ui, log=True)
statistics = game1.start()
print(statistics)