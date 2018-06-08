from synsets_extraction import synsets_extraction
from synsets_extraction import alt_gen
import json

if __name__ == '__main__':
    synsets_final = []
    file1 = open('datatest/1.json')

    synsets_file = alt_gen('ahad', file1)
    del_redundant = synsets_extraction(synsets_file)
    print()
    print()
    for x in del_redundant:
        synsets_final.append(x)
    ##########
    file2 = open('datatest/5.json')
    synsets_fil = alt_gen('perdamaian', file2)
    del_redundan = synsets_extraction(synsets_fil)
    print()
    print()
    for x in del_redundan:
        synsets_final.append(x)

    print(synsets_final)

    file1.close()
    file2.close()
