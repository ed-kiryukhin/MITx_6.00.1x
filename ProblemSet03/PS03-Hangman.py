# Hangman game

import random
import string
import os

file_path = os.path.dirname(os.path.abspath(__file__))

WORDLIST_FILENAME = file_path + "\words.txt"

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

def chooseWord(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	False otherwise
	'''
	count = 0
	for letter in secretWord:
		if letter in lettersGuessed:
			count += 1
	if len(secretWord) == count:
		return True
	else:
		return False

def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	what letters in secretWord have been guessed so far.
	'''
	guessed = ''
	for letter in secretWord:
		if letter in lettersGuessed:
			guessed += '%s ' % letter
		else:
			guessed += '_ '
	return guessed

def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	yet been guessed.
	'''
	alfabet = string.ascii_lowercase
	notUsed = ''
	for letter in alfabet:
		if letter not in lettersGuessed:
			notUsed += letter
	return notUsed

def hangman(secretWord):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
	letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess 
	about whether their guess appears in the computers word.

	* After each round, you should also display to the user the 
	partially guessed word so far, as well as letters that the 
	user has not yet guessed.

	Follows the other limitations detailed in the problem write-up.
	'''
	print "Welcome to game, Hangman!"
	print "I am thinking of a word that is %d letters long." % len(secretWord)
	print "-------------"
	lettersGuessed = []
	mistakesMade = 0
	while True:
		if not isWordGuessed(secretWord, lettersGuessed):
			if mistakesMade < 8:
				print "You have %d guesses left." % (8 - mistakesMade)
				print "Available letters: " + getAvailableLetters(lettersGuessed)
				guess = raw_input('Please guess a letter: ')
				guess = guess.lower()
				if guess not in lettersGuessed:
					lettersGuessed.append(guess)
					if guess in secretWord:
						print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
					else:
						mistakesMade += 1
						print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
				else:
					print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
				print "-------------"
			else:
				print "Sorry, you ran out of guesses. The word was %s." % secretWord
				break
		else:
			print "Congratulations, you won!"
			break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)