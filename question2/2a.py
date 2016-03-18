import re,time,os,sys,numpy
from sklearn.svm import LinearSVC,SVC 
from sklearn.cross_validation import KFold

X = []
Y = []
X_train = []
Y_train = []
X_test = []
Y_test = []
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

	print "Reading files to make Training and Testing Dataset "
	start_time = time.time()

	for indx in train_index:
		X_train.append(X[index])
		Y_train.append(Y[index])
	for indx in test_index:
		X_test.append(X[index])
		Y_test.append(Y[index])

	end_time = time.time() - start_time
	print "It took "+ str(end_time) + " to make the Training and Testing Dataset"
	print "Training and Testing Dataset completed"

	print '\nTraining Classifier'
	start_time = time.time()
	one_vs_all__classifier = LinearSVC(multi_class = 'ovr')
	one_vs_all__classifier.fit(X_train, Y_train)
	end_time = time.time() - start_time
	print "It took "+ str(end_time) + " to train the classifiers"
	print 'Training Completed'

	print '\nTesting data '
	start_time = time.time()
	# Calculating Accuracy
	one_vs_all__classifier_accuracy = one_vs_all__classifier.score(X_test, Y_test)

	end_time = time.time() - start_time
	print "It took "+ str(end_time) + " to test the data "
	print 'Testing Completed'

	# print '\nprinting Accuracy'
	print "\nCase "+i+" : \n"
	print "-------------------------------------------------"
	print "One vs All accuracy : "+ str(one_vs_all__classifier_accuracy)
