# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser


#czyta leksykon z pliku
def read_lexicon(file_name):
    d=[]
    with open(file_name) as FileObj:
        for line in FileObj:
            fields = line.split('\t')
            d.append(fields)
    return d
    
#sprawdza czy slowo x i słowo w maja wspolna koncowke o dlugosci i  
def has_common_ending(x, w, i):
    if len(x)>=i and len(w)>=i and x[-i:]==w[-i:]:
        return True
    else:
        return False

#tworzy zbiór słów ze słownika W, 
#które mają wspólną końcówkę długości i z podanym wyrazem w 
def make_wset(w, W, i):
    wset = [x for x in W if has_common_ending(w,x[0],i)]
    #print "wset=%s"%wset
    return wset

def is_in_lexicon(w,W):
    for x in W:
        if x[0] == w:
            return x
    return False

def addBaseWord(w,D):
    if w in D:
        0
    else:
        return D.append(w)


#szuka analogii do słowa 'w', według leksykonu W


def analogy(w,W,limit):
    result = []
    r = is_in_lexicon(w,W)
    if r:
        print "ROZPOZNANIE STOPNIA 0: Slowo %s jest w slowniku"%w
        addBaseWord(r,result)
    else:
        for i in range(len(w),limit-1,-1):
            wset = make_wset(w, W, i)
            for el in wset:
                W.remove(el)
            for x in wset:
                #print "x0=%s x1=%s" % (x[0],x[1])
                if x[0] != x[1]:
                    z = x[1]
                    stem_length = len(x[0]) - i
                    if stem_length >= len(w) - i:
                        #print "\t slowoW=%s, rozwazane x=%s, bazowe z=%s" %(w,x[0],z)
                        #print "\t i=%d, stem_lenght=%d"%(i,stem_length)
                        base_word = w[:len(w)-i] + z[stem_length:]
                        #return 
                        #if [base_word, base_word, x[2], x[3]] in d:
                        #    print "loool"
                        #    print "ROZPOZNANIE STOPNIA 1: Base_word %s jest w slowniku"%base_word
                        #else:
                        #    print "ROZPOZNANIE STOPNIA *: słowa %s nie ma w słowniku"%base_word
                        addBaseWord([w, base_word, x[2], x[3]], result)
                        #print [base_word, x[2]]
    for haslo in result:
        print haslo
                        
def analogy2(w,W,limit):
    for i in range(len(w),limit-1,-1):
        wset = make_wset(w, W, i)
        for x in wset:
            #print "x0=%s x1=%s" % (x[0],x[1])
            if x[0] != x[1]:
                z = x[1]
                stem_length = len(x[0]) - i
                if stem_length >= len(w) - i:
                    #print "\t slowoW=%s, rozwazane x=%s, bazowe z=%s" %(w,x[0],z)
                    #print "\t i=%d, stem_lenght=%d"%(i,stem_length)
                    base_word = w[:len(w)-i] + z[stem_length:]
                    #return 
                    #print "Base_word = %s"%base_word
                    return base_word

def rozpoznanie_2_stopnia(w,W,l):
    print W
    word1 = analogy2('mapkami',W,l)
    print analogy2('mapka', W, l)
    print analogy2(analogy2('mapkami',W,l), W, l)
    print analogy2(word1, W, l)

#główna metoda                        
def main():
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="outputfile")
    parser.add_option("-i", "--input", dest="inputfile")
    parser.add_option("-l", "--lexicon", dest="lexicon")
    parser.add_option("-w", dest="word")
    (options, args) = parser.parse_args()


    LEX='lexicon'
       
    if options.word:
        word = options.word
    elif options.inputfile:
        inFile = options.inputfile
    if options.lexicon:
        LEX=options.lexicon
    if options.outputfile:
        out=options.outputfile
        
    d = read_lexicon(LEX) 
    analogy(word,d,3)
    #rozpoznanie_2_stopnia(word,d,limit)

main()  



