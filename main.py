from synsets_extraction import delete_redundant
from synsets_extraction import alt_gen
import json

if __name__ == '__main__':
    synsets_final = []
    '''
    file1 = open('datatest/1.json')

    synsets_file = alt_gen('ahad', file1)
    del_redundant = delete_redundant(synsets_file)
    for x in del_redundant:
        synsets_final.append(x)
    ##########
    file2 = open('datatest/5.json')
    synsets_fil = alt_gen('perdamaian', file2)
    del_redundan = delete_redundant(synsets_fil)
    for x in del_redundan:
        synsets_final.append(x)
    #print(synsets_final)
    '''
    ##########'''
    file3 = open('datatest/sample2.json')
    synsets3 = alt_gen('a', file3)
    print(synsets3)

    #file1.close()
    #file2.close()
    file3.close()
