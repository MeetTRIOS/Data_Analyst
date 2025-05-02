#1.Take an input from user as a string then , reverse it.

# a=input("Write something here: ")
# print(a[::-1])

#2.Write a program to check if a string contains only digits.
# a=input("Enter here: ")
# print(a.isdigit())  #It's give you only true if it's number else false

#3.Write a program to check if a string is a palindrome.
# a = input("Enter here: ")
# b = a[::-1]
# if a == b:
#     print(b + " is palindrome string")
# else:
#     print("Not Palindrome")

#4.Write a program to find number of vowels in string.
a = input("Enter here: ")
vowels=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
        vowels+=1
print(f'The number of vowels in string is {vowels}')
