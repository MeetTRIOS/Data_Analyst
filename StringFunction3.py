#1.endswith() - return true if the string ends with specified value
# a="Harry Potter"
# print(a.endswith("r"))
# print(a.endswith("t",6,9))
from tkinter import PanedWindow
from unittest.mock import PropertyMock

#2.startswith() - return true if the string start with specified value
# print(a.startswith("H"))
# print(a.startswith("r",2,4))

#3.swap case() - swap cases, lower case becomes upper case and vice versa
# print(a.swapcase())

#4.strip() - Return a trimmed version of the string
# b="    my Name is Meet ******"
# print(b)
# print(b.strip(" , *"))

#5.split() - Split the string at the specified separator, and return a list
# a="#OTD#BRB#OMW#TB"
# b="hello.My name is meet.I am 22 years old."
# print(a.split("#"))
# print(b.split("."))

#6.ljust() - return a left justified version of the string
# a="Harry Potter"
# x=a.ljust(20,"x")
# print(x,"is my favorite movie.")

#7.rjust() - return a right justified version of the string
# x=a.rjust(40,"^")
# print(x)

#8.replace() - Return a string where a specified value is replacing with a specified value
# name="My name is Meet"
# print(name.replace("Meet","Japan"))

#9.rindex() - Searches the string for a specified value and return
a="Harry Potter and the Prisoner of a Azkaban"
# print(a.rindex("and"))
#the last position of where it was found
# print(a.rfind("and"))
print(a.rfind("o",9,16))