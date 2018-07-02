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

    file1 = open('datatest/data_test/21.json')
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

    file21 = open('datatest/data_test/21.json')
    synsets21 = alt_gen('minggu', file21)
    for x in synsets21:
        synsets_final.append(x)

    file22 = open('datatest/data_test/22.json')
    synsets22 = alt_gen('esa', file22)
    for x in synsets22:
        synsets_final.append(x)

    file23 = open('datatest/data_test/23.json')
    synsets23 = alt_gen('pengguguran', file23)
    for x in synsets23:
        synsets_final.append(x)

    file24 = open('datatest/data_test/24.json')
    synsets24 = alt_gen('pasar', file24)
    for x in synsets24:
        synsets_final.append(x)

    file25 = open('datatest/data_test/25.json')
    synsets25 = alt_gen('rekan', file25)
    for x in synsets25:
        synsets_final.append(x)

    file26 = open('datatest/data_test/26.json')
    synsets26 = alt_gen('kopiah', file26)
    for x in synsets26:
        synsets_final.append(x)

    file27 = open('datatest/data_test/27.json')
    synsets27 = alt_gen('songkok', file27)
    for x in synsets27:
        synsets_final.append(x)

    file28 = open('datatest/data_test/28.json')
    synsets28 = alt_gen('parafin', file28)
    for x in synsets28:
        synsets_final.append(x)

    file29 = open('datatest/data_test/29.json')
    synsets29 = alt_gen('parasit', file29)
    for x in synsets29:
        synsets_final.append(x)

    file30 = open('datatest/data_test/30.json')
    synsets30 = alt_gen('serbat', file30)
    for x in synsets30:
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
    file21.close()
    file22.close()
    file23.close()
    file24.close()
    file25.close()
    file26.close()
    file27.close()
    file28.close()
    file29.close()
    file30.close()

    for x in synsets_final:
        print(x)

    akurasi = f1_score(synsets_final, synsets_manual)

    print('akurasi', akurasi)