#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: index.py
# SPECIFICATION: This program creates an inverted index from documents in
# collection.csv using normalization and lemmatization to do so
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 1 hour
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    'home':'home',
    'homes':'home',
    'in':'in',
    'increases':'increase',
    'increasing':'increase',
    'july':'july',
    'new':'new',
    'rise':'rise',
    'rising':'rise',
    'sale':'sale',
    'sales':'sale',
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    norm_text = text.lower()
    norm_text = norm_text.replace('.', '')

    # Tokenizing the document
    # --> add your Python code here
    tok_list = norm_text.split()

    # Applying lemmatization
    # --> add your Python code here
    lem_list = []
    for token in tok_list:
        lem_list.append(lemmas.get(token))

    # Building the inverted index
    # --> add your Python code here
    for lemma in lem_list:
        invertedIndex.setdefault(lemma, []).append(docID)

# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here
for term in sorted(invertedIndex):
        print(term, ':', invertedIndex.get(term))