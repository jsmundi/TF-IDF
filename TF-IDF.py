import csv
from collections import Counter
import math 


#Open the CSV File
reader = csv.DictReader(open('wine.csv'))
result = {}

#Read the contents of CSV file into dictionary. 
for row in reader:
	result[row['id']] = row['description']


noDocs = len(result)

#print(noDocs)

#print(list(result.values()))

query = 'mac watson'
docCount = 0
tfID = []
for k, v in result.items():
	if query in v:
		docCount += 1

for k,v in result.items():
	if query in v:
		tf = 0
		docLen = 0
		counts = 0
		freq = 0
		docId = k
		#print("Doc Id:", docId)
		docLen = len(v.split())
		print("Doc Length", docLen)
		counts = Counter(v.split())
		if len(query.split()) > 1:
			print(len(query.split()))  #iterate list of query words to add frequency
			print(query.split())
			freq = counts[(query)]
		print("Word Frequency", freq)
		tf = (freq/docLen)
		idf = math.log10(noDocs/docCount)
		tfIdf = tf*idf
		print("Tf:", tf)
		print("idf", idf)
		print("TFIDF", tfIdf)
		tfID.extend((docId, tfIdf))
		#print(len([item for item in v if item]))

print(tfID)



#print(tfID)
#print(keys)
#print(docCount)
#print(tfIdf)
