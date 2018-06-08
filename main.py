from synsets_extraction import synsets_extraction
from synsets_extraction import alt_gen

if __name__ == '__main__':
    file1 = open('datatest/1.json')
<<<<<<< HEAD
    synsets_file1 = alt_gen('ahad', file1)
    del_redundant = synsets_extraction(synsets_file1)

    ##########
    file2 = open('datatest/datatest.json')
    synsets_file2 = alt_gen()

=======
    file2 = open('datatest/datatest.json')
    synsets = synsets_extraction(file2)
>>>>>>> 01780f6641f2a2d48a6af17314af8e84c83d2089
    file1.close()
    file2.close()
    print()
    print()
    for x in synsets_alt:
        print(x)