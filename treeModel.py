class Node:
    father = None
    children_list = []
    node_name = None

    def __init__(self, father, word):
        self.father = father
        self.children_list = []        
        self.node_name = word
        return

# algorithm: travel through the tree and exploring the name
# of each nodes. choosing the node which paper_keywords contain at the next node.
# if none of the them is included, comparing tfidf vector distance between papers and calculating an average depth
# then create an new node as a child node at that level of tree

class Tree():
    root = None
    node_list = []
    flag = 0

    def __init__(self, root):
        self.root = root
        self.node_list = []
        return
    
    def merge(self):

        return

    def insert(self):

        return

    def search(self, node, paper_keywords):
        if (node.node_name == paper_keywords):
            self.flag = 1
            return
        if (len(node.children_list) > 0):
            for childNode in node.children_list:
                self.search(childNode, paper_keywords)
                if self.flag == 1:
                    return
        return

    def tree_dfs(self, paper_keywords):
        self.flag = 0
        self.search(self.root, paper_keywords)
        if (self.flag == 1):
            return True
        else:
            return False
