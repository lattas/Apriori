"""DMST Algorithms 3rd Assignment 2015"""
#
# a_priori.py
#
# @author Alexandros Lattas
#
# created with Spyder
#

#imports
import argparse
import collections
import csv
import itertools

#argument handling

parser = argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numeric", help="items are numeric",
                    action="store_true", default=False)
parser.add_argument("-p", "--percentage", action="store_true",
                    default=False, 
                    help="treat support threshold as percentage value")
parser.add_argument("-o", "--output", type=str, help="output file")
parser.add_argument("support", help="support threshold")
parser.add_argument("filename", help="input filename")

args = parser.parse_args()



#CSV Handling

input_file = open(args.filename, 'r')
csv_reader = csv.reader(input_file, delimiter=',')

csv_form = []

for row in csv_reader:
    lc = set([field.strip().lower() for field in row])
    csv_form.append(lc)

# initial
    
k = 0

# percentage handling

if args.percentage:
    support = int(len(csv_form) * int(args.support) / 100)
else:
    support = int(args.support)

# first a_priori

counts = {}

for basket in csv_form:
    for item in basket:
        if args.numeric:
            item = int(item)
        counts[item] = 0

freq = {}
freq[k] = {}

for basket in csv_form:
    for item in basket:
        if args.numeric:
            item = int(item)
        counts[item] = counts[item] + 1
        
for name in counts:
    if counts[name] >= support:
        
        freq[k][name] = counts[name]

k = 1

# a_priori def

def in_basket(inpair, inbasket):
    """Check if pair is in basket"""
    flag = 1
    for item in inpair:
        if not str(item) in inbasket:
            flag = 0
    return flag
   
def apriori(infreq, csv_form):
    """A Priori algorith for others"""
    counts = {}
    freqs = {}
    mono = []
    for item in infreq:
        mono.append(item)
    pairs = list(itertools.combinations(mono, 2))
    
    rpairs = []
    for pair in pairs:
        
        if isinstance(pair[0], collections.Iterable):        
            a = set(pair[0])
        else:
            aa = [pair[0], pair[0]]
            a = set(aa)
        if isinstance(pair[1], collections.Iterable):        
            b = set(pair[1])
        else:
            bb = [pair[1], pair[1]]
            b = set(bb)
        c = a | b
        rpairs.append(c)
    
    candidates = []
    for pair in rpairs:

        if not pair in candidates:
            candidates.append(pair)
            if len(pair) == (k + 1):
                counts[tuple(pair)] = 0  
                
    for basket in csv_form:   
        candidates2 = []
        for pair in rpairs:
            candidate = set(pair)
            if not candidate in candidates2:
                candidates2.append(candidate)
                if len(candidate) == (k + 1) and in_basket(pair,basket):
                    counts[tuple(pair)] = counts[tuple(pair)] + 1
                    
    for itemset in counts:
        if counts[itemset] >= support:
            freqs[itemset] = counts[itemset]
            
    return freqs
         
    
     
#Running Next a_prioris

while len(freq[k-1]) != 0:
    freq[k] = apriori(freq[k-1], csv_form)
    k = k + 1

# Printing

freq_out = [[] for d in range(k)]
for c in freq:
    freq_out[c] = list(freq[c])

if args.output:
    output_file = open(args.output, 'w')
    csv_writter = csv.writer(output_file, delimiter=';')
    kk = 0
    for row in freq_out:
        temp_row = []
        for i in range(len(row)):
            temp_str = ''.join([str(row[i]),':',str(freq[kk][row[i]])])
            temp_row.append(temp_str) 
        csv_writter.writerow(temp_row)
        kk = kk + 1
    output_file.close()
    print('file printed')
    
else:
    import sys
    csv_writter = csv.writer(sys.stdout, delimiter=';')
    kk = 0
    for row in freq_out:
        temp_row = []
        for i in range(len(row)):
            temp_str = ''.join([str(row[i]),':',str(freq[kk][row[i]])])
            temp_row.append(temp_str)
        csv_writter.writerow(temp_row)
        kk = kk + 1
