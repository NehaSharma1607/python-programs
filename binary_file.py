def fOperation():
    import pickle
    list1=[10,20.30,40,50,60]
    f=open("list.txt","wb")
    pickle.dump(list1,f)
    print("list added to the binary file")
    f.close()
    f=open("list.txt","rb")
    list1=pickle.load(f)
    f.close()
    print(list1)


def binfile():
    import pickle
    file=open("data.dat","wb")
    while True:
        x=int(input("enter the integer:"))
        pickle.dump(x,file)
        ans=input("do you want to enetr more data Y/N:")
        if ans.upper()=="N": break
    file.close()
    file=open("data.dat","rb")
    try:
        while True:
            y=pickle.load(file)
            print(y)
    except EOFError:
        pass
    file.close()



import os
def filecopy(file1,file2):
    f1=open(file1,"r")
    f2=open(file2,"w")
    line=f1.readline()
    while line !=" ":
        f2.write(line)
        line=f1.readline()
    f1.close()
    f2.close()

def main():
    fileName1=input("enter the source file name:")
    fileName2=input("enter the destination file name:")
    filecopy(fileName1,fileName2)

if __name__=="__main__":
    main()
