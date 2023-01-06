import pandas as pd
from math import log2

CLASS_ATTR = 'PlayTennis'
class Node:
    def __init__(self, label):
        self.label = label
        self.branch = dict()

def entropy(data):
    te = len(data)
    pe = len(data.loc[data[CLASS_ATTR] == 'Yes'])
    ne = te - pe
    en = 0
    if pe > 0:
        en -= (pe/te) * log2(pe/te)
    if ne > 0:
        en -= (ne/te) * log2(ne/te)
    return en

def gain(data, attr):
    gain = entropy(data)
    values = set(data[attr])
    for value in values:
        filter_data = data.loc[data[attr] == value]
        gain -= (len(filter_data)/len(data)) * entropy(filter_data)
    return gain

def get_attr(data):
    attr = ''
    max_gain = -float('inf')
    for col in data.columns[:-1]:
        cur_gain = gain(data, col)
        if cur_gain > max_gain:
            max_gain = cur_gain
            attr = col
    return attr

def decision_tree(data):
    pos = len(data.loc[data[CLASS_ATTR] == 'Yes'])
    if pos == len(data):
        return Node('Yes')
    if pos == 0:
        return Node('No')
    attr = get_attr(data)
    root = Node(attr)
    values = set(data[attr])
    for value in values:
        root.branch[value] = decision_tree(data.loc[data[attr] == value].drop(attr, axis=1))
    return root

def get_rules(root, rule = ''):
    if not root.branch:
        return [rule[:-1] + '=>' + root.label]
    rules = []
    for value in root.branch:
        rules += get_rules(root.branch[value], rule + root.label + '=' + value + '^')
    return rules

def test(root, test_str):
    if not root.branch:
        return root.label
    return test(root.branch[test_str[root.label]], test_str)

data = pd.read_csv('./tennis.csv')
tree = decision_tree(data)
rules = get_rules(tree)
print(rules)
test_str = dict()
print('Enter test data:')
for col in data.columns[:-1]:
    test_str[col] = input(col + ': ')
print(test_str)
print(test(tree, test_str))