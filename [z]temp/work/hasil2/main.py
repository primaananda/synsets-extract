#created by primaananda
import csv

#berisi list noun
def get_noun():
    noun = []
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            noun.append(row[1])
    return noun

#berisi list verb
def get_verb():
    verb = []
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            verb.append(row[2])
    return verb

#berisi list adjektiva
def get_adje():
    adje = []
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adje.append(row[3])
    return adje

#berisi list adverb
def get_adve():
    adve = []
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adve.append(row[4])
    return adve

#berisi list gabungan antara noun, verb, adjektiva, dan adverb
def get_pasangan():
    pasangan = []
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pasangan.append(row[1]+row[2]+row[3]+row[4])
    return pasangan

index = []

#berisi dict kata pertama
def get_kata():
    kata = {}
    with open('hasil/tesaurus_hasil.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            index.append(row[0])
            kata[row[0]] = []
            kata[row[0]].extend(row[1].split(','))
            kata[row[0]].extend(row[2].split(','))
            kata[row[0]].extend(row[3].split(','))
            kata[row[0]].extend(row[4].split(','))
    return kata

def ekstraksi():
    calon_synset_tesaurus = {}
    tesa = get_kata()
    temp = ''
    for kata in tesa:
        calon_synset_tesaurus[kata] = []
        for kata_pasangan in tesa[kata]:
            daftar_pasangan_tesaurus = []
            if kata_pasangan in tesa:
                daftar_pasangan_tesaurus.extend(tesa[kata_pasangan])
                if kata in daftar_pasangan_tesaurus:
                    calon_synset_tesaurus[kata].append(kata_pasangan)
    return calon_synset_tesaurus

def cek_pasangan(key, value, tesa) :
    if(value in tesa[key]) and (key in tesa[value]) :
        return True
    else:
        return False

#main func
def ekstraksi_synset_indonesia():
    calon_synset_tesaurus = {}
    pasangan = []
    tesa = get_kata()
    temp = ''
    #print tesa
    for key, value in tesa.items():
        '''calon_synset_tesaurus[kata] = []
        for kata_pasangan in tesa[kata]:
            daftar_pasangan_tesaurus = []
            if kata_pasangan in tesa:
                daftar_pasangan_tesaurus.extend(tesa[kata_pasangan])
                if kata in daftar_pasangan_tesaurus:
                    calon_synset_tesaurus[kata].append(kata_pasangan)
        '''
        for v in value :
            try :
                if (v in tesa[key]) and (key in tesa[v]) :
                    calon = [key,v]
                    if not (([key,v] in pasangan) or ([v,key] in pasangan)):
                        pasangan.append(calon)
            except:
                pass
    print pasangan
    return pasangan

def save_to_txt(data):
    with open('hasil/final.txt','w') as file:
        '''
        for x in index:
            file.write(str(x))
            for y in data[x] :
                file.write(', ' + str(y))
            file.write('\n')
        '''
        for x in data:
            file.write(str(x)+'\n')
def main():
    data = ekstraksi_synset_indonesia()
    save_to_txt(data)
    
    
main()