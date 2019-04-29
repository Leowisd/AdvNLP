# Yifu Yao
# 4/12/2019
# items in meshNumberList are term numbers
# numbers[item] is the term name of current term number
# parentDic[item] are all Ancestors of current term
# childrenDic[item] are direct children of current term
import re
import os
import copy
import treeModel

terms = {}
numbers = {}
 
meshFile = 'E:\WorkPlace\AdvNLP\d2019.bin'  #path of input file need to be defined
with open(meshFile, mode='rb') as file:
    mesh = file.readlines()
 
outputFile = open('E:\WorkPlace\AdvNLP\mesh.txt', 'w')  #path of output file need to be defined
 
for line in mesh:
    meshTerm = re.search(b'MH = (.+)$', line)
    if meshTerm:
        term = meshTerm.group(1).strip()
    meshNumber = re.search(b'MN = (.+)$', line)
    if meshNumber:
        number = meshNumber.group(1).strip()
        numbers[number.decode('utf-8')] = term.decode('utf-8')
        if term in terms:
            terms[term] = terms[term] + ' ' + number.decode('utf-8')
        else:
            terms[term] = number.decode('utf-8')
 
meshNumberList = []
meshTermList = terms.keys()
for term in meshTermList:
    item_list = terms[term].split(' ')
    for phrase in item_list:
        meshNumberList.append(phrase)
 
meshNumberList.sort()
 
used_items = set()
parentDic = {}
childrenDic = {}
for item in meshNumberList:   
    list = []
    list2 = []
    parentList = item.split('.')
    parent = ''
    if len(parentList) != 1:
        for itr in parentList:
            if parent == '':
                parent += itr
            else:
                parent += '.' + itr           
            if parent != item:
                list.append(parent)           
        if len(list) > 0:
            if list[len(list) - 1] in childrenDic:
               list2 = copy.deepcopy(childrenDic[list[len(list) - 1]])
            list2.append(item)
            childrenDic[list[len(list) - 1]] = copy.deepcopy(list2)
        parentDic[item] = copy.deepcopy(list)


# OUTPUT
# items in meshNumberList are term numbers
# numbers[item] is the term name of current term number
# parentDic[item] are all Ancestors of current term
# childrenDic[item] are direct children of current term
root = treeModel.Node(None, 'MeSH')
for item in meshNumberList:
    if numbers[item] not in used_items:
        print(file = outputFile)

        print(numbers[item], '\n', item, file=outputFile)
        
        print('Ancestors:', file=outputFile)
        if item in parentDic:
            print(parentDic[item], file = outputFile)
        else:
            newNode = treeModel.Node(root, item)
            root.children_list.append(newNode)
            print('No Ancestors', file = outputFile)
        
        print('children:', file=outputFile)
        if item in childrenDic:
            print(childrenDic[item], file = outputFile)
        else:
            print('No children', file = outputFile)

        used_items.add(numbers[item])
    else:
        print(item, file=outputFile)
        
        print('Ancestors:', file=outputFile)
        if item in parentDic:
            print(parentDic[item], file = outputFile)
        else:
            print('No Ancestors', file = outputFile)

        print('children:', file = outputFile)
        if item in childrenDic:
            print(childrenDic[item], file = outputFile)
        else:
            print('No children', file = outputFile)

# Store in a tree class
def buildTree(node):
    if node.node_name in childrenDic:
        for childNode in childrenDic[node.node_name]:
            newNode = treeModel.Node(node, childNode)
            node.children_list.append(newNode)
            buildTree(newNode)

def changeName(node):
    meshTree.node_list.append(node)
    node.node_name = numbers[node.node_name]
    if len(node.children_list) == 0:
        return
    for child in node.children_list:
        changeName(child)

meshTree = treeModel.Tree(root)
for node in meshTree.root.children_list:
    buildTree(node)
    changeName(node)

# print(meshTree.tree_dfs('Proteinase Inhibitory Proteins, Secretory'))
print()