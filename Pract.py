def fun(ob):
    long=''
    c=0
    sum=0
    for i in ob:
        c=c+1
        sum=sum+c
    print(c)
    if(len(i)>len(long)):
        long=i
        print(long,"longest line", len(long))
    print(sum)
    ob.close()
ob1=open("test.txt","r")
fun(ob1)
