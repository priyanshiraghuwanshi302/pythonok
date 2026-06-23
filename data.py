#data structure
######
# heterogenous data structure - multiple types of data 
# 1.list
# ""
# denoted by ->[]square btackets
# ""

# #1=[] empty list
# l= [10,20,30,40,50]
# print(l)
# print(type(l))

# hetrogenous data structure- multiple types of data ko store krwa sakte hai

# 2. duplicacy is allowed [same type data repeat]

# 3. list is ordered
# """"

# 4. mutable -> we can change  the value of item in the listn 


# l = [10,20,30,40,50]
# l[3]=400 # iteam assignment 
# print(l)


# item wise loop 
# l =[10,20,30,40,50]

# for i in l:
#     print(i)

# index wise loop 
# l=[10,20,30,40,50]
# for i in range(len(l)):
#     print(i,l[i])
    #i index of list
    #l[i] -> item of list



# question 

# l =[1,67,10,25,14,77]
# for i in l:
#     if i>15:
#         print(i)




# l=[1,67,10,25,14,77]
# for i in range(len(l)):
#     if l[i]>15:
#         print(l[i])



# sum all the element of the list 

# l=[10,20,30,40,50]
# sum=0
# for i in l:
#     sum+=i
#     print(sum)


#   #slicing
# [start=0: stop-1: step=1]
# l=[10,20,30,40,50]
# print(l[1:4:1])



# l=[10,20,30,40,50]

#method in lists
 
# print()
# int()
# .append()  yeh ek method hai 


# #1.  .append() -> addimg element at the last of list 
# l=[10,20,30,40,50]
# l.append(100)
# print(l)

# #2  .extend() lists add hojati hai i me second bhi 
# l1 =[10,20,30,40,50]
# l2=[60,70,80]
# l1.extend(l2)
# print(l1)


# #3.insert(index,value) for adding value in the place of index given
# l1.insert(1,100)
# print(l1)

# #4. .pop() element remove hojayega
# l1=[10,20,30,40,50]
# l1.pop(1)
# print(l1)


# #5.remove(element)
# l1=[1,2,3,4,5]
# l1.remove(5) #agar duplicate value hai toh first occurence remove.
# print(l1)


#6. len()-> list lenght
# l1=[1,5,5,5,5,2,3,4,5]
# print(len(l1))

# question 1 -accepts List elements and reprint it
# part1 accept elements
# n=int(input("enter the size of the lists:"))
# l=[]
# for i in range(n): #0,1,2,3,4
#     element=input("enter element for your lists:")
#     l.append(element)
# print(l)

# n= int(input('enter the size:'))#5
# l=[]
# for i in range(n): #0,1,2,3,4
#     element = input(f'enter element{i}for your lists:')
#     l.append(element)
# print(l)


#2. reverse a list without usig slicing.
# l1=[1,2,3,4,5]
# l1.reverse()
# print(l1)

#print positive and negative element of an lists 
# l1=[10,-9,20,30,-12,-25]
# if i in l1:
#     if i>1:
#        print("it is positive")
#     elif i<0:
#        print("it is negative")

#dictionary.
#[]-> list -square bracket
#{}-> curly bracket
 
#key - values pair
#butvalues can be duplicate but key cannot be


# d= {'a':10, 'b':20, 'c':30,'d':40}
#print20
# print(d['b'])

#creating a new key and assigning value to it.
# 

# d={'a':10,'b':20,'c':30,'d':40,'e':100} 
# d['e']=200# old value can be overwrite
# print(d)

#method of dictionary
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# info['age']=25#item assignment
# print(info)
# print(info.values())# sirf dictionary ki values 

#2.keys 
#'info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(info.keys())

#3. item()
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(info.item())

#4. pop()- it accept krys and will remove key values
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# info.pop('name')
# print(info)

# #length of dictorinary
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(len(info))


# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# for i in info:#i->keys
#     print(i,info[i])#info[i]->values.

# info={'name':'rahul','age':21,'marks':50.25,'present':True}#you will only get the values from dictorinary
# for i in info.values():
#     print(i)

#Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]
#paillndrome or not
#method-1







#Enumerate-> list->[10,20,30,40,50,]->index 0,1,2,3,4
#enumerateb-> index ke sath unki values bhi dega 
# l=[10,20,30,40,50,]
# for index,value in enumerate(l):
#     print(index,value)

# l=[10,20,30,40,50,]
# for index,value in enumerate(l):
#     print(index+1,value)


#6..update({key:value})
# d={'a':100,'b':200,'c':300}
# d.update({'c':500})
# print(d)
 
#7. .clear() -> remove all the element

# d={'a':100,'b':200,'c':300}
# d.clear()
# print(d)

# d={'a':100,'b':200,'c':300}
# del d #to delete all the data frpm memory
# print(d)




#QUESTIONS:

#1. we have  two lists and we have to make  list 1 as key of dict. and lists as values.

# l1=['a','b','c','d']
# l2=[10,20,30,40]

# d={}
# for i in range(len(l1)): #i 0123
#     d[l1[i]] = l2[i]
# print(d)


#2. you have a lists make the index as the keys ans element present on those indexs as values 
#01234-> keys 
# l = [10,20,30,40,50]
# d={}
# index =0
# for i in range(len(l)):
#     d[i]=l[i]
# print(d)

#3. merge 2 dictionaries.
# d1 ={'a':10, 'b':20} #c:30,d:40
# d2 ={'c':30, 'd':40}
# for i in d2: #i->c,d
#     if i not in d1: #c not in d1
#         d1[i]=d2[i]
# print(d1)



#4. frequency count.
# l=[1,1,1,2,2,3,3,6,6,7,6,3,4,1,2]
# d ={} #1:4, 2:3 
# for i in l:
#     if i not in d: #1 not in d
#         d[i]= 1
#     else:
#         d[i]+= 1
# print(d)




