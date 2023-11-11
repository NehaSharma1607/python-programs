# Algorithm Comparison

import timeit

list1=[]
print("We have an empty list right now! Add numbers to it for sorting")
total_elements=int(input("How many numbers do you wish to enter? :"))
for i in range(0,total_elements):
    user_input=int(input("Enter a number to add to the list: "))
    list1.append(user_input)
print("Your original list is:", list1)
length=len(list1)


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def mergeSort(array):
    if len(array) > 1:
        r = len(array) // 2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
          i = i + 1
          (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


def execution_time():
    end_time = timeit.default_timer()
    print("the execution time is:",end_time)


def menu():
    print("WHICH SORTING ALGORITHMS DO YOU WANT TO START COMPARING WITH?")
    print("The algorithms available are:")
    print("1. Insertion Sort")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    sorting=int(input("From which algorithms do you want to start comparing?(1/2/3/4/5) :"))
    sorting_menu(sorting)


def sorting_menu(sorting):
        if sorting==1:
            insertionSort(list1)
            print("The sorted list is:",list1)
            execution_time()
            repeat()
        elif sorting==2:
            bubbleSort(list1)
            print("The sorted list is:",list1)
            execution_time()
            repeat()
        elif sorting==3:
            selectionSort(list1,length)
            print("The sorted list is:", list1)
            execution_time()
            repeat()
        elif sorting==4:
            mergeSort(list1)
            print("The sorted list is:", list1)
            execution_time()
            repeat()
        elif sorting==5:
            quickSort(list1,0,length-1)
            print("The sorted list is:", list1)
            execution_time()
            repeat()
        else:
            print(" Incorrect Input!!")


def repeat():
        next_choice=int(input(" Which algorithm to run next? "))
        if next_choice<=5:
            sorting_menu(next_choice)
        else:
            print("Incorrect input ")




menu()