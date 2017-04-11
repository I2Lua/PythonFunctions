def Del(thelist, element=-1):
    if element == -1:
        thelist.pop(-1)
    else:
        thelist.pop(element)
    return thelist

a = [1,2,3,4]
print(Del(a,2))