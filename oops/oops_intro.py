# Object oriented programming - classes and objects
# focuses on DRY priciple - Dont repeat yourself
# time and space efficent 

# classes -> is a blueprint/template for creating objects, doesnot occupy any space
# Object -> is a instantiation of a class 

#blank railway reservation form  (class) -> fill the details -> application of that person to book a ticket (object)

# modelling a program in oops
# Noun -> class -> Employee
# Adjective -> properties/attributes -> name, age, salary
# verbs -> functions/methods -> getSalary() , increment()


# add two numbers

# creation of class
class Number:
    def sum(self):
        return self.a + self.b

# creating an object of Number class 
num = Number() 

num.a = 10
num.b = 20
s = num.sum()
print(s)

