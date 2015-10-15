import csv
import nltk
from collections import Counter
import numpy as np
from sklearn import svm
from itertools import izip

input_file='train_hindi.csv'

all_words = list()
count_docs = 0
with open(input_file,"rb") as f:
	reader=csv.reader(f,delimiter=',')
	for row in reader:
		count_docs+=1
		#tokenize
		words_list = nltk.word_tokenize(row[1]+row[2])
		term_count = Counter(words_list)
		for ele in term_count.keys():
			if term_count[ele] >=3:
				all_words.append(ele)

len(all_words)
all_words = list(set(all_words))
len(all_words)

#list of list
#term_doc_mat = list()
#term_doc_mat = [[0] * len(all_words)] * count_docs
term_doc_mat = [ [0]* len(all_words) for _ in xrange(count_docs) ]

with open(input_file,"rb") as f:
	reader=csv.reader(f,delimiter=',')
	for row_num, row in enumerate(reader):
		#tokenize
		words_list = nltk.word_tokenize(row[1]+row[2])
		term_count = Counter(words_list)
		for ele in term_count.keys():
			if ele in all_words:
				col_num = all_words.index(ele)
#			curr_count = term_doc_mat[row_num][col_num]
#			new_count = curr_count + term_count[ele]
				term_doc_mat[row_num][col_num] += term_count[ele]


train_labels=list()
with open(input_file,"rb") as f:
	reader=csv.reader(f,delimiter=',')
	for row in reader:
		count_docs+=1
		train_labels.append(int(row[0]))


# get test data

test_file = 'test_hindi.csv'

count_docs = 0
with open(test_file,"rb") as f:
 	reader=csv.reader(f,delimiter=',')
	for row in reader:
		count_docs+=1
train_labels_obtained
test_term_doc_mat = [ [0]* len(all_words) for _ in xrange(count_docs) ]
test_labels=list()
with open(test_file,"rb") as f:
	reader=csv.reader(f,delimiter=',')
	for row_num, row in enumerate(reader)train_labels_obtained:
		test_labels.append(int(row[0]))
		#tokenize
		words_list = nltk.word_tokenize(row[1]+row[2])
		term_count = Counter(words_list)
		for ele in term_count.keys():
			if ele in all_words:
				col_num = all_words.index(ele)
#			curr_count = term_doc_mat[row_num][col_num]
#			new_count = curr_count + term_count[ele]
				test_term_doc_mat[row_num][col_num] += term_count[ele]






#from itertools import izip



X = np.array(term_doc_mat)
#y = np.array(train_labels)
y=train_labels
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)

labels_obtained=list()

#test_X = np.array(test_term_doc_mat)
for ele in test_term_doc_mat:
	sol = (clf.predict(ele)).tolist()[0]
	labels_obtained.append(sol)

train_labels_act=list()
train_labels_obtained=list()
with open(input_file,"rb") as f:
	reader=csv.reader(f,delimiter=',')
	for row_num, row in enumerate(reader):
		train_labels_act.append(int(row[0]))


train_labels_obtained=list()
for ele in term_doc_mat:
        sol = (clf.predict(ele)).tolist()[0]
        train_labels_obtained.append(sol)



accuracy = 0
for i, j in izip(labels_obtained, test_labels):
	if i==j:
		accuracy+=1

accuracy = 0
for i, j in izip(train_labels_obtained, train_labels_act):
	if i==j:
		accuracy+=1

print accuracy
print accuracy/float(len(test_labels))


