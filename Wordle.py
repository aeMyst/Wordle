import sys
import random

"""
Class Wordle is an imitation game of the famous Wordle online game through a simple console program.
subject to improvements...

@guesses - places holder for number of guesses user is at
@file - file is the file program will read from for list of words to use
"""
class Wordle:
    #class variables
    currentWord = ""
    numberOfUserGuesses = 0

    #class constructor
    def __init__(self, guesses, file):
        self.guesses = guesses
        self.file = file
    
    #color print reponse to green
    def prGreen(skk): 
        print("\033[92m {}\033[00m" .format(skk), end = "")

    #color print response in yellow
    def prYellow(skk): 
        print("\033[93m {}\033[00m" .format(skk), end = "")

    #color print reponse in grey
    def prLightGray(skk): 
        print("\033[97m {}\033[00m" .format(skk), end = "")

    #read all lines to file and add to list of words
    def readFile(self):
        reading_file = open(self.file, "r")
        for line in reading_file:
            listOfWords.append(line)
        reading_file.close()
    
    #select random word from file
    def selectRandomWord(self):
        Wordle.currentWord = random.choice(listOfWords)

    #remove any empty spaces at end of word
    def removeNewLineFromWord(self):
        Wordle.currentWord = Wordle.currentWord.rstrip()
    
    #start wordle game
    def playWordle(self):
        while (Wordle.numberOfUserGuesses < self.guesses):
            Wordle.numberOfUserGuesses += 1
            currentGuess = input(f"\nGuess Number {Wordle.numberOfUserGuesses}:")
            currentGuess = currentGuess.lower()
            testIndex = 0
            for character in Wordle.currentWord:
                if currentGuess[testIndex] == Wordle.currentWord[testIndex]:
                    Wordle.prGreen(f"{currentGuess[testIndex]}" + "")
                    testIndex += 1
                elif currentGuess[testIndex] in Wordle.currentWord:
                    Wordle.prYellow(f"{currentGuess[testIndex]}" + "")
                    testIndex += 1
                else:
                    Wordle.prLightGray(f"{currentGuess[testIndex]}" + "")
                    testIndex += 1

            if currentGuess == Wordle.currentWord:
                print(f"\nCongrats on getting today's Wordle which was {Wordle.currentWord}! You got it in {Wordle.numberOfUserGuesses} tries.")
                sys.exit("safely exited program")
            elif Wordle.numberOfUserGuesses == self.guesses:
                print(f"\nYou were not able to guess {Wordle.currentWord} in {Wordle.numberOfUserGuesses} tries. Try again!")
                sys.exit("safely exited program")


#main functionality
listOfWords = []

game = Wordle(6, "myWords.txt")
game.readFile()
game.selectRandomWord()
game.removeNewLineFromWord()

#printing current word for wordle
print(f"\n{Wordle.currentWord}") 

#start game
game.playWordle()
