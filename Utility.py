def tupleToDict(tuple, keys):
    #tuple = (1,2,3)
    #keys = ['a', 'b', 'c']
    #half result = [ ('a', 1), ('b', 2), ('c', 3) ]

    tuplesList = []
    for i in range (0, min(len(tuple), len(keys))):
        tuplesList.append( (keys[i], tuple[i]) )

    return dict(tuplesList)

def inRange(lower, x, upper, inclusivity):
    if inclusivity:
        return lower <= x and x <= upper
    else:
        return lower < x and x < upper