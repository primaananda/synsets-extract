#created by primaananda
import csv

#berisi list noun
def get_noun():
    noun = []
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            noun.append(row[1])
    return noun

#berisi list verb
def get_verb():
    verb = []
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            verb.append(row[2])
    return verb

#berisi list adjektiva
def get_adje():
    adje = []
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adje.append(row[3])
    return adje

#berisi list adverb
def get_adve():
    adve = []
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adve.append(row[4])
    return adve

#berisi list gabungan antara noun, verb, adjektiva, dan adverb
def get_pasangan():
    pasangan = []
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pasangan.append(row[1]+row[2]+row[3]+row[4])
    return pasangan

#berisi dict kata pertama
def get_kata():
    kata = {}
    with open('z_hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            kata[row[0]] = (row[1]+row[2]+row[3]+row[4]).split(',')
    return kata

def tambah_calon_synset(kata_utama, kata_pasangan):
    calon_kata = {}
    calon_kata[kata_utama] = (kata_pasangan)
    return calon_kata

def ekstraksi_synset_indonesia():
    calon_synset_tesaurus = []
    tesa = get_kata()
    for kata in tesa:
        daftar_pasangan_tesaurus = []
        for kata_pasangan in tesa[kata]:
            if kata_pasangan in tesa:
                daftar_pasangan_tesaurus.extend(tesa[kata_pasangan])
                if kata in daftar_pasangan_tesaurus:
                    calon_synset_tesaurus.append((kata, kata_pasangan))
                    #calon_synset_tesaurus.append(tambah_calon_synset(kata, kata_pasangan))
                else:
                    calon_synset_tesaurus.append(kata)
                    #calon_synset_tesaurus.append(tambah_calon_synset(kata, kata_pasangan))
    return calon_synset_tesaurus

def save_to_txt(data):
    with open('z_hasil/final/calon_synset_tesaurus.txt','w') as file:
        for x in data:
            file.write(str(x) + '\n')

def main():
    data = ekstraksi_synset_indonesia()
    save_to_txt(data)
    
main()