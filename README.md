# simple_games

# Rock Paper Scissors

This is a simple implementation of the Rock Paper Scissors game in Python. The game allows you to play against various types of players, including a human player and AI players with different strategies.

## How to Play
1. Run the script in a Python environment.
2. The game will start, and you will be prompted to enter your move (Rock, Paper, or Scissors).
3. The AI player will generate its move based on its strategy.
4. The moves will be compared, and the winner of the round will be announced.
5. The game will continue for three rounds.
6. After the game is over, the final scores will be displayed, and the winner of the game will be announced.

## Players
The game supports the following types of players:

### Human Player
- The human player is controlled by the user.
- When prompted, enter your move by typing "Rock", "Paper", or "Scissors".

### AI Players
1. RandomPlayer:
   - This player selects its move randomly.
   
2. ReflectPlayer:
   - This player starts by making a random move.
   - It then mirrors the opponent's previous move for subsequent rounds.

3. CyclePlayer:
   - This player starts by making a random move.
   - It cycles through the moves in a fixed order for subsequent rounds.

4. AIPlayer:
   - This player uses a Markov Chain model to predict the opponent's move based on previous moves.
   - It generates the next move based on the predicted move.
   - The player tries to choose a move that beats the predicted move.
   - The transitions and predictions are updated after each round.

## How the Game Works
- The game consists of three rounds.
- Each round, both players select their moves.
- The moves are compared to determine the winner of the round.
- Scores are updated accordingly.
- After three rounds, the final scores are displayed, and the winner of the game is announced.

## Prerequisites
- Python 3.x

## How to Run the Code
1. Copy the code into a Python environment or save it in a .py file.
2. Run the script.
3. Play the game against different types of players and enjoy!

Note: You may need to adjust the indentation of the code when copying it to ensure proper execution.


# Adventure Game

This is a simple text-based adventure game implemented in Python. The game puts you in an open field where you encounter different scenarios and make choices to progress through the game.

## How to Play
1. Run the script in a Python environment.
2. Read the story prompts and make choices by entering the corresponding numbers or options.
3. Progress through the game by exploring the field, encountering villains, and finding items.
4. Face off against the final villain and either defeat them or be defeated.
5. After the game ends, you have the option to play again.

## Story
You find yourself standing in an open field filled with grass and yellow wildflowers. Rumor has it that a villain is somewhere around here and has been terrorizing the nearby village. In front of you is a house, and to your right is a dark cave. In your hand, you hold your trusty (but not very effective) dagger.

## Gameplay
### Field
- You have two options:
  1. Knock on the door: The villain might come out of the house, leading to a confrontation.
  2. Peer into the cave: You might find a weapon inside, enhancing your chances in a fight.

### House
- If you choose to knock on the door:
  - The villain steps out and attacks you.
  - You have two options:
    1. Fight: Use your weapon (if you found one) to try to defeat the villain.
    2. Run away: Escape from the house and return to the field.

### Cave
- If you choose to peer into the cave:
  - If you haven't found a weapon before, you discover one inside and equip it.
  - After finding the weapon or if you've already found it, you return to the field.

### Fight
- If you choose to fight:
  - If you have a weapon, you use it against the villain.
    - If the villain sees your legendary weapon, they run away, and you win the game.
    - If you don't have a weapon or the villain is too strong, you are defeated, and the game ends.

### Run Away
- If you choose to run away:
  - You escape from the house and return to the field.

### Play Again
- After the game ends, you have the option to play again.
- If you choose to play again, the game restarts with a new villain and weapon.

## Prerequisites
- Python 3.x

## How to Run the Code
1. Copy the code into a Python environment or save it in a .py file.
2. Run the script.
3. Follow the prompts, make choices, and enjoy the adventure!

Note: You may need to adjust the indentation of the code when copying it to ensure proper execution.

# Racing Turtles

This is a simple turtle race game implemented using the `turtle` module in Python. The game simulates a race between two turtles, Matt and Catalina, and determines the winner based on their progress along the race track.

## How to Play
1. Run the script in a Python environment.
2. Watch as the turtles, represented by blue and red shapes, start moving along the race track.
3. The race continues until one of the turtles reaches or crosses the finish line at the right end of the track.
4. The turtle that reaches the finish line first is declared the winner.
5. The winner's name is displayed in the console.

## Race Track
The race track consists of a start line on the left and a finish line on the right. The turtles start at the same position on the start line and move forward at random speeds to simulate the race. The turtle that reaches the finish line first is the winner.

## Turtles
- Matt: Represented by a blue turtle.
- Catalina: Represented by a red turtle.

## Prerequisites
- Python 3.x
- turtle module (usually included in the standard library)

## How to Run the Code
1. Copy the code into a Python environment or save it in a .py file.
2. Run the script.
3. Observe the turtles' movement on the race track.
4. Check the console output to see the winner of the race.

Note: You may need to adjust the indentation of the code when copying it to ensure proper execution.

## License
This project is licensed under the [MIT License](LICENSE).

