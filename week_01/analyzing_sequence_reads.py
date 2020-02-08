import matplotlib.pyplot as plt

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

seqs, quals = readFastq('SRR835775_1.first1000.fastq')
print(quals[:5])

def phred33ToQ(qual):
    return ord(qual) - 33

def createHist(qualities):
    hist = [0] * 50
    for read in qualities:
        for phred in read:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist
h = createHist(quals)
print(h)


plt.plot(range(len(h)), h)
plt.show()
