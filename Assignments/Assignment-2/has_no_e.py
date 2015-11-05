def has_no_e(line):
    for i in line:
        if (i == "e"):
            return False
    return True
reader = open("gadsby.txt",'r')
#make integer variables to track trues and falses
#t = 0
#f = 0
for line in reader:
    has_no_e(line)
    #if (has_no_e(line) == True):
        #t += 1
    #else:
        #f += 1
#outputs number of trues and falses to check behavour in big files
#print ("Number of lines without an e: " + str(t))
#print ("Number of lines with an e: " + str(f))
#commented out test code, uncomment to see it work
