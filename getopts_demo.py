#!/usr/bin/python

import sys
import getopt

# define variables and defaults
kmer = 10
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
    # print output for help
    if opt == '-h':
        print 'kmer.py -k <kmer_size> -f <inputfile>'
        sys.exit()
    # parse the -k command line parameter 
    elif opt in ("-k"):
        kmer = arg # make command line input for -k  equal to var kmer
    # parse the -f command line parameter
    elif opt in ("-f"):
        file_name = arg # make commandline input for -f equal to var file_name
print "Kmer size is:", kmer
print "Input file is:", file_name
