import csv
from collections import Counter


#Open the CSV File
reader = csv.DictReader(open('wine.csv'))
result = {}

#Read the contents of CSV file into dictionary. 
for row in reader:
	result[row['id']] = row['description']


noDocs = len(result)

print(noDocs)

#print(list(result.values()))

query = 'tremendous' 
docCount = 0
for k, v in result.items():
	if query in v:
		docCount = docCount + 1
		docId = k
		print("Doc Id:", docId)
		docLen = len(v.split())
		print("Doc Length", docLen)
		counts = Counter(v.split())
		freq = counts[query]
		print("Word Frequency", freq)
		tf = (freq/docLen)
		print("Tf:", tf)
		#print(len([item for item in v if item]))
		
#print(keys)
print(docCount)
