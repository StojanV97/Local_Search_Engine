'''
Created on Jun 20, 2017

@author: vStojan
'''
from Tkconstants import CURRENT
from multiprocessing.process import _current_process

class Node(object):
    def __init__(self, label=None, data=None,link= None):
        self.label = label
        self.data = data
        self.children = {}
        self.link_recnik = {}
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key
    
    def __getitem__(self, key):
        return self.children[key]


class Trie(object):
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, key):
        return self.head.children[key]
   
    def add(self, word,link):
        current_node = self.head
        word_finished = True    
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break
        
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1
        current_node.data = word
        if current_node.link_recnik.has_key(link):
            current_node.link_recnik[link] += 1
        else:
            current_node.link_recnik[link] = 1
                
        
    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string') 
        current_node = self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break

        if exists:
            if current_node.data == None:
                exists = False
        
        return exists
    
    def start_with_prefix(self, prefix):
        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')
        
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                return words
        
        if top_node == self.head:
            queue = [node for key, node in top_node.children.iteritems()]
        else:
            queue = [top_node]
        
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                words.append(current_node.data)
            queue = [node for key,node in current_node.children.iteritems()] + queue
        
        return words
    
    def getData(self, word):
        if not self.has_word(word):
            raise ValueError("Ne postoji rec!!!")
        current_node = self.head
        for letter in word:
            current_node = current_node[letter]
        return current_node.data#,link
    
    def getLink(self,word):
        if  self.has_word(word):
            current_node = self.head
            for letter in word:
                current_node = current_node[letter]
            return current_node.link_recnik#,link
        else:
            print "Ne postojeca rec"
            
    
    
    
    
    
    
    