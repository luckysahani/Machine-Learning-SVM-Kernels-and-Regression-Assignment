import re,time,os,sys,numpy
from sklearn.svm import LinearSVC,SVC 
from sklearn.cross_validation import KFold

X = []
Y = []
data = open('connect-4.data', 'r')

data_total = []
for line in data:
	line = line.rstrip('\n').split(',')
	data_total.append(line)

X = [[0]*(42*3) for i in range(len(data_total))]
Y = [0]*len(data_total)
class_dict = {'win': 1, 'draw': 0, 'loss': -1}
position_dict = {'o':0 , 'b':1, 'x':2}

for index in range(0,len(data_total)):
	for i in range(42):
		X[index][3*i + position_dict[data_total[index][i]]] = 1
	Y[index] = class_dict[data_total[index][42]]

for i in range(0,5):
	for m,n in KFold(len(data_total), n_folds=5,shuffle=True):
		train_index =m
		test_index = n

	# print "Reading files to make Training and Testing Dataset "
	start_time = time.time()

	X_train = [[0]*(42*3) for i in range(len(train_index))]
	Y_train = [0]*len(train_index)
	X_test = [[0]*(42*3) for i in range(len(test_index))]
	Y_test = [0]*len(test_index)
	for indx in range(len(train_index)):
		X_train[indx] = X[train_index[indx]]
		Y_train[indx] = Y[train_index[indx]]
	for indx in range(len(test_index)):
		X_test[indx] = X[test_index[indx]]
		Y_test[indx] = Y[test_index[indx]]

	end_time = time.time() - start_time
	# print "It took "+ str(end_time) + " to make the Training and Testing Dataset"
	# print "Training and Testing Dataset completed"

	# print '\nTraining Classifier'
	start_time = time.time()
	one_vs_one__classifier = SVC()
	one_vs_one__classifier.fit(X_train, Y_train)
	end_time = time.time() - start_time
	# print "It took "+ str(end_time) + " to train the classifiers"
	# print 'Training Completed'

	# print '\nTesting data '
	start_time = time.time()
	# Calculating Accuracy
	one_vs_one__classifier_accuracy = one_vs_one__classifier.score(X_test, Y_test)

	end_time = time.time() - start_time
	# print "It took "+ str(end_time) + " to test the data "
	# print 'Testing Completed'

	# # print '\n# printing Accuracy'
	# print "\nCase "+str(i)+" : \n"
	# print "-------------------------------------------------"
	print "\nOne vs One accuracy : "+ str(one_vs_one__classifier_accuracy)
