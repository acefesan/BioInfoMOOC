import numpy as np
import matplotlib.pyplot as plt

def computeSkew(DNA):
    skew = np.zeros(len(DNA))
    for i in range(1,len(DNA),1):
        if DNA[i-1] == 'G':
            skew[i] = skew[i-1]+1
        elif DNA[i-1] == 'C':
            skew[i] = skew[i-1]-1
        else:
            skew[i] = skew[i-1]
    return skew

def plotSkew(DNA):
    skew = computeSkew(DNA)
    plt.plot(np.arange(skew.shape[0]),skew)
    plt.show()


def findMinSkew(DNA):
    skew = computeSkew(DNA)
    min_vals = np.where(skew==skew.max())
    return min_vals[0]

def hammingDistance(DNA1,DNA2):
    dist = 0
    for n,k in zip(DNA1,DNA2):
        if n != k:
            dist += 1

    return dist

def approximatePatternMatchingProblem(kMer,DNA,d):
    ind = []
    for i in range(0,len(DNA)-len(kMer)+1,1):
        slc = DNA[i:i+len(kMer)-1]
        if hammingDistance(kMer,slc) <= d:
            ind.append(i)
    return ind

def approximatePatternCount(kMer,DNA,d):
    count = 0
    for i in range(0,len(DNA)-len(kMer)+1,1):
        slc = DNA[i:i+len(kMer)-1]
        if hammingDistance(kMer,slc) <= d:
            count+=1

    return count

def neighbors(kMer,d):
    if d == 0:
        return set([kMer])
    if len(kMer) == 1:
        return set(['A','C','G','T'])
    neighborhood = set()
    suffix_neighbors = neighbors(kMer[1:],d)
    for n in suffix_neighbors:
        if hammingDistance(kMer[1:],n) < d:
            for nc in ['A','C','G','T']:
                neighborhood.add(nc+n)
        else:
            neighborhood.add(kMer[0]+n)

    return neighborhood

def reverseComplement(DNA):
    rcomp = ""
    for n in DNA[::-1]:
        if n == 'G':
            rcomp+='C'
        elif n == 'C':
            rcomp+='G'
        elif n == 'A':
            rcomp+='T'
        elif n == 'T':
            rcomp+='A'
    return rcomp


def frequentWordsWithMissmatches(Text, k, d):
    n = len(Text)
    D = {}
    patterns = []
    for i in range(0,n-k,1):
        pattern = Text[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood:
            if neighbor in D:
                D[neighbor]+=1
            else:
                D[neighbor]=1
    m = max(D.values())
    for k in D:
        if D[k] == m:
            patterns.append(k)
    return patterns

def frequentWordsWithMissmatchesAndRComplements(Text, k, d):
    n = len(Text)
    D = {}
    patterns = []
    for i in range(0,n-k,1):
        pattern = Text[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood:
            rc = reverseComplement(neighbor)
            if neighbor in D:
                D[neighbor]+=1
            else:
                D[neighbor]=1
            if rc in D:
                D[rc] += 1
            else:
                D[rc] = 1
            
    m = max(D.values())
    for k in D:
        if D[k] == m:
            patterns.append(k)
    return patterns



f  = open('BioInformatics1/Week2/salmonela_enterica.txt')
f = f.readlines()

DNA = ""
for line in f:
    DNA += line

# plotSkew(DNA)
# minSkew = findMinSkew(DNA)[0]
# print(minSkew)
# print(frequentWordsWithMissmatches(DNA[minSkew-250:minSkew+250],9,1))

print(hammingDistance("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC","GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"))

print(findMinSkew("CATTCCAGTACTTCATGATGGCGTGAAGA"))



print(approximatePatternCount("TGT","CGTGACAGTGTATGGGCATCTTT",1))

print(len(neighbors("TGCAT",2)))

