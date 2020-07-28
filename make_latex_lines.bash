#!/bin/bash


input=equations_latex.json
cmd=prog

while read line
do
        file=$(echo $line | cut -d':' -f1)
        #key=$(echo $line | cut -d' ' -f2)
        #log=$(echo $line | cut -d' ' -f3)
        #lat=$(echo $line | cut -d' ' -f4)
        #echo $cmd $key $log $lat $file
        echo $file
done < "$input"
