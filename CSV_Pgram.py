'''
file=open("Storage.txt","r")
lines=file.readlines()
file.close()
lines=[line.strip() for line in lines[1:]]
for line in lines:
    personal_data=line.split(",")
    name=personal_data[0].title()
    age=personal_data[1]
    university=personal_data[2].title()
    degree=personal_data[3].capitalize()

    print(f"{name}is{age},studying {degree} at {university}. ")
sample_csv_value=",".join(["neha",18,"iit","mechanical"])   #this is how to simply write the data
print(sample_csv_value)
'''

