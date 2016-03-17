#!/bin/bash

printf "Part A : Using Hinge Loss \n-------------------------------------------------\n
We will consider 5 cases in which, for each case we will take 2 folders as a testing folder 
and other folders as training folders.The accuracy for each of the 5 cases are given below:\n"

for i in {1,3,5,7,9}
do
   printf "\nCase $i: Testing folder is $i and $((i+1)):\n-------------------------------------------------\n"
   python 1a.py $i $((i+1)) | awk '/---------/{y=1;next}y'
done

printf "\nAverage (Part A)\n-------------------------------------------------\n"
printf "Average Accuracy = \n"