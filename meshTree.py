import re
 
terms = {}
numbers = {}
 
meshFile = 'd2019.bin'
with open(meshFile, mode='rb') as file:
    mesh = file.readlines()
 
outputFile = open('mesh.txt', 'w')
 
for line in mesh:
    meshTerm = re.search(b'MH = (.+)$', line)
    if meshTerm:
        term = meshTerm.group(1)
    meshNumber = re.search(b'MN = (.+)$', line)
    if meshNumber:
        number = meshNumber.group(1)
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
for item in meshNumberList:
    list = []
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
        parentDic[item] = parent
            

    if numbers[item] not in used_items:
        print(numbers[item], '\n', item, file=outputFile)
        print('parent:\n', file=outputFile);
        if item in parentDic:
            print(parentDic[item], file = outputFile)
        used_items.add(numbers[item])
    else:
        print(item, file=outputFile)
        if item in parentDic:
            for itr in parentDic[item]:
                print(itr, file = outputFile)


# item is number of each phrase and
# numbers[item] is the term name of each number

# to do
# to complete a dic of parents of each term
# and children of each term
