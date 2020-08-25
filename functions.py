def compare(a, b):
    if a < b:
        res = -1
    elif a > b:
        res = 1
    else:
        res = 0
    return res

def binarySearch(l, searched , comp=compare, a=0, b=None):
    """
    parameters
    ----------
    l: (list) a sorted list, elements in increasing order
    searched: (any) the searched element
    a, b: (int) part of the list to be used for searching
    comp: (function) the comparison function used for comparing l's elements

    Usage constraints
    -----------------
     a >= 0, b <= length of l
     
    return
    ------
    (int) if <searched> is in l[a:b], the smallest index where <searched> can be found, else -1
    """
    if b == None:
        b = len(l)
    beg = a
    end = b
    found = False
    res = -1
    while not found:
        m = (beg + end) // 2 # does a <= m <= b-1 ?
        c = comp(searched, l[m])
        if c < 0:
            end = m - 1
        elif c > 0:
            beg = m + 1
        else: 
            res = m
            found = True
    return res

def minIndex(l, a=0, b= None, comp=compare):
    """
    parameters
    ---------
    l: (list)
    a, b: (int)
    comp: (function) the comparison function used for comparing l's elements

    UC: l is not empty
    return 
    ------
    (int) index of the minimum element in l[a:b] using comp
    """
    if b == None:
        b = len(l)
    i = a + 1
    res = a
    while i < b:
        if comp(l[res], l[i]) > 0:
            res = i
        i += 1
    return res    

def swap(l, a, b):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp

def selectionSort(l, comp=compare):
    """
    parameters
    ----------
    l: (list)
    comp: (function) the comparison function used for comparing l's elements

    side effects
    ------------
    l will be sorted
    """
    length = len(l)
    for i in range(0, len(l)-1):
        indMin = minIndex(l, a=i, b=length, comp=comp)
        swap(l, i, indMin)


def insert(l, a, comp=compare):
    """
    parameters
    ----------
    l: (list)
    a: (int) index of the element to be inserted
    comp: (function) the comparison function used for comparing l's elements

    Usage constraints
    -----------------
    l[0:a] is supposed to be sorted increasingly
    length of f > a 

    side effects
    ------------
    l[0:a+1] is sorted increasingly
    """ 
    ins = l[a]
    i = a - 1   
    while i >= 0 and comp(l[i], ins) > 0:
        l[i+1] = l[i]
        i = i - 1
    l[i+1] = ins

def insertionSort(l, comp=compare):
    """
    parameters
    ----------
    l: (list) list to be sorted
    comp: (function) the comparison function used for comparing l's elements 
    """
    for i in range(1, len(l)):
        insert(l, i, comp=comp)

if __name__ == "__main__":
    from random import randint, shuffle
    l = [x for x in range(10)]
    shuffle(l)
    print(l)
    insertionSort(l)
    print(l)