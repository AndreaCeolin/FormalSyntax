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
    labels=[]
    d=[]
    for line in open(file):
        if line[0].isnumeric(): #ignore all the lines which do not contain the taxa
            data = line.split()
            labels.append(data[1]) #save ids
            d.append(float(data[2])) #save delta scores
    #print summary statistics
    print('Median :', str(statistics.median(d)), 'Sd :', str(statistics.stdev(d)), ' Max :', str(max(d)), ' Min :', str(min(d)))
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
    plt.bar(labels, d, color='blue')
    plt.xticks(rotation='vertical', fontsize=8)
    plt.title('Delta scores')
    plt.xlabel('Languages')
    plt.ylabel('Delta')
    plt.ylim(0,0.4) #specify y axis interval
    plt.subplots_adjust(top=0.9, bottom=0.4)
    plt.show()
    for tuple in sorted(zip(d,labels), reverse=True):
        print(tuple[0], '\t', tuple[1])

if __name__ == '__main__':
    main(sys.argv[1])