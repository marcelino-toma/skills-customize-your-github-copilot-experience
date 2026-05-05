
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build an interactive Hangman game that helps students practice Python strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a list of words and randomly select one as the hidden word for the game.

#### Requirements
Completed program should:

- Define a list of possible words
- Randomly choose one hidden word for each new game
- Keep the hidden word secret from the player

### 🛠️ Guess Processing and Progress Display

#### Description
Allow the player to guess letters, reveal correct letters in the hidden word, and display current progress.

#### Requirements
Completed program should:

- Prompt the player to guess a letter
- Reveal correctly guessed letters in the word using `_` placeholders for unknown letters
- Show the current word progress after each guess
- Prevent repeated guesses from affecting the game state incorrectly

### 🛠️ Win/Lose Logic and Game Feedback

#### Description
Track remaining attempts, detect game win or loss, and display appropriate messages.

#### Requirements
Completed program should:

- Limit the number of incorrect guesses allowed
- Decrease remaining attempts for each wrong guess
- End the game when the word is fully guessed or attempts run out
- Display a win message when the player guesses the word
- Display a lose message and reveal the hidden word if attempts are exhausted
