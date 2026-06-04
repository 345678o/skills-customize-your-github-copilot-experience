
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, and user input handling. Players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Implement the core game loop

#### Description
Implement the main game loop that displays the word progress, accepts letter guesses, updates game state, and ends on win or loss.

#### Requirements
Completed program should:

- Randomly select a secret word from the provided `words` list (see `starter-code.py`).
- Display current progress using underscores for unguessed letters (for example: `_ p p _ e`).
- Accept single-letter guesses (case-insensitive) and ignore repeated guesses.
- Track and display remaining incorrect attempts and end the game when attempts reach zero.
- Print a clear win or lose message with the correct word.

### 🛠️ Input validation & polish

#### Description
Add input validation and user-facing improvements to make the game robust and friendly.

#### Requirements
Completed program should:

- Validate that input is a single alphabetic character; prompt again for invalid input.
- Show a list of letters already guessed and the number of attempts remaining.
- (Optional) Offer a replay option or difficulty levels that adjust allowed attempts.

## Starter code

Use `starter-code.py` in this folder as a starting point. It includes a word list and scaffolding for the game loop.

## Tests (optional)

If you add automated tests, describe how to run them here (for example, `python -m pytest`).

## Hints

- Use a set to track guessed letters and to check for repeated guesses efficiently.
- Keep the UI text clear and concise since this is a command-line exercise.

