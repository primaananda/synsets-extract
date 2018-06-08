from synsets_extraction import synsets_extraction
from synsets_extraction import alt_gen
import json

if __name__ == '__main__':
    file1 = open('datatest/1.json')
    thesa = json.load(file1)
    synsets_file = alt_gen('ahad', thesa)
    del_redundant = synsets_extraction(synsets_file)
    print()
    print()
    for x in del_redundant:
        print(x)
    ##########
    word = ['ahad', 'setanggi', 'aborsi', 'pekan', 'abah']
    new_synsets = []
    with open(open('datatest/datatest.json')) as fl:
        thesa = json.load(fl)
        for w in word:
            new_synsets = alt_gen(w, thesa)

    file1.close()
    file2.close()
