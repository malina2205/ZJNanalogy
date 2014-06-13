import linecache
import random
linenum = 6578142
myFile = open('lexicon','w')
for i in range(1,10000):
    rand = random.randint(1,linenum)
    for j in range (rand-3, rand+3): 
        myFile.write(linecache.getline('PoliMorf-0.6.7.tab', j))
        
myFile.close()
