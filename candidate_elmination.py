import pandas as pd
import numpy as np
import csv
import pprint

concept = []
target = []
with open('./data.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        concept.append(line[:-1])
        target.append(line[-1])
    print('Concept: ', concept)
    print('Target: ', target)

def candidateElimination(concept, target):
    specific_h = concept[0]
    general_h = [['?' for i in range(len(specific_h))] for j in range(len(specific_h))]

    for k, h in enumerate(concept):
        if target[k] == 'Yes':
            for j in range(len(specific_h)):
                if h[j] != specific_h[j]:
                    specific_h[j] = '?'
                    general_h[j][j] = '?'
        else:
            for j in range(len(specific_h)):
                if h[j] != specific_h[j]:
                    general_h[j][j] = specific_h[j]
                else:
                    general_h[j][j] = '?'
    indices = [i for i in range(len(general_h)) if general_h[i] == ['?' for j in range(len(specific_h))]]
    for index in indices:
        general_h.remove(['?' for i in range(len(specific_h))])
    print(specific_h)
    print(general_h)

candidateElimination(concept, target)