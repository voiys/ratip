from langdetect import *


en_file = open('engleski.txt', 'w+')
hr_file = open('hrvatski.txt', 'w+')
other_file = open('ostali.txt', 'w+')

try:
    with open('korpus.txt') as korpus:
        for line in korpus.readlines():
            line = line.split('|')[6]
            if line not in ('-'):
                if detect(line) == 'en':
                    en_file.write(f"{line}\n")
                elif detect(line) == 'hr':
                    hr_file.write(f"{line}\n")
                else:
                    other_file.write(f"{line}\n")
except:
    pass

en_file.close()
hr_file.close()
other_file.close()
