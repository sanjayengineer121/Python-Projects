Code for Shell script to print first 5 odd numbers 


echo Enter a 5 digit number

read num

n=1

while [ $n -le 5 ]

do

a=`echo $num | cut -c $n`

echo $a 

n=`expr $n + 2`

done







2nd







#!/bin/bash

for n in {1..10..2}

do

   echo $n
   
done

