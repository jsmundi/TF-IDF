#Jaiteg S Mundi
#CS 483: Web Data
#Assignment 2: TF-IDF

from collections import Counter
from operator import itemgetter
import csv
import math 
import sys

#Open the CSV File
reader = csv.DictReader(open('wine.csv'))
corpus = {}

#Read the contents of CSV file into dictionary. 
for row in reader:
	corpus[row['id']] = row['description'] 


#Accepts two terms d document id as a string and t the term as a string
#Calculated the frequency of the term in the given document. 
#Stores the term frequency and the corresponding document in a dictionary.
#If term is not found in the document returns 0 
#Returns the Dictionary 
def tf(d, t):

	tfList = {}

	#Split up all the words in given document and count frequency of all words in document
	description = corpus[d]
	docLength = len(description.split())
	counts = Counter(description.split())
	word = t.split()

	#Find the frequency of given term t in the document d
	for word in word:
		termCount = 0
		tFreq = 0 
		termCount = termCount + counts[word]
		tFreq = (math.log(1+(termCount/docLength)))
		tfList[word] = tFreq

	#If the word not found in document return 0
	for key, value in tfList.items():
		if(value == 0):
			return 0 

	return tfList

#Accept document d and query
#Returns the relevance of query and corresponding document if TF is not zero
def relevance(d, query):

	#Calculate total number of times query appears in the corpus
	nDocsQ = nDocs(d, query)
	relv = 0

	#Get the tf 
	TF = tf(d, query)

	#Test if terms found or not
	if(TF == 0):
		return 0 

	#Calculate relevance 
	sTF = sum(TF.values())
	relv = sTF/nDocsQ

	if relv == 0:
		return 0 

	return relv

#Calculate total number of times query appears in the corpus
def nDocs(d,query):

	nDocs = 0

	if ((len(query.split())) > 1):
		for key, values in corpus.items():
			if(query in values):
				nDocs = nDocs + 1
	else:
		for key, values in corpus.items():
			if(query in values.split()):
				nDocs = nDocs + 1

	return nDocs

#Accepts query and k number of top scores to be returned.
#Finds all the documents in the corpus containing the query.
#If query exists in the documents calculates the relevance score
#Returns a list of k tuples containing the id and score in descending order (score)
def tf_idf(query, k):
	
	docsList = []
	rel = []
	d = []
	score = []

	#Find the doucments containing the query in corpus
	#Append the document IDs into a list 
	if ((len(query.split())) > 1):
		for key, values in corpus.items():
			if(query in values):
				docsList.append(key)
	else:
		for key, values in corpus.items():
			if(query in values.split()):
				docsList.append(key)

	#Calculate the score for the list of documents 			
	for x in range(len(docsList)):
		#Add the relevance to rel list 
		rel.append(relevance(docsList[x], query))
		#Add the document ID to d list 
		d.append(docsList[x])
		#Create a list of tuples using rel and d
		score = (list(zip(d, rel)))
		
	#Sort the score
	score = sorted(score, key=itemgetter(1), reverse=True)

	#Return k results in list of tuples 
	return(score[:k])

def menu():
	print("MENU TF-IDF ")
	print("1. Calculate TF-IDF")
	print("2. Calculate relevance")
	print("3. Calculate tf")
	choice = (input("Enter your choice: "))
	return choice

def main():

	results = []
	loop = True
	k = 0

	while loop:
		choice = menu()
		if choice == '1':
			query = input("Enter query: ")
			k = input("Number of returned results (k): ")
			k = int(k)
			s = ((tf_idf(query, k)))
			print(s)
			exit()

		if choice == '2':
			d = input("Enter document ID: ")
			query = input("Enter query: ")
			s = ((relevance(d, query)))
			print(s)
			exit()

		if choice == '3':
			d = input("Enter document ID: ")
			term = input("Enter term: ")
			s = ((tf(d, term)))
			print(s)
			exit()
	

if __name__ == '__main__':
	main()