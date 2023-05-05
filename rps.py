import random
import time

moves = ['Rock', 'Paper', 'Scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.5)


class Player:
    def move(self):
        return 'Rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    their_move = None

    def move(self):
        if self.their_move:
            return self.their_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):  # I checked if this class would work with ChatGPT
    my_move = None

    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
            return self.my_move

        index = moves.index(self.my_move)
        index = (index + 1) % len(moves)
        self.my_move = moves[index]
        return self.my_move

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, or Scissors?").capitalize()
            if move in ["Rock", "Paper", "Scissors"]:
                return move
                break


def beats(one, two):
    return ((one == 'Rock' and two == 'Scissors') or
            (one == 'Scissors' and two == 'Paper') or
            (one == 'Paper' and two == 'Rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause("Shoot!")
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("PLAYER ONE wins the round!")
            print_pause(f"PLAYER ONE score: {self.p1_score}")
            print_pause(f"PLAYER TWO score: {self.p2_score}")
        elif beats(move2, move1):
            self.p2_score += 1
            print("PLAYER TWO wins the round!")
            print_pause(f"PLAYER ONE score: {self.p1_score}")
            print_pause(f"PLAYER TWO score: {self.p2_score}")
        else:
            print("TIE!")
            print_pause(f"PLAYER ONE score: {self.p1_score}")
            print_pause(f"PLAYER TWO score: {self.p2_score}")

    def play_game(self):
        for round in range(1, 4):
            print_pause(f"Round {round}:")
            print_pause("Rock...")
            print_pause("Paper...")
            print_pause("Scissors...")
            self.play_round()
        print_pause("Game over!")
        print_pause("Final score:")
        print_pause(f"PLAYER ONE: {self.p1_score}")
        print_pause(f"PLAYER TWO: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print_pause("PLAYER ONE WINS!!")
        elif self.p2_score > self.p1_score:
            print_pause("PLAYER TWO WINS!!")
        else:
            print_pause("The game is a DRAW!!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
