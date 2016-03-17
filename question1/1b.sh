#!/bin/bash

printf "Part B : Using Standard Formulation \n-------------------------------------------------\n
We will consider 5 cases in which, for each case we will take 2 folders as a testing folder 
and other folders as training folders.The accuracy for each of the 5 cases are given below:\n"

for i in {1,3,5,7,9}
do
   printf "\nCase $i: Testing folder is $i and $((i+1)):\n-------------------------------------------------\n"
   python 1b.py $i $((i+1)) | awk '/---------/{y=1;next}y'

done

printf "\nAverage (Part B)\n-------------------------------------------------\n"
printf "Average Accuracy = \n"