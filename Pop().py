def Pop(thelist, element=-1):
    if element == -1:
        i = 0
        while i != 1:
            del thelist[-1]
            i += 1
    else:
        del thelist[element]

    return thelist
a = [1,2,3]
print(Pop(a,1))