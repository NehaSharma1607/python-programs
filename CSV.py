import csv
'''
with open("myfile.csv") as csvfile:
    myreader=csv.reader(csvfile,delimiter=",")
    count=0
    print("EMPNO","EMP NAME","SALARY")
    print("=======")
    for row in myreader:
        print(row[0],row[1],row[2])
        count+=1
    print("================")
    print("total records:",count)
    print("+++++++++")
'''
'''

with open("myfile.csv",mode="a") as csvfile:
    mywriter =csv.writer(csvfile,delimiter=",")
    ans="y"
    while ans.lower()=="y":
        eno=int(input("enter employee no.:"))
        name=input("enter employee name:")
        salary=int(input("enter employee salary:"))
        mywriter.writerow([eno,name,salary])
        print("## data saved##")
        ans=input("add more:")

with  open("myfile.csv") as csvfile:
    myreader=csv.reader(csvfile,delimiter=",")
    ans="y"
    while ans.lower()=="y":
        found=False
        e=int(input("enter employee ti search:"))
        for row in myreader:
            if len(row)!=0:
                if int(row[0])==e:
                    print("========")
                    print("name:",row[1])
                    print("salary:",row[2])
                    found=True
                    break
        if not found:
            print("========")
            print("emp not found")
            print("====")
        ans=input("search more:")
'''