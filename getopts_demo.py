#!/usr/bin/python

import sys
import getopt

# define variables and defaults
kmer = 0
file_name = ""

# pass in commmands line args array
argv = sys.argv[1:]

# Get options demo for a script which takes in a file and a kmer parameter

try:
    opts, args = getopt.getopt(argv, "hk:f:") # h does not require input so the is no : after it
except getopt.GetoptError:
    print 'kmer.py -k <kmer_size> -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'kmer.py -k <kmer_size> -f <inputfile>'
        sys.exit()
    elif opt in ("-k"):
        kmer = arg
    elif opt in ("-f"):
        file_name = arg
print "Kmer size is:", kmer
print "Input file is:", file_name
