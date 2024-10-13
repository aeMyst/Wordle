# Wordle

This is a console-based imitation of the popular online game Wordle. The game involves guessing a randomly selected word within a limited number of attempts. Each guess provides feedback by coloring the letters according to how accurate they are:

Green for correct letters in the correct position.
Yellow for correct letters but in the wrong position.
Light Gray for incorrect letters.
The program reads a list of words from a specified file and selects one randomly for the player to guess. The user is given six attempts to guess the word correctly. After each guess, the game provides feedback using colored output to help the player zero in on the correct word.

How to Play
The program randomly selects a word from a list of words stored in a text file (myWords.txt by default).
You will be prompted to enter a guess for the word.
After each guess, the program will provide feedback using colored output:
Green letters indicate the letter is in the correct position.
Yellow letters indicate the letter exists in the word but is in the wrong position.
Light Gray letters indicate the letter is not in the word at all.
You have 6 attempts to guess the correct word.
The game ends when:
You guess the word correctly, and the game congratulates you.
You use up all 6 attempts without guessing correctly, and the game reveals the word.
Features
Random word selection from a file.
Simple and intuitive feedback system using color-coded letters.
Customizable number of attempts.
Reads from a file to allow the list of words to be easily modified or expanded.
Requirements
Python 3.x
A text file containing a list of words (one word per line).
Running the Game
Clone the repository or download the script.
Ensure you have a text file (myWords.txt by default) with a list of words for the game to choose from or download the txt file available in repository. Each word should be on a new line.
Run the program using Python:
bash
Copy code
python wordle.py
Follow the on-screen instructions to play the game.

Example File (myWords.txt)

apple
table
chair
grape
mango

In the example above, one of these words will be selected randomly for the player to guess.

Notes for Future Improvements
Add more robust input validation.
Implement a scoring system.
Create a user-friendly graphical interface.
Allow the player to choose difficulty levels based on word length.
