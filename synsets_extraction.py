import itertools
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
                                matrik[word][sense] = True
                                matrik[sense][inner_sense] = True

        output.append(matrik)
    return output

def evaluate_synsets(matrik, word):
    synsets = []
    for i in range(len(matrik.index), 1, -1):
        for k in itertools.combinations(matrik.index, i):
            sub_matrix = matrik.loc[list(k), list(k)]

            is_synset = all(sub_matrix.all().values)
            if is_synset:
                new_synset = sorted(sub_matrix.all().index)
                similar = False
                for syn in synsets:
                    if set(new_synset) < set(syn):
                        similar = True
                if not similar:
                    synsets.append(new_synset)
    if len(synsets) == 0:
        synsets = [word]
    #print(synsets)
    return sorted(synsets)

def alt_gen(word, file):
    thesa = json.load(file)
    matrixs = check_validation(word, thesa)
    #print(matrixs)
    sets_list = []
    for matrix in matrixs:
        synset = evaluate_synsets(matrix, word)
        sets_list.append(synset)
    return sets_list