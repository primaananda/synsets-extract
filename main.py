from output import synsets_manual
from synsets_extraction import alt_gen


def f1_score(synsets_program, synsets_manual):
    relevant_synset = 0
    retrieved_synsets_program = len(synsets_program)
    retrieved_synsets_manual = len(synsets_manual)
    for synset in synsets_program:
        if synset in synsets_manual:
            relevant_synset += 1
    precision = relevant_synset/retrieved_synsets_program
    recall = relevant_synset/retrieved_synsets_manual
    f1score = 2 * precision*recall/(precision+recall)
    return f1score*100

if __name__ == '__main__':
    synsets_final = []

    file1 = open('datatest/1.json')
    synsets_file1 = alt_gen('ahad', file1)
    for x in synsets_file1:
        synsets_final.append(x)
    file2 = open('datatest/5.json')
    synsets_file2 = alt_gen('lebu', file2)
    for x in synsets_file2:
        synsets_final.append(x)

    # file3 = open('datatest/6.json')
    # synsets3 = alt_gen('abu', file3)
    # print(synsets3)

    file1.close()
    file2.close()
    #file3.close()

    akurasi = f1_score(synsets_final, synsets_manual)

    print(akurasi)