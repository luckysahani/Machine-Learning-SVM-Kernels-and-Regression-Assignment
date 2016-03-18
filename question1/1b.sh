#!/bin/bash

printf "Part B : Using Standard Formulation \n-------------------------------------------------\n
We will consider 5 cases in which, for each case we will take 2 folders as a testing folder 
and other folders as training folders.The accuracy for each of the cases are given below:\n"

for i in {1..10}
do
	for ((j=$((i+1));j<=10;j++));
	do
		printf "\nCase $i , $j: Testing folder is $i and $j :\n-------------------------------------------------\n"
		python 1b.py $j $i | awk '/---------/{y=1;next}y'
	done
done

# printf "\nAverage (Part B)\n-------------------------------------------------\n"
# printf "Average Accuracy = \n"