#num= list(range(6))
#print (num)
# adding " " makes it string while leaving it doesnt
#numbers=[1,2,3,4,5]
#print(numbers[0]+numbers[3])

#numbers = [10 ] * 5
#print(numbers)

# num=[1,2,3,4,5]
# print(num[-3])

# words = "Hello,world,I,am,here"
# test = words.split(",")
# print (test)

#finding number of elements we use list
# numbers = ["a","b","c"]
# print(len(numbers))
#answer will be 3 numbers

# list1= ["a","b ","c"]
# list2= [1, 2, 3]
# list3= list1+ list2
# print(list3)
# #it'll print ['a', 'b ', 'c', 1, 2, 3]
#+= can be c += 5 is just c = c + 5

# Python program to find sum of elements in list
total = 0
ele = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# Iterate each element in list
# and add them in variale total
while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1
     
# printing total value
print("Sum of all elements in given list: ", total)