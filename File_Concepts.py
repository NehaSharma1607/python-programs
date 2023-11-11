
my_file=open("data.txt","r")   #we wrote r here to indicate that we are going to read the file only and not write on it

file_content=my_file.read()

my_file.close()

print(file_content)

#when we write in the file it erases the data already present there
user_input=input("enter the name:")
my_file_writing=open("data.txt","w") # we wrote w here to indicate that we are writing in the file
my_file_writing.write(user_input)

my_file_writing.close()


#Ask the user for a list of 3 friends
#For each friend , we will tell the user if they are nearby
#For each friend nearby, we will save them in the file "nearby_friends"


#hint:readlines()

friends=input("enter the names of three friends separated with commas(no space please_):").split(",")
nearby_people=open("people.txt","r")
nearby_people_content=[line.strip() for line in nearby_people.readlines()]  # gives a list of names in the file per line
                         #.strip() removes the new line char from the start and the end
nearby_people.close()
friends_set=set(friends)
nearby_people_content_set=set(nearby_people_content)

friends_nearby_set=friends_set.intersection(nearby_people_content_set)
nearby_friends_file=open("Nearby_friends.txt","w")
for friend in friends_nearby_set:
    print(f'{friend} is nearby! meet up time.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()


