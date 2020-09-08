#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: anonymous
November 2019
'''

import matplotlib.pyplot as plt
import sys
import statistics

def main(file):
    #labels=[]
    q=[]
    for line in open(file):
        if line[0].isnumeric(): #ignore all the lines which do not contain the taxa
            data = line.split()
            #labels.append(data[1]) #save ids
            q.append(float(data[3])) #save q-residuals
    #print summary statistics
    print('Median :', str(statistics.median(q)), 'Sd :', str(statistics.stdev(q)), ' Max :', str(max(q)), ' Min :',
          str(min(q)))
    labels = ['Siciliano_Ragusa', 'Siciliano_Mussomeli', 'Calabrese_Southern', 'Salentino',
              'Calabrese_Northern', 'Barese', 'Campano', 'Teramano', 'Casalasco', 'Reggio_Emilia', 'Parma',
              'Italian', 'Spanish', 'French', 'Portuguese', 'Romanian', 'Salento_Greek', 'Greek_Calabria_1',
              'Greek_Calabria_2', 'Greek', 'Greek_Cypriot', 'English', 'Dutch', 'Afrikaans', 'German', 'Danish',
              'Icelandic', 'Faroese', 'Norwegian', 'Bulgarian', 'Serbo-Croatian', 'Slovenian', 'Polish', 'Russian',
              'Irish', 'Welsh', 'Marathi', 'Hindi', 'Pashto', 'Tamil', 'Telugu', 'Mandarin', 'Cantonese', 'Japanese',
              'Korean', 'Hungarian', 'Khanty_1', 'Khanty_2', 'Estonian', 'Finnish', 'Mari_1', 'Mari_1','Udmurt_1','Udmurt_2',
              'Yukaghir', 'Even_1', 'Even_2',
              'Evenki', 'Yakut', 'Uzbek', 'Kazakh', 'Kirghiz', 'Turkish', 'Buryat', 'Basque_Central', 'Basque_Western',
              'Malagasy', 'Archi', 'Lak']
    print(len(labels), len(q))
    plt.bar(labels, q, color='red')
    plt.xticks(rotation='vertical', fontsize=8)
    plt.title('Q-residuals')
    plt.xlabel('Languages')
    plt.ylabel('Q')
    plt.ylim(0,0.2) #specify y axis interval
    plt.subplots_adjust(top=0.9, bottom=0.4)
    plt.show()
    for tuple in sorted(zip(q,labels), reverse=True):
        print(tuple[0], '\t', tuple[1])

if __name__ == '__main__':
    main(sys.argv[1])