# #print("hello world")
# a=5
# ch='a'
# name="sandesh"

# print(a)
# print(ch)
# print(name)

# a=int(input("enter a num: "))
# b=int (input("enter second num: "))
# sum=a+b
# print(sum)

#..................................simple_inheritance.........................................................................
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname 
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname +" "+ self.lastname)

# x=person("sandesh","kandel")
# x.printname()

# class student(person):
#     def first(self):
#         print("i am a student")

# y=student("sahas","khadka")
# y.first()

#.........................................multiplelevel_inheritance.................................................................

# class vehicles:
#     def wheeler(self):
#      print("i am four wheeler ")

# class bike(vehicles):
#     def twowheel(self):
#         print("i am two wheeler")

# class ns(bike):
#     def nsbike(self):
#         print("ns 200")

# obj=ns()
# obj.nsbike()
# obj.twowheel()
# obj.wheeler()

#.........................................hierarchical.............................................................................

# class bird:
#     def allbirds(self):
#         print("all birds categories ")

# class eagle(bird):
#     def birdeagle(self):
#         print("i ama an eagle")

# class parrot(bird):
#     def birdparrot(self):
#         print("i can talk ;)")

# class dove(bird):
#     def dovebird(self):
#         print("i can flyyyyyyyyy highhh")

# obj=dove()
# obj.allbirds()
# obj.dovebird()

# obj=eagle()
# obj.allbirds()
# obj.birdeagle

#.......................................multiple_inheritance......................................................

# class bike:
#     def firstparent(self):
#         print("i am a parent class ")

# class car:
#     def secondparent(self):
#         print('i am a second parent class ')

# class vehicle(bike,car):
#     def childvehicle(self):
#         print("i am a child class")

# obj=vehicle()
# obj.childvehicle()
# obj.firstparent()
# obj.secondparent()

#.....................................print_stars........................................................................

# def stars(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print("@  ",end="")
#         print('\r')     
# stars(5)


#......pip install django..............................................................................................
#......create a class called rectange that has two attributes : l and w. the class should have a method called area and peremeter that calculates area and peremeter of rectangle.
#......create a class called bank account that has two attributes ;balance and acc no. the class should have method called deposite and withdraw that allows a user to deposite or withdraw from an account .the balance should be updated accordingly.

#..............................homework.................................................................................

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
   
#     def area(self):
#          area=self.length*self.width
#          print("area of rectangle is ",area)

#     def perimeter(self):
#         perimeter=2*(self.length+self.width)
#         print("perimeter of rectangle is: ",perimeter)

# obj=Rectangle(5,4)   
# obj.area()
# obj.perimeter()   

#..........................homework.............................................................................

# class Bank:
#     def __init__(self,balance,accountnum):
#         self.balance=balance
#         self.accountnum=accountnum
   
#     def deposit(self,money):
#          self.balance=self.balance+money
#          print("total balance ",self.balance)

#     def withdraw(self,money):
#         self.balance=self.balance-money
#         print("total balance: ",self.balance)

# obj=Bank(10000,54321)   
# obj.deposit(2000)
# obj.withdraw(1000)   


#.....................method_overloading.........................................................................................

# from multipledispatch import dispatch
# @dispatch(int,int)
# def product(a,b):
#     print(a*b)
# @dispatch(int,int,int)
# def product(a,b,c):
#     print(a*b*c)

# @dispatch(float,float,float)
# def product(a,b,c):
#     print(a*b*c)

# product(2,3,4)
# product(5,10)
# product(10.3,10.3,10.4)  

'''''
name = input("Enter your name: ")
for i in name:
    print (i)   '''

# for i in range(5,11):
#     print(i)    

# for i in range (1,11):
#     print("7 * ",i," = ",7*i)

# def stars(n):
#     num=1
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(num,end=" ")
#             num +=1
#         print('\r')     
# stars(5)

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

#.....write a program that takes a list of words as input and returns a new list containing only the words that have three letters and starts with the letter 'a' sorted in alphabetical order.
# word.len()
# and word [0]='a'


# words=["sam","ram","abinash","abc","aaaa","aab","acs"]
# newlist=[]
# for i in words :
#    if len(i)>3 and i[0]=='a':
#         newlist.append(i)
# newlist.sort()
# print(newlist) 

# a="sandesh"
# b=12
# c=12.12
# print (a, b, c)
# print(type(a),a)          1:10|>
    

'''

'''
# .....................area of rectangle........................................................
# class rect:
#     def __init__(self,length,breadth):
#          self.length=length
#          self.breadth=breadth

#     def area(self):
#         area=self.length*self.breadth
#         print( "area of rectangle is: ",area)
# obj=rect(4,5)
# obj.area()

# a=4
# b=5
# area=(a*b)
# print('area od rectangle is :',area)

# ....................simple intrest .................................................................
#take input from user
# principal = float (input("inter the principal: "))
# time = float (input("enter time: "))
# rate = float (input(" enter rate: "))

#calculate simple intrest
# simple_intrest = ((principal * time * rate) / 100)

#display the result
# print("simple intrest is: ", simple_intrest)

#.............................         .................................................
