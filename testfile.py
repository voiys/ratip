from langdetect import *



en_file = open('engleski', 'w+')
hr_file = open('hrvatski', 'w+')
other_file = open('ostali', 'w+')
try:
    with open('korpus.txt') as korpus:
    	for line in korpus.readlines():
    		line = line.split('|')[6]
    		if line not in ('-'):
    			if detect(line) == 'en':
    				en_file.write(line)
    			elif detect(line) == 'hr':
    				hr_file.write(line)
    			else:
    				other_file.write(line)
except:
	pass

en_file.close()
hr_file.close()
other_file.close()
