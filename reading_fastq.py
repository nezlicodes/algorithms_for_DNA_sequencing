def readFastq(filename):
    qualities = []
    sequences = []
    with open(filename, 'r') as f:
        while True:
            ## Reads the first line (corresponds to tag of seq, we don't care about it)
            f.readline();
            # Reads second line : Our read
            seq = f.readline().rstrip()
            # Just a placeholder line in the fastq file
            f.readline()
            # Quality bases line
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)

    return sequences, qualities

seqs, quals = readFastq('SRR835775_1.first1000.fastq')


def fred33ToQual(val):
    return ord(val) - 33

def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = fred33ToQual(phred)
            hist[q] += 1
    return hist

h = createHist(quals)
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()