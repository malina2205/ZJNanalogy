# -*- coding: utf-8 -*-

import sys
import codecs
from optparse import OptionParser
import os

#czyta leksykon z pliku
def read_lexicon(file_name):
    d=[]
    with open(file_name) as FileObj:
        for line in FileObj:
            fields = line.decode('utf-8').split('\t')
            d.append(fields)        
    return d
    
#formatuje wyjscie
def print_result(tab, out, opt):
    s = ""
    #tylko jedno wyjscie
    if opt == 0 and len(tab)>0:
        s = s + tab[1][1] + " | " 
    else:   
        for el in tab:
            # same formy podstawowe w jednej linii
            if opt == 1:
                s = s + el[1] + " | " 
            # wyraz odmieniony  wyraz podstawowy  |
            elif opt == 2:
                s = s + el[0] + " "+ el[1] + " | "   
            # wyraz odmieniony | wyraz podstawowy | forma odmiany
            elif opt == 3:
                s = s + el[0] + " "+ el[1] + " " + el[2] + " | "  
    return s
           
#sprawdza czy slowo x i słowo w maja wspolna koncowke o dlugosci i  
def has_common_ending(x, w, i):
    #print type(x[-i:])
    #print type(w[-i:])
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

#jeśli słowo w znajduje się w leksykonie zwraca jego opis
def is_in_lexicon(w,W):
    for x in W:        
        if x[0] == w:
            return x
    return False

#dodaje wpis w do tablicy D, jeśli jeszcze go tam nie ma
def addBaseWord(w,D):
    if w in D:
        return False
    else:
        D.append(w)
        return True


#szuka analogii do słowa 'w', według leksykonu W
def analogy(w,W,limit,degree):
    result = []
    base_w = []
    r = is_in_lexicon(w,W)
    if r:
        print "ROZPOZNANIE STOPNIA 0: Slowo %s jest w slowniku"%w
        addBaseWord(r,result)
    if degree<=0:
        return result
    else:
        for i in range(len(w),limit-1,-1):
            wset = make_wset(w, W, i)

            for x in wset:
                #print "x0=%s x1=%s" % (x[0],x[1])
                if x[0] != x[1]:
                    z = x[1]
                    stem_length = len(x[0]) - i
                    if stem_length >= len(w) - i:
                        base_word = w[:len(w)-i] + z[stem_length:]
                        #return 
                        if (degree<=1 and len([x for x in W if x[1]==base_word])>0) or degree>1:
                            #print "ROZPOZNANIE STOPNIA 1: Base_word %s jest w slowniku"%base_word                                           
                            #print "ROZPOZNANIE STOPNIA *: słowa %s nie ma w słowniku"%base_word
                            if addBaseWord(base_word, base_w):
                                addBaseWord([w, base_word, x[2], x[3]], result)
    if len(result) == 0:
        result.append([w, "-", "-", "-"])
    return result

def analogy_file(in_file,d,limit,degree):
    ret = []
    try:
        fh = open(in_file,"r")
        words = fh.read().split()
        for word in words:
            ret.append(analogy(word,d,3,degree))       
    finally:
        fh.close()
    pass
    return ret
                        
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
    word1 = analogy2(w,W,l)
    print analogy2(word1, W, l)
    print analogy2(word1, W, l)


#główna metoda                        
def main():
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="outputfile")
    parser.add_option("-i", "--input", dest="inputfile")
    parser.add_option("-d", "--dictionary", dest="lexicon")
    parser.add_option("-w", dest="word")
    parser.add_option("-l", "--limit", dest="limit")
    parser.add_option("-f", "--format", dest="out_format")
    parser.add_option("-c", "--degree", dest="degree")
    (options, args) = parser.parse_args()

    LEX='lexicon'
    limit = 3
    out = False
    out_format = 0
    degree = 3
    s = ''
    
    if options.lexicon:
        LEX=options.lexicon
    if options.outputfile:
        out=options.outputfile
    if options.limit:
        limit=options.limit
    if options.out_format:
        out_format = options.out_format       
    d = read_lexicon(LEX) 
    
    if options.degree:
        degree = int(options.degree)

    if options.word:
        word = options.word
        tab = analogy(word,d,3, degree)
        s = print_result(tab, out, int(out_format))
        
        #rozpoznanie_2_stopnia(word,d,limit)
    elif options.inputfile:
        inFile = options.inputfile
        tab = analogy_file(inFile,d,3, degree)
        for el in tab:
            s = s + print_result(el, out, int(out_format)) + "\n"
           
    else:
        print "Nie podano danych wejściowych"
        print " opcja -w podanie pojedynczego słowa"
        print " opcja -i podanie pliku wejściowego"
        return 
                   
    
    if out:
        try:
            f = open(out, "w")
            f.write(s)
        finally:
            f.close()
        pass
    else:
        print s
    #rozpoznanie_2_stopnia(word,d,limit)
    print "............."
    

main()  



