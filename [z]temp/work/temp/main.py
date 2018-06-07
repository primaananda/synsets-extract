"""
created by : Prima Ananda
"""
import json

#untuk membaca data tesaurus
file_tesaurus = open('tesaurus2008.json','r')
#untuk baca file json tesaurus
with file_tesaurus as jsonf:
    tesaurus = json.load(jsonf)

#untuk baca detail data
#for kata in tesaurus:
#    for synset in tesaurus[kata] :
#        print(kata, synset)

def cari_pasangan(kata):
    hasil_kata = []
    for synset in tesaurus[kata] :
        hasil_kata.append(synset)
    return hasil_kata

def ekstraksi_synset_indonesia():
    daftar_pasangan = []
    daftar_pasangan_tesaurus = []
    calon_synset_tesaurus = []
    for kata in tesaurus:
        daftar_pasangan = cari_pasangan(kata)
        #print('daftar pasangan : ',daftarPasangan)
        for kata_pasangan in daftar_pasangan:
            if kata_pasangan in tesaurus:
                daftar_pasangan_tesaurus.append(kata_pasangan)
                #print('daftar pasangan tesauruaas ',daftarPasanganTesaurus)
                if kata in daftar_pasangan_tesaurus:
                    calon_synset_tesaurus.append((kata, kata_pasangan))
                else:
                    calon_synset_tesaurus.append(kata)
    print(calon_synset_tesaurus)

ekstraksi_synset_indonesia()
