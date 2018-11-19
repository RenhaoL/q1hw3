import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = open('all_reads.txt', 'r')

contigs = file.readlines()


length_less_50kb = []
length_more_50kb = []

for i in contigs:
    if len(i) >= 50000:
        length_more_50kb.append(len(i))
    else:
        length_less_50kb.append(len(i))


'''
Plot the histogram. 
Each green line on the bottom of the histogram represents each value from the data. 
'''

sns.set()
sns.set_context("notebook")
ax = sns.distplot(length_more_50kb, rug_kws={"color": "g"}, bins=20, kde = False, rug = True)
ax.set(xlabel = "Read Length (bp)", ylabel = 'Counts')
ax.set_title("Experimental Reads >50kb")
plt.show()


sns.set()
sns.set_context("notebook")
ax = sns.distplot(length_less_50kb, rug_kws={"color": "g"}, bins=20, kde = False, rug = True)
ax.set(xlabel = "Read Length (bp)", ylabel = 'Counts')
ax.set_title("Experimental Reads <50kb")
plt.show()
