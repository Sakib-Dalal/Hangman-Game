# Hangman Game

Welcome to the Hangman Game! This Python script lets you play the classic word-guessing game. Try to guess the hidden word before you run out of lives.

## How to Play

1. Run the `main.py` script.
2. Enter your guesses to uncover the hidden word.
3. You have 6 lives to complete the word.
4. If you guess the word or run out of lives, the game will end.

Enjoy the challenge of Hangman!

## Features

- Interactive interface with ASCII art for aesthetics.
- A variety of words to guess from the provided word list.
- Fun and challenging gameplay.

## Word List

The words used in the game are stored in `hangman_words.py` and include a diverse set of options to keep the game interesting.

## Hangman Stages

The different stages of the hangman are represented with ASCII art. As you make incorrect guesses, the hangman is gradually revealed.

```python
# hangman_art.py
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
```

## Hangman Logo

A stylish ASCII art logo adds a visually appealing touch to the Hangman Game.

```python
# hangman_art.py
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''
```

## How to Run

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Sakib-Dalal/Hangman-Game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Hangman-Game
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

*Have fun playing Hangman!*

---

*This project is developed by Sakib Dalal. For more details, please visit the [GitHub repository](git@github.com:Sakib-Dalal/Hangman-Game.git).*
