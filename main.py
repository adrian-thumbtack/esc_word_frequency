import os
from config import *
from string import ascii_letters

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
	if section == 'title': pass #file format TBD
	else:
		ret = []
		with open(get_path(year,section,country),'r') as f:
			for line in f:
				ret += line.strip().split(' ')
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
	return list_to_freq(words(year,section,country))

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

print(total_freq(years,sections,countries))