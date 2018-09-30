# TF-IDF

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

TF-IDF is a python program to calculated TF-IDF of a collection of documents. The data is read from csv file containing the document id and corresponding text. The data from csv is parsed into a dictionary with document ids as keys and description as values in the dictionary. 
There are three major operations that can be performed on the data. 

  - TF- calculate the term frequency | INput document id and term
  - Relevance - calculate the query | Input given document id and query
  - TF-IDF - calculates the TF-IDF of query returns k results | Input query and k

Read [Documentation](writeup.pdf)
  
## Sample of Database (CSV)

| id | description |
| ------ | ------ |
| 0 | [this tremendous 100 varietal wine ...] |
| 1 | [ripe aromas of fig blackberry and cassis...] |
| 2 | [mac watson honors the memory of a wine...] |
| ... | ... |



### Installation

TF-IDF requires [Python 3](https://docs.python-guide.org/starting/installation/) to run.

```sh
$ git clone https://github.com/jsmundi/TF-IDF_CS483_Web
$ python TF-IDF.py
```
Output after running TF-IDF.py
```sh
MENU TF-IDF 
1. Calculate TF-IDF
2. Calculate relevance
3. Calculate tf
Enter your choice: 
```



### Todos

 - Improve Menu
 - Improve speed for larger corpus

License
----

MIT

**Free Software, Yeah!**
