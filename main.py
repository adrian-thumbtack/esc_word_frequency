import os
from config import *
from word_processing import *

final_freq = total_freq(years,sections,countries)
#final_freq = sort_frequency(final_freq, reverse=False, alpha=True)

print_to_file(sort_frequency(final_freq), 'sorted_frequencies.txt')
print_to_file(sort_frequency(final_freq, reverse=False, alpha=True), 'alphabetical_frequencies.txt')