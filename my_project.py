import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password",
                               database="railway")  # connecting the database and python
mycursor = mydb.cursor()


# tablename = 'reservedseats'


# RESERVATION
def reserve():
    train_name = input("Enter train  name:")
    train_no = int(input("Enter train number:"))

    if str(train_name) == "Ato1i" and str(train_no) == "12345":
        booking_func("Ato1i", 12345)
    elif str(train_name) == "Ato1ii" and str(train_no) == "12346":
        booking_func("Ato1ii", 12346)
    elif str(train_name) == "Ato1iii" and str(train_no) == "12347":
        booking_func("Ato1iii", 12347)

    elif str(train_name) == "Ato2i" and str(train_no) == "12348":
        booking_func("Ato2i", 12348)
    elif str(train_name) == "Ato2ii" and str(train_no) == "12349":
        booking_func("Ato2ii", 12349)
    elif str(train_name) == "Ato2iii" and str(train_no) == "12350":
        booking_func("Atoiii", 12350)

    elif str(train_name) == "Ato3i" and str(train_no) == "12351":
        booking_func("Ato1ii", 12351)
    elif str(train_name) == "Ato3ii" and str(train_no) == "12352":
        booking_func("Ato1ii", 12352)
    elif str(train_name) == "Ato3iii" and str(train_no) == "12353":
        booking_func("Ato1iii", 12353)

    elif str(train_name) == "Bto1i" and str(train_no) == "12354":
        booking_func("Bto1i", 12354)
    elif str(train_name) == "Bto1ii" and str(train_no) == "12355":
        booking_func("Bto1ii", 12355)
    elif str(train_name) == "Bto1iii" and str(train_no) == "12356":
        booking_func("Bto1iii", 12356)

    elif str(train_name) == "Bto2i" and str(train_no) == "12357":
        booking_func("Bto2i", 12357)
    elif str(train_name) == "Bto2ii" and str(train_no) == "12358":
        booking_func("Btoii", 12358)
    elif str(train_name) == "Bto2iii" and str(train_no) == "12359":
        booking_func("Bto2iii", 12359)

    elif str(train_name) == "Bto3i" and str(train_no) == "12360":
        booking_func("Bto3i", 12360)
    elif str(train_name) == "Bto3ii" and str(train_no) == "12361":
        booking_func("Bto3ii", 12361)
    elif str(train_name) == "Bto3iii" and str(train_no) == "12362":
        booking_func("Bto3iii", 12362)

    elif str(train_name) == "Cto1i" and str(train_no) == "12363":
        booking_func("Cto1i", 12363)
    elif str(train_name) == "Cto1ii" and str(train_no) == "12364":
        booking_func("Cto1ii", 12364)
    elif str(train_name) == "Cto1iii" and str(train_no) == "12365":
        booking_func("Cto1iii", 12365)

    elif str(train_name) == "Cto2i" and str(train_no) == "12366":
        booking_func("Cto2i", 12366)
    elif str(train_name) == "Cto2ii" and str(train_no) == "12367":
        booking_func("Cto2ii", 12367)
    elif str(train_name) == "Cto1ii" and str(train_no) == "12368":
        booking_func("Cto2iii", 12368)

    elif str(train_name) == "Cto3i" and str(train_no) == "12369":
        booking_func("Cto3i", 12369)
    elif str(train_name) == "Cto3ii" and str(train_no) == "12370":
        booking_func("Cto3ii", 12370)
    elif str(train_name) == "Cto3iii" and str(train_no) == "12371":
        booking_func("Cto3iii", 12371)
    else:
        typeerror()
    print()
    print()


# CANCELLATION
def cancel():
    ticket_no = str(input("Enter your ticket number:"))
    print()
    mycursor.execute("DELETE FROM reservedseats where ticket_no = %s ", (ticket_no,))

    mydb.commit()
    print(mycursor.rowcount, "records deleted")
    if mycursor.rowcount == 0:
        print("Your ticket has not been cancelled yet!!")
        print()
    else:
        print("Your ticket is been cancelled!!")
        print()


# UPDATE IN DATABASE
def booking_func(train_name, train_no):
    passenger_name = input("Enter passenger name:")
    ticket_no = random.randint(111, 999)  # append passenger name in table
    values = (passenger_name, train_no, ticket_no, train_name)
    statement = "insert into reservedseats values( %s, %s, %s, %s)"
    mycursor.execute(statement, values)
    mydb.commit()
    print("Your ticket number is:", ticket_no)
    print()
    print(mycursor.rowcount, "ticket booked successfully")


# POSSIBLE DEPARTURES
def poss_departure():
    print("Choose your departure location from the following: ")
    print("A    B    C")


# POSSIBLE DESTINATIONS
def poss_destination():
    print("Choose your destination location from the following: ")
    print("1    2    3")


# POSSIBLE TRAINS FROM DEPARTURE TO DESTINATION
def poss_trains():
    poss_departure()
    print()
    poss_destination()
    print()
    dept = input("What is your departure location?  ").lower()
    dest = input("What is your destination location? ")
    if str(dept) == "a" and str(dest) == "1":
        print("The possible trains are:")
        print("1.Ato1i-->12345")
        print("2.Ato1ii-->12346")
        print("3.Ato1iii-->12347")
        print()
    elif str(dept) == "a" and str(dest) == "2":
        print("The possible trains are:")
        print("1.Ato2i-->12348")
        print("2.Ato2ii-->12349")
        print("3.Ato2iii-->12350")
        print()
    elif str(dept) == "a" and str(dest) == "3":
        print("The possible trains are:")
        print("1.Ato3i-->12351")
        print("2.Ato3ii-->12352")
        print("3.Ato3iii-->12353")
        print()
    elif str(dept) == "b" and str(dest) == "1":
        print("The possible trains are:")
        print("1.Bto1i-->12354")
        print("2.Bto1ii-->12355")
        print("3.Bto1iii-->12356")
        print()
    elif str(dept) == "b" and str(dest) == "2":
        print("The possible trains are:")
        print("1.Bto2i-->12357")
        print("2.Bto2ii-->12358")
        print("3.Bto2iii-->12359")
        print()
    elif str(dept) == "b" and str(dest) == "3":
        print("The possible trains are:")
        print("1.Bto3i-->12360")
        print("2.Bto3ii-->12361")
        print("3.Bto3iii-->12362")
        print()
    elif str(dept) == "c" and str(dest) == "1":
        print("The possible trains are:")
        print("1.Cto1i-->12363")
        print("2.Cto1ii-->12364")
        print("3.Cto1iii-->12365")
        print()
    elif str(dept) == "c" and str(dest) == "2":
        print("The possible trains are:")
        print("1.Cto2i-->12366")
        print("2.Cto2ii-->12367")
        print("3.Cto2iii-->12368")
        print()
    elif str(dept) == "c" and str(dest) == "3":
        print("The possible trains are:")
        print("1.Cto3i-->12369")
        print("2.Cto3ii-->12370")
        print("3.Cto3iii-->12371")
        print()
    else:
        typeerror()



# MAIN FUNCTION
def reservationMenu():
    while 1:
        print("This website can be used for:")
        print("1.RESERVATION (one ticket at a time)")
        print("2.CANCELLATION (one ticket at a time)")
        print("3.EXIT APPLICATION")
        print()

        choice = input(
            "What do you want to use the website for ?(Mention only the number written along your choice):  ")
        print()
        if choice == "1":
            poss_trains()
            reserve()
            mydb.close()
        elif choice == "2":
            cancel()
            mydb.close()
        elif choice == '3':
            print("Exiting")
            print("Have a safe journey!")
            break
        else:
            typeerror()
            break
        print("==================================================")


def typeerror():
    raise TypeError("This is not the right character. Please enter value as asked!")

reservationMenu()