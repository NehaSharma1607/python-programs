# program to print the float nos. with no decimal points
x = float(input("enter the the no. with decimal:"))
print("original number:", x)
print("formatted no. with n decimal places: " + "{:.0f}".format(x))