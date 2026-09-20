# Hangman Game

A simple text-based Hangman game built in Python, made as part of the CodeAlpha internship.

## About

The player has to guess the hidden word one letter at a time. Each wrong guess uses up one of 6 attempts. The game ends when the word is fully guessed or the attempts run out.

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python hangman.py
```

## How to Play

- You'll see blanks representing each letter of the word.
- Type one letter at a time and press Enter.
- Correct letters get filled into the word.
- Wrong letters count against your 6 attempts.
- Guess the full word before running out of attempts to win.

## Concepts Used

- `random` module for word selection
- `while` loop for the main game flow
- `if-else` statements for guess checking
- Strings and lists for tracking progress

## Project Structure

```
hangman-game/
├── hangman.py
└── README.md
```
