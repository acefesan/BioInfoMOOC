import numpy as np
import matplotlib.pyplot as plt
from itertools import product




def median_string(k, DNAs):
    bases = ['A','C','G','T']
    median = ''
    score = float('inf')
    for prod in product(bases, repeat=k):
        pattern = ''
        for b in prod:
            pattern += b
        tmp_score = 0
        for dna in DNAs:
            min_distance = float('inf')
            for i in range(len(dna)-len(pattern)):
                if hammingDistance(pattern,dna[i:i+k]) < min_distance:
                    min_distance =  hammingDistance(pattern,dna[i:i+k])
            tmp_score += min_distance
        if tmp_score < score:
            score = tmp_score
            median = pattern
    return median


basePair = {'A':0,'C':1,'G':2,'T':3}



def hammingDistance(DNA1,DNA2):
    dist = 0
    for n,k in zip(DNA1,DNA2):
        if n != k:
            dist += 1

    return dist

def probabilityForPattern(profileMatrix,pattern):
    prob = 1
    for n,i in zip(pattern,range(len(pattern))):
        prob *= profileMatrix[basePair[n],i]
    return prob

def parseProfileMatrix(k,numbers):
    return np.resize(np.array(numbers),(4,k))

def maxProbPattern(matrix,dna,k):
    max_pattern_score =0
    max_pattern = ''
    for i in range(0,len(dna)-k,1):
        pattern = dna[i:i+k]
        prob = probabilityForPattern(matrix,pattern)
        if prob > max_pattern_score:
            max_pattern = pattern
            max_pattern_score = prob
    return max_pattern


def constructProfile(Motifs,k):
    charMatrix = np.array(Motifs,(t,k))
    profile = np.zeros((4,k))
    for i in range(k):
        profile[i] = np.count(charMatrix == 'A',axis = 1)


def greedyMotiveSearch(k,t,DNAs):


f  = open('BioInformatics1/Week3/dataset_159_3.txt')
f = f.readlines()
dna = f[0]
k = int(f[1])
numbers = [float(x) for line in f[2:] for x in line.strip().split(' ') ]
matrix = createProfileMatrix(k,numbers)
print(maxProbPattern(matrix,dna,k))
