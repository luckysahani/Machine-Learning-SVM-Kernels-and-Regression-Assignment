import nltk
nltk.download('punkt') # for tokens
nltk.download("stopwords") # for stopwords
nltk.download('wordnet')
import re,time,os,sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
word_lemmatizer = WordNetLemmatizer()
from sklearn.svm import LinearSVC,SVC
import numpy as np

output = ()
main_dictionary = {}
final_training_dataset_values = []
final_training_dataset_keys = []
final_testing_dataset_values = []
final_testing_dataset_keys = []
testing_directory_1 = sys.argv[1]
testing_directory_2 = sys.argv[2]

def read_from_file_to_make_dictionary(file_name_with_path,file_name):
	with open(file_name_with_path,"r") as lines:
		for line in lines:
			if ( line == ""):
				continue
			tokens = nltk.word_tokenize(line)
			for token in tokens:
				token = token.lower() # making everything in lower case to avoid conflicts due to word case
				# if token.isalpha(): #and token not in stopwords.words():
				if token.isalpha() and token not in stopwords.words('english'):
					# main_dictionary.update({token: 0})
					main_dictionary.update({word_lemmatizer.lemmatize(token): 0})



def make_dictionary():
	dataset_directory = os.getcwd()+"/bare"
	print "Your dataset directory is :"+ dataset_directory
	for root, dirs, files in os.walk(dataset_directory):
		for name in files:
			read_from_file_to_make_dictionary(os.path.join(root, name),name)

def read_from_file(file_name_with_path,file_name):
	temp_dictionary = main_dictionary.copy()
	with open(file_name_with_path,"r") as lines:
		for line in lines:
			if ( line == ""):
				continue
			tokens = nltk.word_tokenize(line)
			for token in tokens:
				token = token.lower() # making everything in lower case to avoid conflicts due to word case
				# if token.isalpha(): #and token not in stopwords.words():
				if token.isalpha() and token not in stopwords.words('english'):
					# temp_dictionary.update({token: 1})
					temp_dictionary.update({word_lemmatizer.lemmatize(token): 1})
		if file_name.startswith("spm"):
			return (list(temp_dictionary.values()),"spam")
		else:
			return (list(temp_dictionary.values()),"non_spam")


def traverse_over_files(testing_directory_1,testing_directory_2):
	# global final_training_dataset_values,final_training_dataset_keys
	print "Your current working directory is :"+os.getcwd()
	dataset_directory = os.getcwd()+"/bare"
	print "Your dataset directory is :"+ dataset_directory
	get_list_of_all_subdirectories =  [dirs for root, dirs, files in os.walk(dataset_directory)]
	for dir_cur in get_list_of_all_subdirectories[0]:
		if(dir_cur == "part"+ testing_directory_1) or (dir_cur == "part"+ testing_directory_2):
			test_directory = dataset_directory+"/"+dir_cur
			print "Creating testing dataset for :"+test_directory
			for root, dirs, files in os.walk(test_directory):
				for name in files:
					currentFile=os.path.join(root, name)
					output = read_from_file(currentFile,name)
					final_testing_dataset_keys.append(output[0])
					final_testing_dataset_values.append(output[1])
		else:
			current_directory = dataset_directory+"/"+dir_cur
			print "Current working for training dataset on :"+current_directory
			for root, dirs, files in os.walk(current_directory):
				for name in files:
					currentFile=os.path.join(root, name)
					output = read_from_file(currentFile,name)
					# print output
					# raw_input()
					final_training_dataset_keys.append(output[0])
					final_training_dataset_values.append(output[1])

print "Reading files to make Dictionary "
start_time = time.time()
make_dictionary()
end_time = time.time() - start_time
print "It took "+ str(end_time) + " to make the dicitonary"
print "Dictionary completed"

print "Reading files to make Training Dataset "
start_time = time.time()
traverse_over_files(str(testing_directory_1),str(testing_directory_2))
end_time = time.time() - start_time
print "It took "+ str(end_time) + " to make the Training Dataset"
print "Training Dataset completed"

print '\nTraining data'
start_time = time.time()
linear_svm_classifier = LinearSVC(loss = 'l1')
linear_svm_classifier.fit(final_training_dataset_keys, final_training_dataset_values)
end_time = time.time() - start_time
print "It took "+ str(end_time) + " to train the classifiers"
print 'Training Completed'

print '\nTesting data '
start_time = time.time()
# Calculating Accuracy
linear_svm_classifier_accuracy = linear_svm_classifier.score(final_testing_dataset_keys, final_testing_dataset_values)

end_time = time.time() - start_time
print "It took "+ str(end_time) + " to test the data "
print 'Testing Completed'

# print '\nprinting Accuracy'
print "\nCase : Testing folder is part"+str(testing_directory_1)+' and '+str(testing_directory_2)
print "-------------------------------------------------"
print "Linear SVM with hinge loss accuracy : "+ str(linear_svm_classifier_accuracy)


# print 'Training Size:'+str(len(final_training_dataset_keys))+' and Testing size = '+str(len(final_testing_dataset_keys))