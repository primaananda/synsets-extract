"""
author by Prima Ananda
created 01 maret 2018 with love
"""

import PyPDF2
#import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#agar dapat membaca file
filename = 'resources/tesaurus2008.pdf'

pdfFIleObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFIleObj)

num_pages = pdfReader.numPages
count = 8
text = ""

#looping membaca tiap halaman

while count < num_pages:
	pageObj = pdfReader.getPage(count)
	count += 1
	text += pageObj.extractText()
	print ('', count)

#print text

#this if statement exist to check if the above library returned words.
#It's done because PyPDF2 cannot read scanned files.
#if text != "":
#	text = text
#else:
#	text = textract.process(fileurl, method='teserract', language='eng')

#text = text.replace('- ', '')
#text = text.replace('  ', '')
#text = text.replace('\n', ' ')
#text = text.replace('- ', '')
file = open('hasil/tesaurus_pypdf2.txt','w')
file.write(text.encode("UTF-8"))
file.close()