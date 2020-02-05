# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:10:29 2020

@author: Dell
"""


from reading_fasta_file import readGenome;
from manipulating_dna_strings import complementStrand;

genome = readGenome('lambda_virus.fa')
p = 'TTAA'

def findOccurences(p, t):
    pos = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            pos.append(i)
    return pos

## Number of occurences of ACCT or its reverse
total_acct = len(findOccurences('ACCT', genome)) + len(findOccurences(complementStrand('ACCT'), genome))

## Number of occurences of TTAA
total_ttaa = len(findOccurences('TTAA', genome))

# offset of the leftmost occurrence of ACTAAGT

lefmost_offset_actaagt = min(findOccurences('ACTAAGT', genome)[0], findOccurences(complementStrand('ACTAAGT'), genome)[0])
print(lefmost_offset_actaagt)

# offset of the leftmost occurence of AGTCGA
leftmost_offset_agttcga =  min(findOccurences('AGTCGA', genome)[0], findOccurences(complementStrand('AGTCGA'), genome)[0])
print(leftmost_offset_agttcga)