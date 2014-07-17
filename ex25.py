# By guoshu 
# 2014/7/13 19:19

def break_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poppint it"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first sentence and returns the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and the last one """
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
