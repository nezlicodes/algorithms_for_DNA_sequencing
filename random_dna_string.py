import random
complement = {'a': 't', 't':'a', 'c':'g', 'g':'c'}
seq = ''
complement_seq = ''

# Generate random DNA sequence
for _ in range(10):
    seq += random.choice('atcg')

# Generate Complementary strand
for i in range(len(seq)):
    complement_seq += complement[seq[i]]


print(seq)
print(complement_seq)
