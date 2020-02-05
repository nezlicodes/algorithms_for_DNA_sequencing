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
print(seqs)
