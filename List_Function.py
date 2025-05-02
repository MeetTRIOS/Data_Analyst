# a=["Thor","Hulk","Ironman","Captain America"]
#To find the length of a list
# print(len(a))

#To count an Occurrence of a particular element
# print(a.count("Thor"))

#To add to the list
# a.append("meet")
# print(a)

#To add to a specific location
# a.insert(1,"Vision")
# print(a)

#To remove from a list
# a.remove("Hulk")
# print(a)

#To remove from a certain location
# print(a.pop(1))
# print(a)

#List Function part (2)
a=["Thor","Hulk","Ironman","Captain America"]
#1.to create a copy of list
#
# b=[]
# print(b)
# b=a.copy() # to understand the b list empty and first before copying the list a
# print(b)

#2.To access an element
# print(a.index("Ironman")) #Basically to know the index of element:

#3.To extend the list:
# c=["Meet","Japan"]
# a.extend(c)
# print(a)

#4. To reverse the list
# print(a[::-1]) # This is slicing methode.
#
# a.reverse() #Using Function Methode.
# print(a)

#5. To sort the list
# a.sort() # Sort means ascending order
# print(a)
# a.sort(reverse=True)  # Sorts the list in descending order
# print(a)

#5. To clear all the list:
a.clear()
print(a)
