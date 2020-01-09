import collections;
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genome = readGenome('lambda_virus.fa')
print(len(genome))

# Base count
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for base in genome:
    counts[base] += 1

## OOOOR using collections
baseCounts = collections.Counter(genome);
print(baseCounts)
# Base frequency
for i in counts:
    print(i, counts[i]/len(genome))
