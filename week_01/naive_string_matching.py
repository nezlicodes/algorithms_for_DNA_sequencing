def readGenome(fasta):
    genome = ''
    with open(fasta, 'r') as f :
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    
    return genome

genome = readGenome('phix.fa');
print(genome[:49])

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
          occurrences.append(i)
    return occurrences
t = 'TGGCCTGATTTT'
p = 'GG'

print(naive(p,t))

