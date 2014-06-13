ZJNanalogy
==========

Program służy do lematyzacji tekstów. W tym celu zaimplementowano Analogy Algorithm, zgodnie z pseudokodem zawartym w pracy: <br><i>
Filip Graliński. Morphological analysis by analogy. In Stanisław Puppel and Grażyna Demenko, editors, Prosody 2000. Speech recognition and synthesis, pages 59-67, Poznań, 2001. Wydział Neofilologii Uniwersytetu im. Adama Mickiewicza. </i>
<br>

Użycie
------

Uruchomienie programu na pojedynczym słowie: 
<code> python analogyAlgorithm.py -w word </code>
<br> Zwróci wynik w konsoli.
<br>


Opcje
------

    -o, --output  -  określa plik wyjściowy 
    -i, --input   -  określa plik wejściowy  
    -d, --dictionary - określa ścieżkę do własnego słownika 
    -w, --word   - określa pojedyncze słowo na wejściu 
    -l, --limit  - podaje dokładność działąnia algorytmu 
    -f, --format - określa format wyjścia:
        0 - pierwszy zlematyzowany wyraz 
        1 - wszystkie zlematyzowany wyrazy, oddzielone znakiem |
        2 - wszystkie zlematyzowane wyrazy w formie: wyraz odmieniony wyraz podstawowy |
        3 - wszystkie zlematyzowane wyrazy w formie: wyraz odmieniony wyraz podstawowy forma odmiany |
    -c, --degree - określa typ rozpoznania algorytmu:
        0 - Analizowany wyraz zawarty jest w słowniku
        1 - Rozpoznanie zostało dokonane na zasadzie analogii
        2 - Rozpoznanie nie wymaga istnienia formy podstawowej w słowniku.
        3 - Wnioskuje analogię na podstawie analogii do wyrazu uzyskanego w rozpoznaniu stopnia 1
