'''
Created on Jun 28, 2017

@author: vStojan
'''

class Item(object):
    __slots__ = 'key', 'value'

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + self.key + ', ' + self.value + ')'

def bucket_sort(S):
    length = len(S)
    Bucket = {}
    for item in S:
        k = item.key
        S.remove(item)
        Bucket[k].append(item)
    for i in xrange(length):
        for item in Bucket[i]:
            Bucket[i].remove(item)
            S.append(item)
    return S