'''
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="neha",passwd="neha",database="school")
mycursor = mydb.cursor()
mycursor.execute("insert into 12a values('payal',15,07032004),('anjana',15,28042003)")
mydb.commit()
print(mycursor.rowcount,"record inserted")
mycursor.close()
'''
'''
from collections import deque

arr=[]
elements=int(input("enter the no. elements of list:"))
for i in range(0,elements):
    ele=int(input("enter the element:"))
    arr.append(ele)

def LShift(Arr,n):
    print(Arr)
    a=deque(Arr)
    a.rotate(-n)
    print(a)

LShift(arr,2)

lst=[1,2,3,4,5]
n=int(input("Enter the no. of elements to be shifted:"))
def shift(arr,n):
    for i in arr[0:n]:
        arr.remove(i)
        arr.insert(len(arr),i)
    print(arr)
if n<=len(lst):
    shift(lst,n)
else:
    print("no. of elemets to be shifted are exceeding the no. of elements in list")

'''

'''
import random
help(random)
PNR=[ ]
if len(PNR)<=10:
    pnr=random.randint(0,11)
    print(pnr)
else:
    None
'''
import timeit
start_time = timeit.default_timer
list1=[186,189,6,1896,1686531,45,465,64654,54654,58,4,685,7,56,54,68,68653,26485,69,68,678,786,76,876,78,78852,8528,96,741,96,858,57,858,5]
def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
selectionSort(list1,len(list1))
print(list1)
end_time = timeit.default_timer()
#elapsed_time = end_time - start_time
#print ("Code execution time in seconds is ",elapsed_time)
#elapsed_time_milliSeconds = elapsed_time*1000
#print("code elapsed time in milliseconds is ",elapsed_time_milliSeconds)
print(end_time)