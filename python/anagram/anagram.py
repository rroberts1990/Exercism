def find_anagrams(word, candidates):
	word_sorted = sorted(word.lower())
	return [w for w in candidates if word_sorted == sorted(w.lower()) and not w.lower() == word.lower()]