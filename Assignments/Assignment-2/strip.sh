#! /bin/bash
K=$1
M=$2
file=$3
head -n -$M $file | tail -n +$K 
