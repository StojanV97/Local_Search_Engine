'''
Created on Jun 21, 2017

@author: vStojan
'''

class Node(object):
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = {}
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key
    
    def __getitem__(self, key):
        return self.children[key]


