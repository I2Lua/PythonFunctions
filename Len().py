def Len(thelist):
    i = 0
    while thelist != []:
        thelist.pop()
        i += 1
    return i

a = [] # Values
print(Len(a))