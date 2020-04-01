import csv
import math
import statistics

import numpy as np
from scipy import stats

# creating our lists
quantitySold = list()
prices = list()

# reading dataset.txt and populating our lists with data
with open('dataset.txt') as fd:
    rd = csv.DictReader(fd, delimiter='\t', quotechar='"')
    for row in rd:
        quantitySold.append(int(row['qntysold']))
        prices.append(int(row['price']))

# [a] max for quantity sold
print('Maximum quantity sold:', max([q for q in quantitySold]))

# [b] min for quantity sold
print('Minimum quantity sold:', min([q for q in quantitySold]))

# [c] finding mean for our data
print('Mean is: %.2f' % statistics.mean(prices))

# [c] standard deviation
print('Standard deviation: %.2f' % statistics.stdev(prices))

# we need these two values min/max for later calculations
minPrice = min([p for p in prices])
maxPrice = max([p for p in prices])

# [d] normalizing with max/min function from [10-20] using the formula
print('\nMin/Max normalization:')
for price in (prices[:3], prices[-3:]):
    for p in price:
        print(p, '%.2f' % ((p - minPrice) / (maxPrice - minPrice) * (20 - 10) + 10))

# [e] normalizing with Z-Score
print('\nZ-Score:')
print(stats.zscore(prices))

length = len(str(maxPrice))

# [f] decimal scaling normalization
# using formula to find the values
print('\nDecimal scaling:')
for price in (prices[:3], prices[-3:]):
    for p in price:
        print(p, float(p) / pow(10, length))

# [g] finding percentile for 25 and 75 of quantity sold
p25 = np.percentile(quantitySold, 25)
median = np.percentile(quantitySold, 50)
p75 = np.percentile(quantitySold, 75)
print('\nPercentile 25 is: %i, Median is: %i, Percentile 75 is: %i' % (p25, median, p75))

"""

    SECOND EXERCISE

"""


firstFile = None
secondFile = None

# opening first file
with open('paper1.txt') as file:
    firstFile = file.read().split()

# opening second file
with open('paper2.txt') as file:
    secondFile = file.read().split()


# jaccard similarity
def jaccardSimilarity(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


# function returns a number, how similar are the two given dictionaries
def cosine_dic(dic1, dic2):
    numerator = 0
    dena = 0
    for key1, val1 in dic1.items():
        numerator += val1 * dic2.get(key1, 0.0)
        dena += (val1 * val1)
    denb = 0
    for val2 in dic2.values():
        denb += (val2 * val2)

    return numerator / math.sqrt(dena * denb)


# function returns a dictionary of given input
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))


firstSetOfWords = set(firstFile)
secondSetOfWords = set(secondFile)
firstDic = wordListToFreqDict(firstFile)
secondDic = wordListToFreqDict(secondFile)


# using jaccard similarity
print('\nFiles are about %.2f%% similar (Jaccard).' % (jaccardSimilarity(firstSetOfWords, secondSetOfWords) * 100))
# using cosine similarity
print('Files are about %.2f%% similar (Cosine).' % (cosine_dic(firstDic, secondDic) * 100))

print('\nDONE')
