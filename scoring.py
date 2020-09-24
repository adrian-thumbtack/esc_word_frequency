def score_section(freq_list, word_list, points):
	'''A function to find the score of a specific section or sections of songs

	Parameters: freq_list - the dictionary of frequencies of words in that section
				word_list - the list of words to score
				points - the amount of points per occurrence

	Returns: total score as an integer 
	'''
	int total = 0
	for word, freq in freq_list.items():
		if word in word_list:
			total += freq*points

	return total