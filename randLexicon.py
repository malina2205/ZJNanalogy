import linecache
import random
linenum = 6578142
myFile = open('lexicon','w')
for i in range(1,5000):
    rand = random.randint(1,linenum)
    for j in range (rand-7, rand+7): 
        myFile.write(linecache.getline('PoliMorf-0.6.7.tab', j))
        
myFile.close()
