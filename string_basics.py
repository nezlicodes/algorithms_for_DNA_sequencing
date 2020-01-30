# You can define a string using single or double quotes
seq1 = 'ACCCTGGGCTA'

# Get the length of a string
print(len(seq1))

#concatenate
seq2 = 'GcTT'
#A) using the + operator
print(seq1+seq2)
#B) using the join built-in function
seqs = ['A', 'C', 'T', 'G', 'G', 'T', 'C', 'C', 'C']
print(''.join(seqs))
print('-'.join(seqs))

#Create a random string of DNA sequences
import random
random_seq = ''

for i in range(10):
    random_seq += random.choice('ACGT')

print(random_seq)

#Another way of doing this is
seq = ''.join([random.choice('ACTG') for _ in range(10)])


#Substrings
seq[1:3]

#prefix
seq[:3]

#suffix
seq[-3:]
