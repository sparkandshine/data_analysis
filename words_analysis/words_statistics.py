#!/usr/bin/env python3
from fileinput import filename

#fname = "datasets/english_words.txt"
fname = "datasets/just_for_test.txt"

# read file to list
with open(fname) as f:
    lines = f.readlines()

for line in lines:    
    #print("original\t%s" %(line))
    print line
    print line.endswith("aa")
    if line.endswith('aa') :
        print "target", line
    

#str.endswith also accepts a tuple
#'test.mp3'.endswith(('.mp3', '.avi'))