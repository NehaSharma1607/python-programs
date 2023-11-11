#function that takes two lists and returns true if at least one value in common in them
def commom_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
    return result
print(commom_data([1,2,3,4,5],[1,2,6,3,5,4]))