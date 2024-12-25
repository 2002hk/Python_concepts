#!/usr/bin/env python
# coding: utf-8

# Class and Object
# 
# - Write a Python class Car with attributes make, model, and year, and a method to display the car's details.
# - Create objects for the class and print their details

# In[1]:


class Car:
    def __init__(self):
        self.make='mercz'
        self.model='vb32'
        self.year='2002'
    def display(self):
        print('the maker of the car ',self.make)
        print('the model of the car', self.model)
        print('the year car was made', self.year)
car1=Car()
car1.display()


# Encapsulation
# 
# - Create a class BankAccount with private attributes _balance and methods deposit() and withdraw().
# - Ensure the balance can only be modified through these methods.

# In[4]:


class BankAccount:
    def __init__(self):
        self.__balance=10000
        
    def deposit(self,amount):
        print('The amount is deposited')
        self.__balance=self.__balance+amount
        
    def withdraw(self,amount):
        if amount>self.__balance:
            print('Insufficient Funds')
        else:
            self.__balance=self.__balance-amount
    def currentbalance(self):
        print('Your current Balance is ', self.__balance)
bank=BankAccount()
bank.deposit(10000)
bank.withdraw(10000)
bank.currentbalance()
bank.__balance


# Inheritance
# 
# - Design a class Animal with a method speak(). Create subclasses Dog and Cat, and override the speak() method for each.
# - Demonstrate polymorphism with these classes.

# In[15]:


# this type of polymorphism is called method overriding which is done on subclass which has a function with same name as the parent class but different implementation
class Animal:
   
    def speak():
        pass
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('{} barks!'.format(self.name))
class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('{} meows!'.format(self.name))

animal=Animal()
dog1=Dog('Lucky') 
dog1.speak()
cat1=Cat('Tixy')
cat1.speak()


# Polymorphism
# 
# - Implement a class hierarchy with a base class Shape and derived classes Circle, Rectangle, and Triangle. Each class should have a get_area() method.
# - Use polymorphism to calculate and display areas of different shapes.

# In[21]:


class Shape:
    def __init__(self):
        pass
    def get_area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def get_area(self):
        self.area=3.14*self.r**2
        return self.area
        #print('The area of circle is ', self.area)
        
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def get_area(self):
        self.area=self.l*self.b
        return self.area
        #print('The area of the rectangle ', self.area)
class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def get_area(self):
        self.area=0.5*self.b*self.h
        return self.area
        #print('The area of triangle ', self.area)
        
# Instantiate objects and calculate areas
shapes = [
    Circle(3),
    Rectangle(2, 3),
    Triangle(5, 10)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.get_area()}")


# Abstraction
# 
# - Define an abstract class Vehicle with an abstract method start(). Create subclasses like Bike and Car that implement the method.

# In[24]:


from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print('the Bike starts')
class Car(Vehicle):
    def start(self):
        print('the cars starts')
        
#vehicle=Vehicle()
bike1=Bike()
bike1.start()
car1=Car()
car1.start()


# Constructor and Destructor
# 
# - Write a class Book with attributes title and author. Implement a constructor to initialize these and a destructor to display a message when the object is deleted.

# In[29]:


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __del__(self):
        print('The object is deleted')
book1=Book('abcd','hfwef')
del book1


# Static and Class Methods
# 
# - Create a class Employee with a static method is_valid_age(age) that checks if the age is valid, and a class method from_string(emp_str) that creates an Employee object from a string like "John-30-50000".

# In[ ]:




