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

    # file1 = open('datatest/6.json')
    # synsets_file1 = alt_gen('ahad', file1)
    # for x in synsets_file1:
    #     synsets_final.append(x)
    # file2 = open('datatest/5.json')
    # synsets_file2 = alt_gen('lebu', file2)
    # for x in synsets_file2:
    #     synsets_final.append(x)

    file1 = open('datatest/data_test/1.json')
    synsets1 = alt_gen('ahad', file1)
    for x in synsets1:
        synsets_final.append(x)

    file2 = open('datatest/data_test/2.json')
    synsets2 = alt_gen('setanggi', file2)
    for x in synsets2:
        synsets_final.append(x)

    file3 = open('datatest/data_test/3.json')
    synsets3 = alt_gen('aborsi', file3)
    for x in synsets3:
        synsets_final.append(x)

    file4 = open('datatest/data_test/4.json')
    synsets4 = alt_gen('pekan', file4)
    for x in synsets4:
        synsets_final.append(x)

    file5 = open('datatest/data_test/5.json')
    synsets5 = alt_gen('lebu', file5)
    for x in synsets5:
        synsets_final.append(x)

    file6 = open('datatest/data_test/6.json')
    synsets6 = alt_gen('abu', file6)
    for x in synsets6:
        synsets_final.append(x)

    file7 = open('datatest/data_test/7.json')
    synsets7 = alt_gen('peci', file7)
    for x in synsets7:
        synsets_final.append(x)

    file8 = open('datatest/data_test/8.json')
    synsets8 = alt_gen('koran', file8)
    for x in synsets8:
        synsets_final.append(x)

    file9 = open('datatest/data_test/9.json')
    synsets9 = alt_gen('susur', file9)
    for x in synsets9:
        synsets_final.append(x)

    file10 = open('datatest/data_test/10.json')
    synsets10 = alt_gen('temu', file10)
    for x in synsets10:
        synsets_final.append(x)

    file11 = open('datatest/data_test/11.json')
    synsets11 = alt_gen('suar', file11)
    for x in synsets11:
        synsets_final.append(x)

    file12 = open('datatest/data_test/12.json')
    synsets12 = alt_gen('lilin', file12)
    for x in synsets12:
        synsets_final.append(x)

    file13 = open('datatest/data_test/13.json')
    synsets13 = alt_gen('sakat', file13)
    for x in synsets13:
        synsets_final.append(x)

    file14 = open('datatest/data_test/14.json')
    synsets14 = alt_gen('satwa', file14)
    for x in synsets14:
        synsets_final.append(x)

    file15 = open('datatest/data_test/15.json')
    synsets15 = alt_gen('binatang', file15)
    for x in synsets15:
        synsets_final.append(x)

    file16 = open('datatest/data_test/16.json')
    synsets16 = alt_gen('fiksi', file16)
    for x in synsets16:
        synsets_final.append(x)

    file17 = open('datatest/data_test/17.json')
    synsets17 = alt_gen('lamur', file17)
    for x in synsets17:
        synsets_final.append(x)

    file18 = open('datatest/data_test/18.json')
    synsets18 = alt_gen('radas', file18)
    for x in synsets18:
        synsets_final.append(x)

    file19 = open('datatest/data_test/19.json')
    synsets19 = alt_gen('persentase', file19)
    for x in synsets19:
        synsets_final.append(x)

    file20 = open('datatest/data_test/20.json')
    synsets20 = alt_gen('bandrek', file20)
    for x in synsets20:
        synsets_final.append(x)

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()
    file7.close()
    file8.close()
    file9.close()
    file10.close()
    file11.close()
    file12.close()
    file13.close()
    file14.close()
    file15.close()
    file16.close()
    file17.close()
    file18.close()
    file19.close()
    file20.close()

    akurasi = f1_score(synsets_final, synsets_manual)

    print('ini akurasi', akurasi)