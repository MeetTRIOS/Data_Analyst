#Fibonacci series
a=0
b=1

n=int(input("Enter a num:"))
if n ==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

#2.Prime Number
# n=int(input("Enter a number: "))
# if n<=1:
#     print("Not a prime number:")
# else:
#     for i in range (2,n):
#         if n%i==0:
#             print("The number is not prime:")
#             break
#     else:
#             print(f"The number is prime: {n}")

#3. Function to check if a number is a palindrome
# def is_palindrome(num):
#     # Convert the number to a string
#     num_str = str(num)
#
#     # Compare the string with its reverse
#     if num_str == num_str[::-1]:
#         return True
#     else:
#         return False
#
#
# # Input from user
# number = int(input("Enter a number: "))
#
# # Check if the number is a palindrome
# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")

#-------------------------------------------------------

#a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
#1.Write a program to separate the string into coma(,).

# a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b=a.split(".")
# print(b)

#2. Write a program to sort strings alphabetically in python.

# a= input("Please enter here: ")
# b=sorted(a)
# print(b)

#Write a program to remove a given character from string.
# a="hello"
# b=a.replace("e","")
# print(b)

#write a program to remove dot(.) from the following string.
# z="F.R.I.E.N.D.S."
# m=z.replace(".","")
# print(m)

#Write a program to check the number of occurrence of a substring in a string.
a="she sells seashells on the sea shore"
b=a.count("sea")
print(b)
