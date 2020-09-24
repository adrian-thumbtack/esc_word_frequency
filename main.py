import os

current_dir = os.path.dirname(__file__)
path = 'lyrics_data/esc2018/chorus/australia.txt'
filepath = os.path.join(current_dir,path)

with open(filepath,'r') as f:
	for line in f: print(line)