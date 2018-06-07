import json
import pandas as pd
import numpy as np

def synsets_to_dataframe(word, thesa):
    list_set = []
    for val in thesa[word]:
        word_set = set(val)
        word_set.add(word)
        list_set.append(word_set)
    dt = list_set
    list_dataframe = []

    for ls in dt:
        df = pd.DataFrame(data=False, index=ls, columns=ls)
        np.fill_diagonal(df.values, True)
        list_dataframe.append(df)
    return list_dataframe

def check_validation(word, thesa):
    lines = thesa[word]
    output = []
    matriks_synset = synsets_to_dataframe(word, thesa)
    for matrik in matriks_synset:
        for line in lines:
            for sense in line:
                if thesa.get(sense) is not None:
                    for inner_senses in thesa[sense]:
                        for inner_sense in inner_senses:
                            if sense in matrik.index and inner_sense in matrik.index:
                                matrik[sense][inner_sense] = True
                                matrik[word][sense] = True
        output.append(matrik)
    return output

def evaluate_synsets(matrik):
    series = matrik.all()
    result = series[series == True]
    return sorted(set(result.index))

def alt_gen(word, file):
    thesa = json.load(file)
    matrixs = check_validation(word, thesa)
    sets_list = []
    for matrix in matrixs:
        synset = evaluate_synsets(matrix)
        sets_list.append(synset)
    return sets_list

#ekstraksi synset
def synsets_extraction(file):
    #print('Proses ekstraksi synset')
    thesa = json.load(file)
    calon_synsets = []
    count_synset = 0
    for word in thesa:
        output = alt_gen(word, open('datatest/1.json'))
        for synsets in output:
            calon_synsets.append(synsets)
            count_synset += 1
    #print('done\n'+'Terdapat : ' + str(count_synset) + ' synsets yang berhasil di ekstrak')

    #delete redundant data
    synsets = calon_synsets
    #print('Menghapus data redundant')
    new_synset = []
    count_synset_after = 0
    for synset in synsets:
        #print(len(synset))
        #remove zero synset in list
        if len(synset) != 0:
            new_synset.append(synset)

    #remove duplicate synsets
    new_set = set(tuple(syns) for syns in new_synset)
    new_synset = [list(syns) for syns in new_set]

    #sum synset after delete redundant and zero list
    for x in new_synset:
        count_synset_after += 1
    #print('done\nBerhasil menghapus ' + str(count_synset - count_synset_after) + ' synsets duplikat')
    #print('Terdapat : ' + str(count_synset_after) + ' synsets setelah menghapus data duplikat')

    return new_synset