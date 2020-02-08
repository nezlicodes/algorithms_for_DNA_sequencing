def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

print(longestCommonPrefix('ACCATG', 'ACCTGGG'))

def match(s1, s2):
    if not len(s1) == len(s2):
        return False
    for i in range(len(s2)):
        if not s1[i] == s2[i]:
            return False
    return True

#an even easier way:
'ATTGCT' == 'TCGGAG'

complement = {
    'A': 'T',
    'T': 'A',
    'C' :'G',
    'G': 'C'
}

def complementStrand(strand):
    complementStr = ''
    for base in strand:
        complementStr = complement[base] + complementStr
    return complementStr

print(complementStrand('ATGC'))


