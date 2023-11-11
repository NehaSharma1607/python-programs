#program to get the largest no in the list
def max_num_in_list(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max
print(max_num_in_list([1,2,3,8,4,6,67]))