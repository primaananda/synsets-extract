#created by prima ananda 10 may 2018
import re
import csv

types = ['1','2','3','4','5','6']

def preprocessing(file):
    dicts = []
    dicts2 = []
    temp2 = ''
    lines = file.readline()
    while lines:
        dicts.append(lines.rstrip())
        lines = file.readline()
    
    for k in dicts:
        k = re.sub('\(.*?\)','',k) #hapus kata yang berada dalam kurung
        for character in [' n ', ' v ', ' a ', ' adv ', ' p ', ' num ', '  ']:
            if character in k:
                k = k.replace(character,' ')
        for chara in [';']:
            k = re.sub(';',',',k)
        temp2 = k
        dicts2.append(temp2)
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
    writer.writerow(["Kata","sense-1","sense-2","sense-3","sense-4","sense-5"])
    count = 0
    for line in file:
        sense1 = []
        sense2 = []
        sense3 = []
        sense4 = []
        sense5 = []
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
        count += 1
        try:
        	kata = word[0:1]
        	sense1 = type[0][1:]
        	sense2 = type[1][1:]
        	sense3 = type[2][1:]
        	sense4 = type[3][1:]
        	sense5 = type[4][1:]
        except IndexError:
        	pass
        	#print "terdapat indeks kosong pada baris : " + str(count)
        #print kata
        '''
        try:
            if str(type[0][0]) in types:
                if type[0][0] == '1':
            	    print type[0][1]
            	    sense1 = type[0][1:]
                elif type[0][0] == '2':
                    sense2 = type[0][1:]
                else:
                    tempword = type[0][1:]
            elif type[1][0] in types:
                if type[0][0] == '1':
            	    sense1 = type[0][1:]
                elif type[0][0] == '2':
                    sense2 = type[0][1:]
                    print type[1][1]
                else:
                    tempword = type[0][1:]
            elif type[2][0] in types:
                if type[0][0] == '1':
            	    sense1 = type[0][1:]
                elif type[0][0] == '2':
                    sense2 = type[0][1:]
                else:
                    tempword = type[0][1:]
        except IndexError:
            print 'index zero'
        '''
        writer.writerow([kata[0],','.join(sense1),','.join(sense2),','.join(sense3),','.join(sense4),','.join(sense5)])

def main():
    text = open('src/contoh.txt','r')
    file_text = open('hasil/cleartesaurus.txt','w')
    file_csv = open('hasil/tesaurus_hasil.csv','w')
    
    pre = preprocessing(text)
    
    #import to txt
    add_file(pre, file_text)
    #import to csv
    txt_to_csv(pre, file_csv)
    
    text.close()
    file_text.close()

main()