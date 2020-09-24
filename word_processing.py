import os
from config import *
from string import ascii_letters
from nltk.stem import PorterStemmer

current_dir = os.path.dirname(__file__)

def get_path(year,section,country):
	'''
	Get the path to a file specified by a year, lyric section (chorus and unchorus only),
	and country

	Parameters:
	year - the year of the ESC
	section - which section of lyrics is needed (chorus, unchorus)
	country - the country whose song is needed

	Returns:
	path to the appropriate text file
	'''
	rel_path = 'lyrics_data/esc%d/%s/%s.txt' % (year,section,country)
	return os.path.join(current_dir,rel_path)

def clean_word(word):
	'''
	Remove excess punctuation from a word

	Parameters:
	word - string to be cleaned

	Returns:
	the string, without and starting or ending punctuation
	'''

	while word[0] not in ascii_letters: word = word[1:]
	while word[-1] not in ascii_letters: word = word[:-1]
	return word.lower()

def clean_words(wordlist):
	'''
	Clean up a list of words, removing excess punctuation and empty strings

	Paramaters:
	wordlist - list of strings to be cleaned

	Returns:
	the list of cleaned words
	'''
	ret = []
	for word in wordlist:
		if word == '': continue
		cleaned = clean_word(word)
		if cleaned != '': ret.append(cleaned)
	return ret

def words(year,section,country):
	'''
	Get words for the appropriate combination of year, section, and country

	Parameters:
	year - the year of the ESC
	section - which section of lyrics is needed (title, chorus, unchorus)
	country - the country whose song is needed

	Returns:
	the words in the corresponding song section, as a list
	'''
	if section == 'titles': pass #file format TBD
	else:
		ret = []
		with open(get_path(year,section,country),'r', encoding='utf-8') as f:
			for line in f:
				ret += line.strip().split()
		return clean_words(ret)

def list_to_freq(wordlist):
	'''
	Transforms a list of words to a frequency table

	Parameters:
	wordlist - list of strings

	Returns:
	dictionary, where keys are words and values are frequencies within the list
	'''
	ret = dict()
	for word in wordlist:
		try: ret[word] += 1
		except: ret[word] = 1
	return ret

def word_freq(year,section,country):
	'''
	Get word frequency list for the appropriate combination of year, section, and country

	Parameters:
	year - the year of the ESC
	section - which section of lyrics is needed (title, chorus, unchorus)
	country - the country whose song is needed

	Returns:
	the word frequency list as a dictionary
	'''
	wordlist = words(year, section, country)
	return list_to_freq(stem_words(wordlist))

def total_freq(year_list,section_list,country_list):
	'''
	Get word frequency list for every combination of year, section, and country in total

	Parameters:
	year_list - list of years
	section_list - list of song sections
	country_list - list of countries

	Returns:
	the word frequency list as a dictionary
	'''
	ret = dict()
	for year in year_list:
		for section in section_list:
			for country in country_list:

				try:
					d = word_freq(year,section,country)
					for key in d:
						try: ret[key] += d[key]
						except: ret[key] = d[key]
				except: continue

	return ret

def print_freq(freq_list, num=0):
	'''
	Print word frequency lists in the format "word: number"

	Parameters:
	freq_list - the frequency list to be printed
	'''
	if num == 0:
		num = len(freq_list)

	i = 0
	for word, freq in freq_list.items():
		print('%s: %d' % (word, freq))
		i += 1
		if (i >= num): break

def print_to_file(freq_list, file_name='frequencies.txt'):
	'''
	Write the frequencies to a file

	Parameters:
	freq_list - the frequency list to be written to file
	file_name - file name to write the frequency list

	Returns: nothing, file called file_name overwritten or created for method
	'''
	f = open(os.path.join(current_dir,file_name), 'w', encoding='utf-8')
	for word, freq in freq_list.items():
		f.write('%s: %d\n' % (word, freq))

	f.close()


def stem_words(wordlist):
	'''Get the stems of all words in the given word list

	Parameters:
	wordlist - list of words to stem
	option - 0 for porter stem, 1 for lancaster stem, no stem by default

	Returns:
	the list of stems as a list
	'''
	ret = []
	porter = PorterStemmer()
	for word in wordlist:
		ret.append(porter.stem(word))

	return ret


def sort_frequency(freq_list, reverse=True, alpha=False):
	'''Sort frequency lists by alphabet or value

	Parameters:
	freq_list - dictionary to be sorted
	reverse - True sorts the list descending, False ascending
	alpha - True sorts by alphabetical order instead of numerical, False is numerical

	Returns:
	sorted dictionary of frequencies
	'''
	if alpha:
		return {k:v for k,v in sorted(freq_list.items(), key=lambda item: item[0], reverse=reverse)}
	else:
		return {k:v for k,v in sorted(freq_list.items(), key=lambda item: item[1], reverse=reverse)}