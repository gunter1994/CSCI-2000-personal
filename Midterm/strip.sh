#!
#Hunter Thompson: 100486809
echo Enter the number of lines from the top
read k
echo Enter the number of lines from the bottom
read m
echo Enter the filename
read filename
find . $filename | head -n -M | tail -n k | > gadsby_stripped.txt

