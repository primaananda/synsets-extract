#created by primaananda
import re
import csv

types = ['v','a','n','adv', 'p', 'pron', 'num']

#perulangan untuk menghilangkan baris tab dan hanya mengambil yang tidak ada tabnya dan dimasukan kedalam tampungan dicts
def preprocessing(file):
	data = []
	dicts = []
	dicts2 = []
	letter = '###'
	temp2 = ''
	lines = file.readline()
	while lines:
		if(not lines.startswith('\t')):
			data.append(lines.rstrip())
		lines = file.readline()
		if not lines:
			break
	###
	#merapikan text untuk yang kata"nya kepotong dan mengambil text yang diperlukan perulangan untung membaca dan menampung huruf sesuai yang di awali oleh kress(#) : contoh bila #A maka yang ditampung huruf awalny A
	for x in range(0,len(data)):
		temp = ''
		if(data[x].startswith('#')):
			letter = data[x][1].lower() #.lower berfungsi untuk membuat huruf kapital menjadi kecil
		if(data[x].startswith(letter)):
			temp += data[x]
			while(data[x].endswith(',')) or (data[x].endswith('-')):
				if(data[x].endswith(',')): #kalau diakhiri ',' maka kata/kalimat digabung dengan kata/kalimat berikutnya
					temp = temp + ' '
					temp += data[x+1]
					x =  x+1
				elif(data[x].endswith('-')): #kalau diakhiri '-' maka huruf terakhir yaitu - dihilangkan lalu digabungkan dengan kata berikutnya
					temp = temp[:-1]
					temp += data[x+1]
					x = x+1
			dicts.append(temp)
	###
	#hapus whiespace yang berlebihan dan hapus kata kata yang tidak diperlukan seperti (cak), k, adv
	for k in dicts:
		k = re.sub('\(.*?\)','',k) #menghilangkan kata yang dalam '(kata)'
		for ch in ['  ','	 ', '1 ', '2 ', '3 ', '4 ', '5', '6', '7']:
			if ch in k:
				k = k.replace(ch,'')
		for ch2 in [';']:
			k = re.sub(';',',',k)
		temp2 = k
		dicts2.append(temp2)
	#deleting empty list
	#list1 = [x for x in dicts2 if x]
	return dicts2

#perulangan untuk menulis hasil yang ada di dicts2 kedalam file txt bernama tesaurus_clear_text.txt
def add_file(data, files):
    for x in data:
        files.write(x+'\n')

def get_lowest_type_index(line):
	value = []
	for type in types :
		if(type in line):
			value.append(line.index(type))
	return min(value)

def get_type_sequence(line):
    sequence = []
    for word in line:
        if word in types:
            sequence.append(word)
    return sequence

def get_type_index(types, line):
    sequence = []
    for type in types:
        sequence.append(line.index(type))
    return sequence

#merubah ke csv
def txt_to_csv(file, files):
    dicts = []
    writer = csv.writer(files, delimiter=',')
    writer.writerow(["Kata","Noun","Verb","Adjektiva","Adverb"])
    for line in file:
        noun = []
        verb = []
        adv = []
        adj = []
        tempword = ''
        dicts = [x.rstrip(',') for x in line.split()]
        #edit wordnya
        word = dicts[0:get_lowest_type_index(dicts)]
        dicts = dicts[get_lowest_type_index(dicts):]
        sequence = get_type_sequence(dicts)
        index_sequence = get_type_index(sequence, dicts)
        index_sequence.append(len(dicts))
        type = []
        for x in range(0, len(index_sequence)-1):
        	type.append(dicts[index_sequence[x]:index_sequence[x+1]])
        #print type
        kata = word[0:1]
        #print kata
        try:
            if type[0][0] in types:
                if type[0][0] == 'n':
            	    noun = type[0][1:]
                elif type[0][0] == 'v':
                    verb = type[0][1:]
                elif type[0][0] == 'adv':
                    adv = type[0][1:]
                elif type[0][0] == 'a':
                    adj = type[0][1:]
                else:
                    tempword = type[0][1:]
            elif type[1][0] in types:
                if type[0][0] == 'n':
            	    noun = type[0][1:]
                elif type[0][0] == 'v':
                    verb = type[0][1:]
                elif type[0][0] == 'adv':
                    adv = type[0][1:]
                elif type[0][0] == 'a':
                    adj = type[0][1:]
                else:
                    tempword = type[0][1:]
            elif type[2][0] in types:
                if type[0][0] == 'n':
            	    noun = type[0][1:]
                elif type[0][0] == 'v':
                    verb = type[0][1:]
                elif type[0][0] == 'adv':
                    adv = type[0][1:]
                elif type[0][0] == 'a':
                    adj = type[0][1:]
                else:
                    tempword = type[0][1:]
        except IndexError:
            print 'index'
        writer.writerow([kata[0],','.join(noun),','.join(verb),','.join(adj),','.join(adv)])

def main():
    file = open('hasil/final/tesaurus_hasil_convert_from_pdf.txt','r')
    file_text_write = open('hasil/final/tesaurus_clear_text.txt','w')
    file_csv = open('hasil/final/tesaurus.csv','w')
	
    dpro = preprocessing(file)
    
    #import to txt
    add_file(dpro, file_text_write)
    
    #txt to csv
    txt_to_csv(dpro, file_csv)
    
    file.close()
    file_text_write.close()

main()