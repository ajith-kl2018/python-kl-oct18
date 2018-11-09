import re

hand = open('data/mbox-short.txt')

for line in hand :
    line = line.rstrip()
    #if line.find('From:') >= 0 :
    #    print(line)
    #if re.search('From:',line) :
    #if re.search('^From:', line):
    #if re.search('^X.*:', line):
    if re.search('^X-\S+:', line):
        print(line)

    #print(re.findall('[0-9]+',line))




