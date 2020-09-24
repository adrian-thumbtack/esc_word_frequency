import os
from config import *
from word_processing import *

final_freq = total_freq(years,sections,countries)
final_freq = {k:v for k,v in sorted(final_freq.items(), key=lambda item: item[1], reverse=True)}

print_freq(final_freq)