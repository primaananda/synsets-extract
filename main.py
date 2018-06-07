from synsets_extraction import synsets_extraction

if __name__ == '__main__':
    #open file
    file1 = open('datatest/1.json')
    file2 = open('datatest/1.json')
    synsets = synsets_extraction(file1)
    file1.close()
    file2.close()
    print()
    print()
    for x in synsets:
        print(x)
