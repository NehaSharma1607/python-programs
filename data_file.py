f=open("test.txt","w")
f.write("i am writing data to a text file \n")
f.write("hopefully it will be right \n")
print("data written to file successfully")
x=56
f.write(str(x))
list=["cs\n","maths\n","eng\n","hin"]
f.writelines(list)
print("list of lines written to the text file successfully")





f.close()