import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main(graph_file):
    '''
    This function returns the cumulative of proportion and a list with all the length of reads.
    All those information are needed for the second graph.
    '''
    f = open(graph_file, 'r')
    contigs = f.readlines()
    all_length = []
    for i in contigs:
        all_length.append(len(i))
    total_contigs = sum(all_length)
    all_length = sorted(all_length)
    proportion = []
    for i in all_length:
        proportion.append(i/total_contigs)
    cum_proportion = []
    for i in range(len(proportion)):
        cum_proportion.append(sum(proportion[:i+1]))
    cum_proportion = sorted(cum_proportion)
    f.close()
    return cum_proportion, all_length


pro, length = main("all_reads.txt")
pro1, length1 = main('all_reference_r6.24.txt')

# print("1111",len(pro1), pro1)
# print('222', len(length1), length1)

if length[-1] < length1[-1]:
    length.append(length1[-1])
    pro.append(pro[-1])


def data_frame(list1, list2, list3, list4):
    '''
    create the dataframe for later use.
    '''
    if len(list1) != len(list2) or len(list3) != len(list4):
        return None
    prop = []
    prop.extend(list1)
    prop.extend(list3)
    total_length = []
    total_length.extend(list2)
    total_length.extend(list4)
    event = []
    for i in range(len(list1)):
        event.append('experimental')
    for i in range(len(list3)):
        event.append("reference")
    d = {"proportion": prop, 'read_length': total_length, 'legend': event}
    return pd.DataFrame(d)

'''
plot the line plot. 
'''
sns.set()
sns.set_context("notebook")
ax = sns.lineplot(x="read_length", y="proportion", hue = "legend", data=data_frame(pro, length, pro1, length1))
plt.show()