import string

def is_pangram(sentence):
	alphabet = set(string.ascii_lowercase)
	letter_list = set([char.lower() for char in sentence if char.lower() in alphabet])
	return len(letter_list) == len(alphabet)
    
