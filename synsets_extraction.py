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

def evaluate_synsets(matrik):
    count_true = 0
    # for col_name, column in matrik.transpose().iterrows():
    #     print(column)
    for name, values in matrik.iteritems():
        print('{name}: {value}'.format(name=name, value=values[0]))
        count_true += matrik[name].value_counts()
    # for colm in matrik:
    #     print('colm ', colm)
    #     print('matrik[colm] ', matrik[colm].index[1])
    #     #print(matrik[colm].index.values)
    #     count_true += matrik[colm].value_counts(True)
    #     #print(matrik[colm].value_counts())
    #print(count_true)
    series = matrik.all()
    print(series)
    result = series[series == True]
    return sorted(set(result.index))

def alt_gen(word, file):
    thesa = json.load(file)
    matrixs = check_validation(word, thesa)
    print(matrixs)
    sets_list = []
    for matrix in matrixs:
        synset = evaluate_synsets(matrix)
        sets_list.append(synset)
    return sets_list