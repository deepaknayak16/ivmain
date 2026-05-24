'''
1. Class
A class is a blueprint for creating objects. It defines attributes (variables) and behaviors (methods).
2. Object
An object is an instance of a class. It contains real values of attributes defined in the class.
3. Encapsulation
Encapsulation is the concept of restricting direct access to certain attributes and methods. It is achieved using private (__) and protected
 (_) attributes.
4. Inheritance
Inheritance is the process of creating a new class by inheriting properties and methods from an existing class. 
It promotes code reuse and organization.
5. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables
dynamic method binding and method overriding.
6. Abstraction : 
Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. 
It is achieved using abstract classes and interfaces.
7. Method Overriding
Method overriding is the ability of a subclass to provide a specific implementation of a method that is already provided by its superclass.
8. Method Overloading
Method overloading is the ability to define multiple methods with the same name but different parameters or arguments.
9. Composition
Composition is a design technique in object-oriented programming where objects are composed of other objects as parts.
10. Aggregation
Aggregation is a type of association where one class contains references to objects of another class as part of its state.
11. Association
Association is a relationship between two classes that describes how they are related to each other.
12. Dependency
Dependency is a relationship between two classes where one class depends on another class but does not own or control it.
13. Class Method
A class method is a method that is bound to the class and not the object instance. It can access class variables and modify them.
14. Static Method
A static method is a method that does not access or modify class or instance variables. It is defined using the @staticmethod decorator.
15. Instance Method
An instance method is a method that is bound to the object instance. It can access and modify instance variables.
16. Getter and Setter Methods
Getter and setter methods are used to get and set the values of private attributes in a class, respectively.
17. Constructor
A constructor is a special method in a class that is automatically called when an object is created. It initializes the object's state.
18. Destructor
A destructor is a special method in a class that is automatically called when an object is destroyed. It cleans up resources used by the object.
19. Singleton Pattern
The singleton pattern is a design pattern that restricts the instantiation of a class to a single object. It ensures that only one instance of the class exists.
20. Factory
The factory pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects created.
21. Decorator
The decorator pattern is a structural design pattern that allows behavior to be added to individual objects dynamically. It is used to extend or modify the behavior of objects at runtime.
22. Observer
The observer pattern is a behavioral design pattern where an object (subject) maintains a list of dependents (observers) that are notified of any changes in its state.

🔴 Problems with Overusing Global Variables
Unintended Side Effects:
Any function can modify the global state, making the program unpredictable.
Hard to Debug:
Tracking where a variable was changed becomes difficult in large codebases.
Testing Is Harder:
Functions that rely on globals are harder to isolate and test.
Namespace Pollution:
Globals occupy the global namespace, increasing the risk of name clashes.
Poor Code Readability:
Readers of your code may not know where a global variable is being used or modified.
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Inheritance(Single,Multiple,Multilevel,Hierchical,Hybdrid)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Key Concepts in Inheritance:
Parent Class (Base Class or Superclass): The class whose properties and methods are inherited by another class.
Child Class (Derived Class or Subclass): The class that inherits the properties and methods from the parent class. It can also add its 
own attributes and methods or override those from the parent class.
Syntax of Inheritance
In Python, inheritance is implemented by passing the parent class as a parameter to the child class. Here’s a simple example:
'''
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"

# Child class
class Dog(Animal):
    def sound(self):
        return "Bark"

# Instantiate objects
dog = Dog("Buddy")
print(dog.name)      # Output: Buddy
print(dog.sound())   # Output: Bark

#Key Aspects of Inheritance:
#Single Inheritance:

#A derived class inherits from one base class.
#Example:
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def speed(self):
        print("Car is speeding")

car = Car()
car.move()  # Inherited method from Vehicle class
car.speed()  # Car's own method

#Multiple Inheritance:
#A derived class can inherit from more than one base class. This allows a class to inherit attributes and methods from multiple parents.
#Example:
# Base Class 1: Employee
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

# Base Class 2: Manager
class Manager:
    def __init__(self, department):
        self.department = department

    def show_managerial_role(self):
        print(f"Manages Department: {self.department}")

# Derived Class: TeamLead (Inheriting from Employee & Manager)
class TeamLead(Employee, Manager):
    def __init__(self, name, emp_id, department, team_size):
        # Calling constructors of both parent classes
        Employee.__init__(self, name, emp_id)
        Manager.__init__(self, department)
        self.team_size = team_size

    def show_team_lead_details(self):
        self.show_details()
        self.show_managerial_role()
        print(f"Team Size: {self.team_size}")

# Creating an object of TeamLead
lead = TeamLead("John Doe", "E123", "Software Development", 10)

# Displaying TeamLead details
lead.show_team_lead_details()


#Multilevel Inheritance:
#In multilevel inheritance, a derived class is derived from another derived class. This forms a hierarchy.
#Example:
class Animal:
    def sound(self):
        print("Animal makes sound")

class Mammal(Animal):  # Derived from Animal
    def has_fur(self):
        print("Mammal has fur")

class Dog(Mammal):  # Derived from Mammal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.sound()  # Inherited from Animal
dog.has_fur()  # Inherited from Mammal
dog.bark()  # Defined in Dog class

#Hierarchical Inheritance:
#In this type of inheritance, multiple derived classes inherit from a single base class.
#Example:
class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
cat = Cat()

dog.sound()  # Inherited from Animal
cat.sound()  # Inherited from Animal
#Hybrid Inheritance:
#This is a combination of two or more types of inheritance. It can involve multiple, multilevel, and hierarchical inheritance structures together.
#Overriding Methods: Replace parent method
#A derived class can override or replace methods from its base class by defining methods with the same name in the derived class.
#Example:
class Parent:
    def say_hello(self):
        print("Hello from Parent class")

class Child(Parent):
    def say_hello(self):
        print("Hello from Child class")

child = Child()
child.say_hello()  # Output: Hello from Child class (overrides the Parent method)
#Using super(): Extend parent method
#The super() function allows you to call methods from the parent class in the child class. It is often used when you want to extend or modify the functionality of the parent class rather than replace it entirely.
#Example:
class Parent:
    def say_hello(self):
        print("Hello from Parent class")

class Child(Parent):
    def say_hello(self):
        super().say_hello()  # Call the parent class method 
        print("Hello from Child class")

child = Child()
child.say_hello()   # Output: Hello from Parent class
                    #         Hello from Child class
# EXAMPLE:
class Parent:
    def __init__(self):
        self.num =100
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var =200
child = Child()
print(child.num, ' ', child.var)  #Output: 100   200

'''
Inheritance of Constructors:

The constructor (__init__()) of the parent class is not automatically called in the child class unless you explicitly call it using 
super().__init__(). If the child class defines its own constructor, it will override the parent’s constructor unless super() is used.
Advantages of Inheritance:
Code Reusability: The child class can reuse methods and properties of the parent class, which reduces code duplication.
Extensibility: A child class can extend or modify the behavior of a parent class.
Maintainability: Inheritance allows a modular and organized way to handle code, making it easier to maintain and manage larger systems.
Polymorphism: It allows the use of the same method or attribute names in different contexts with different functionality.
Disadvantages of Inheritance:
Complexity: Overusing inheritance, especially with multiple and multilevel inheritance, can make the code more difficult to understand and debug.
Tight Coupling: The child class is tightly coupled with the parent class. Changes in the parent class can inadvertently affect the child class, potentially causing unexpected issues.
Overhead: If inheritance is used improperly or unnecessarily, it can introduce performance overheads and make the program less efficient.
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Accesser Mothos (Public,Private,Protect) Encapsulation
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Public Access Modifier:
#Public members are accessible from outside the class. They are denoted by no prefix.
class Person:
    def __init__(self, name, age):
        self.name = name  # Public variable
        self.age = age  # Public variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Creating object
person = Person("Alice", 20)
person.display()

# Accessing public variables
print(person.name)  # Accessible
print(person.age)  # Accessible


#Protected Access Modifier:
#Protected members are accessible within the class and its subclasses (derived classes). They are denoted by a single underscore (_) prefix.
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected variable
        self._age = age  # Protected variable

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        super().display()
        print(f"Roll Number: {self.roll_number}")
# Creating object
student = Student("Alice", 20, "A123")
student.display()

# Accessing protected variables
print(student._name)  # Accessible
print(student._age)  # Accessible

#Private Access Modifier:
#Private members are accessible only within the class where they are defined. They are denoted by a double underscore (__) prefix.
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age  # Private variable

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        super().display()
        print(f"Roll Number: {self.roll_number}")
# Creating object
student = Student("Alice", 20, "A123")
student.display()

# Trying to access private variables (will give an error)
# print(student.__name)  # AttributeError
# print(student.__age)  # AttributeError

#Encapsulation:
#Encapsulation is the concept of restricting direct access to certain attributes and methods. It is achieved by making attributes private and providing public methods to access or modify them.
#Example:
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age  # Private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
# Creating object
person = Person("Alice", 20)

# Accessing private variables using public methods
print(person.get_name())  # Accessible
print(person.get_age())  # Accessible

# Modifying private variables using public methods
person.set_name("Bob")
person.set_age(25)
person.display()


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Polymersim (Method Overriding,Method Overloading)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
# It enables dynamic method binding and method overriding.
##Example:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) # Output: Woof! Meow!

#Method Overriding:
#Method overriding is the ability of a subclass to provide a specific implementation of a method that is already provided by its superclass.
#Example:
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"
print(Dog().speak()) #Output: Dog barks
print(Cat().speak()) #Output: Cat meows 

#Method Overloading:
# Method overloading is the ability to define multiple methods with the same name but different parameters or arguments.
# Python does not support method overloading natively, but you can achieve similar functionality using default arguments or variable-length arguments.
# Example:
# Method overloading using default arguments
# class Calculator:
#    def add(self, a, b=None, c=None):
#       if b is not None and c is not None:
#         return a + b + c
#      elif b is not None:
#        return a + b
#    else:
#       return a

# # Create an object
# calc = Calculator()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Abstraction 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from abc import ABC, abstractmethod
import re

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create object
circle = Circle(5)
print(circle.area())  # Output: 78.5

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Class Methods, Static Methods and instance methods
                - Instance → works with object.
                - Class → works with class.
                - Static → works independently.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class MyClass:
    # Class-level attribute
    class_variable = 0  # class variable shared by all instances
    __count = 0 # private class variable
    def __init__(self, value):
        # Instance-level attribute
        self.value = value
    # Instance method
    def display(self):
        print(f"Instance value: {self.value}")
        self.__count += 1
        print(f"Count: {self.__count}")

    # Class method
    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        print(f"Class variable incremented to: {cls.class_variable}")
    # Static method
    @staticmethod
    def multiply(a, b):
        return f"Result of multiplication: {a * b}"

# Create an instance of MyClass
obj = MyClass(10)
# Call instance method
obj.display()  # Output: Instance value: 10, Count: 1
obj.display()  # Output: Instance value: 10, Count: 2
# Call class method
MyClass.increment_class_variable()  # Output: Class variable incremented to: 1
MyClass.increment_class_variable()  # Output: Class variable incremented to: 2
# Call static method
print(MyClass.multiply(5, 3))  # Output: Result of multiplication: 15

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Getter and setter
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Getter and Setter methods are used in Python to control access to the attributes of a class. They allow you to encapsulate the internal representation 
# of an object while providing a way to get (retrieve) and set (modify) its attributes safely.
#In Python, you can use the @property decorator to define getter methods and the @<attribute>.setter decorator to define setter methods. 
# This approach is more Pythonic than using traditional getter and setter methods.
class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute (conventionally marked with a single underscore)
        self._age = age    # Private attribute

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
person = Person("Alice", 25)

# Access attributes using getters
print(person.name)  # Output: Alice
print(person.age)   # Output: 25

# Modify attributes using setters
person.name = "Bob"
person.age = 30

# Display updated details
person.display()  # Output: Name: Bob, Age: 30

# Attempt to set invalid values
try:
    person.name = 123  # Raises ValueError: Name must be a string.
except ValueError as e:
    print(e)

try:
    person.age = -5  # Raises ValueError: Age must be a non-negative integer.
except ValueError as e:
    print(e)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Constructor and Destructor
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Constructor: The __init__ method is called when an object is created. It initializes the object's attributes.
#Destructor: The __del__ method is called when an object is about to be destroyed (e.g., when it goes out of scope or is explicitly deleted). 
# It is used to perform cleanup tasks.

class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Constructor called: {self.name} created.")

    # Destructor
    def __del__(self):
        print(f"Destructor called: {self.name} destroyed.")

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
person1 = Person("Alice", 25)
# Access attributes and call methods
person1.display()  # Output: Name: Alice, Age: 25
# Create another object
person2 = Person("Bob", 30)
person2.display()  # Output: Name: Bob, Age: 30
# Delete an object explicitly
del person1  # Destructor called: Alice destroyed.
# The destructor for person2 will be called automatically when the program ends
'''class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print(f"File {filename} opened.")

    def write_data(self, data):
        self.file.write(data)
        print(f"Data written to file.")

    def __del__(self):
        self.file.close()
        print("File closed.")

# Create an object
file_handler = FileHandler("example.txt")

# Write data to the file
file_handler.write_data("Hello, World!")

# Destructor will be called when the object is deleted or goes out of scope
del file_handler  # Output: File closed.'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Association , Agregation, Composition and Dependancy 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Association: Two classes are connected but can exist independently.
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

# Aggregation: A class (Department) has a collection of another class (Teacher), but the parts can exist independently.
class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # Aggregation: Department has teachers

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_teachers(self):
        print(f"Teachers in {self.name}:")
        for teacher in self.teachers:
            print(teacher.name)

# Composition: A class (Car) owns another class (Engine), and the parts cannot exist independently.
class Engine:
    def __init__(self):
        print("Engine created.")

    def __del__(self):
        print("Engine destroyed.")

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()  # Composition: Car has an engine

    def __del__(self):
        print(f"{self.model} is destroyed, and so is its engine.")

# Dependency: One class (Calculator) temporarily uses another class (Logger) for a specific task.
class Logger:
    @staticmethod
    def log(message):
        print(f"Log: {message}")

class Calculator:
    def add(self, a, b):
        result = a + b
        Logger.log(f"Addition result: {result}")  # Dependency: Calculator uses Logger
        return result

# Main program
if __name__ == "__main__":
    # Association
    teacher1 = Teacher("Mr. Smith")
    student1 = Student("Alice")
    print(f"{teacher1.name} teaches {student1.name}.")  # Output: Mr. Smith teaches Alice.

    # Aggregation
    department = Department("Computer Science")
    department.add_teacher(teacher1)
    department.add_teacher(Teacher("Ms. Johnson"))
    department.display_teachers()  # Output: Teachers in Computer Science: Mr. Smith, Ms. Johnson

    # Composition
    car = Car("Tesla Model S")
    del car  # Output: Tesla Model S is destroyed, and so is its engine. Engine destroyed.

    # Dependency
    calculator = Calculator()
    calculator.add(5, 3)  # Output: Log: Addition result: 8

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: How is multithreading and multi processing in python 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Multithreading vs. Multiprocessing in Python
Python provides two ways to achieve parallel execution:
Multithreading (Using threading module)
Multiprocessing (Using multiprocessing module)
🔹 Multithreading
Definition: Multithreading allows multiple threads to run concurrently within the same process.
Uses: Best for I/O-bound tasks like network requests, file reading/writing, or database queries.
Limitation: Due to Python's Global Interpreter Lock (GIL), only one thread executes Python bytecode at a time, making CPU-bound tasks 
inefficient.
🔹 Multiprocessing
Definition: Multiprocessing allows multiple processes to run concurrently, each with its own memory space.
Uses: Best for CPU-bound tasks like image processing, machine learning, or data crunching.
Advantage: Each process runs independently, bypassing the GIL, allowing true parallel execution.
'''
'''
----------------------------------------------------------------------------------------------------
| Feature         | Multithreading                                | Multiprocessing                   |
-----------------------------------------------------------------------------------------------------
| Execution Model | Multiple threads in the same process          | Multiple independent processes     |
| Memory Usage	  | Shared memory (low)	                          | Separate memory (high)             |
| Best For	      | I/O-bound tasks (e.g., web scraping,          | CPU-bound tasks (e.g., image processing, 
|                 |  database queries)	                          | heavy computations)                 |
| GIL Impact	  | Affected by Global Interpreter Lock (GIL)	  | Bypasses GIL, true parallelism      |
| Performance	  | Faster for I/O tasks	                      | Faster for CPU-heavy tasks          |
| Overhead	      | Low (lightweight)	                          | High (heavyweight due to process creation)|
--------------------------------------------------------------------------------------------------------------------

'''
import multiprocessing.pool
import threading
import time
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")
def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Starting threads
t1.start()
t2.start()

# Waiting for threads to finish
t1.join()
t2.join()

print("Multithreading Done")

import multiprocessing
import time

def compute_square(n):
    print(f"Square of {n}: {n*n}")
    time.sleep(1)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    # Creating multiple processes
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=compute_square, args=(num,))
        processes.append(p)
        p.start()
    
    # Waiting for all processes to finish
    for p in processes:
        p.join()

    print("Multiprocessing Done")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: How is memory managed in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''1. Memory Management Concepts in Python
a) Private Heap Space:
Python objects and data structures are stored in a private heap, which is not directly accessible to the programmer.
The Python memory manager manages this private heap. It handles the allocation and deallocation of memory blocks as needed.
b) Memory Allocators:
Python has several memory allocators that work at different levels to optimize memory management:

Raw memory allocator: This manages the raw memory by interacting with the operating system.
Object-specific allocators: These are specialized memory managers used to handle specific types of objects (like integers, lists, or 
dictionaries) more efficiently.
Pool allocators: These manage small memory blocks within pre-allocated pools to reduce fragmentation and improve speed.
2. Python’s Built-in Garbage Collection (GC)
Garbage collection is the process of automatically reclaiming memory that is no longer in use. Python uses two primary methods for 
garbage collection:

a) Reference Counting:
Python uses reference counting to keep track of the number of references to an object in memory.

When the reference count of an object drops to zero (i.e., no part of the program is using it), Python automatically frees the memory used by that object.'''

#Example:
a = [1, 2, 3]
b = a  # Reference count of the list increases
del a  # Reference count decreases, but still 1 (b points to it)
del b  # Reference count is now 0, memory is deallocated

#In the above example, when both references to the list are deleted, the memory is automatically released.
'''b) Cyclic Garbage Collection:
Reference counting alone can’t detect cyclic references, where two or more objects reference each other, creating a cycle.

Python’s garbage collector also includes a cyclic garbage collector that detects and cleans up objects involved in reference cycles.

It uses generational garbage collection, grouping objects by their lifespan, with objects that survive multiple collections placed in 
older generations. Older generations are collected less frequently than younger ones, optimizing performance.'''

#Example of a reference cycle:

class Node:
    def __init__(self):
        self.other = None

node1 = Node()
node2 = Node()

# Create a reference cycle
node1.other = node2
node2.other = node1

del node1
del node2
# Without cyclic garbage collection, the memory would never be freed.

#Automatic garbage collection 
#Example
def create_list():
    temp_list = [1, 2, 3, 4, 5]
    return temp_list
# Create a list and assgin to a variable 
result = create_list()
print("Result", result)
# After this point, `temp_list` will be garbage collected if there are no references to it.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: What is monkey patching in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Monkey patching in Python refers to the dynamic modification of a class or module at runtime. This means that you can alter or extend 
the behavior of existing classes or modules without modifying the original source code. Monkey patching is typically used to make 
changes to third-party libraries or modules when you cannot directly modify them, but you want to change or extend their behavior for 
specific use cases.
'''
#Example of Monkey Patching
#Here's a simple example where we monkey-patch a method of an existing class.
class Animal:
    def sound(self):
        print("Some generic sound")

# Monkey patch the `sound` method of Animal class
def new_sound(self):
    print("Woof Woof!")

# Assign the new method to the class
Animal.sound = new_sound

# Now any instance of Animal will use the new sound method
a = Animal()
a.sound()  # Output: Woof Woof!

#In this example, we replace the sound method of the Animal class with a new method (new_sound). Now, every instance of the Animal 
#class will use the new sound method.

#Example: Monkey Patching a Third-Party Module
#Assume you are using a third-party library with a bug, and you can’t modify the library’s source code. You can use monkey patching to fix the bug in your application.
#import IV_Q_COUNT

# Assume some_library has a buggy method called `function()`
#def fixed_function():
    #print("This is the fixed version of the function!")

# Monkey patch the buggy function with the fixed one
#IV_Q_COUNT.function = fixed_function

# Now, calling some_library.function() will call the fixed version
#IV_Q_COUNT.function()  # Output: This is the fixed version of the function!
'''Downsides of Monkey Patching:
Unexpected Side Effects:

Since monkey patches alter the behavior of classes or modules globally, it can lead to unexpected side effects in other parts of the code that depend on the original behavior.
Maintenance Issues:

If the third-party library or the original codebase is updated in the future, your monkey patch might break or cause compatibility issues.
Debugging Complexity:

It can make debugging more difficult since the original code behavior has been altered, potentially leading to hard-to-find bugs.
Readability:

Monkey patches can reduce code readability because future developers may not expect certain behaviors to be altered in this manner, and it might not be clear from the codebase why something is behaving differently.'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: How Decorators Work?With example
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#A decorator in Python is a function that modifies or extends the behavior of another function or method without changing its code.
#How Decorators Work:
#A decorator takes a function as input and returns a new function that enhances or alters the behavior of the original function.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper executed before the function")
        result = func(*args, **kwargs)
        print("Wrapper executed after the function")
        return result
    return wrapper
@my_decorator
def add(x, y):
    print(f"Adding {x} and {y}")
    return x + y
print(add(5, 3))

# Define a decorator that repeats a function N times
def repeat_three_times(func): # ← func = the function you are decorating
    def rept(*args, **kwargs):
        print(f"Start func.. {func.__name__}")
        result = None
        for _ in range(3):
            result = func(*args, **kwargs) # ← Here we call the original function
        if result is not None:
            print(f"Result: {result}")
        print(f"Finish Func .. {func.__name__}")
    return rept  # Must return the wrapper
# Use the decorator
@repeat_three_times
def greet():
    print("Hello Deepak")
@repeat_three_times
def add(x, y):
    return x + y
# Call the decorated function
greet()
print("Adding 5 and 3")
add(5, 3)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: How to Reload a Module in Python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''To reload a module in Python, you can use the reload() function from the importlib library. 
This re-executes the module's code and updates any references to objects within the module to reflect changes.

Steps to Reload a Module:
Import the module.
Make changes to the module (e.g., edit the code).
Reload the module using importlib.reload().'''

import importlib

# Reload the module to reflect the changes
#importlib.reload(IV_Q_COUNT)

# Call the function again
#IV_Q_COUNT.greet()  # Output: "Hi, module was changed!"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: write a progam to  thread one with excute the even number and other thread will excute 
the odd number o/p will 1,2,3,4,5,6,7,8,9,10
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import threading

# Initialize a threading lock
lock = threading.Lock()
# Variable to keep track of the current number
current_number = 1

# Function to print odd numbers
def print_odd():
    global current_number
    while current_number <= 10:
        with lock:
            if current_number % 2 != 0:
                print(current_number)
                current_number += 1

# Function to print even numbers
def print_even():
    global current_number
    while current_number <= 10:
        with lock:
            if current_number % 2 == 0:
                print(current_number)
                current_number += 1

# Creating threads for odd and even
odd_thread = threading.Thread(target=print_odd)
even_thread = threading.Thread(target=print_even)

# Start the threads
odd_thread.start()
even_thread.start()

# Wait for both threads to complete
odd_thread.join()
even_thread.join()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Circular queue ?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class CircularQueue:
    # Constructor
    def __init__(self, maxSize=8):
        self.queue = [None] * maxSize  # Initialize the queue with fixed size
        self.head = 0
        self.tail = 0
        self.maxSize = maxSize

    # Adding elements to the queue
    def enqueue(self, data):
        if self.size() == self.maxSize:  # Check if the queue is full
            return "Queue Full!"
        self.queue[self.tail] = data  # Add data to the tail
        self.tail = (self.tail + 1) % self.maxSize  # Move tail circularly
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.size() == 0:  # Check if the queue is empty
            return "Queue Empty!"
        data = self.queue[self.head]  # Get data from the head
        self.queue[self.head] = None  # Clear the slot
        self.head = (self.head + 1) % self.maxSize  # Move head circularly
        return data

    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.maxSize - (self.head - self.tail)

    # Optional: Display the queue (for debugging purposes)
    def display(self):
        print(f"Queue: {self.queue}, Head: {self.head}, Tail: {self.tail}, Size: {self.size()}")
cq = CircularQueue(maxSize=4)

print(cq.enqueue(10))  # True
print(cq.enqueue(20))  # True
print(cq.enqueue(30))  # True
print(cq.enqueue(40))  # True
print(cq.enqueue(50))  # Queue Full!

print(cq.dequeue())    # 10
print(cq.dequeue())    # 20
print(cq.enqueue(50))  # True

cq.display()  # Queue: [None, None, 30, 40, 50], Head: 2, Tail: 1, Size: 3
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: How to Call parent __init__ method??
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#In Python, the parent class's __init__ method can be explicitly called from a child class using either the super() function or 
# directly referencing the parent class. 
# This is often done to ensure the parent class is properly initialized when subclassing.
class BaseClass:
    def public_method(self):
        print("Public method in BaseClass called.")
        self.__private_method()  # Private method can be called within the class.

    def __private_method(self):
        print("Private method in BaseClass called.")

class SubClass(BaseClass):
    def public_method(self):
        print("Public method in SubClass called.")
        super().public_method()  # Call the parent's public method

    # Trying to override a private method won't work as intended because private methods are name-mangled.
    def __private_method(self):
        print("This won't override the BaseClass private method due to name mangling.")

# Example usage
sub = SubClass()
sub.public_method()

# Attempting to directly access private method
# sub.__private_method()  # Will raise AttributeError

# Accessing private method through name mangling (not recommended)
# sub._BaseClass__private_method()  # This would work but violates encapsulation

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: How to Call parent __init__ method??
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized with name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        # Call the parent class's __init__ method
        super().__init__(name)
        self.age = age
        print(f"Child initialized with age: {self.age}")

# Create an instance of the Child class
child = Child("John", 10)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''' The line if __name__ == '__main__': is a common construct in Python scripts. It is used to determine whether the Python file is being run as a standalone program or being imported as a module into another script.

__name__: This is a special built-in variable in Python.

When a Python script is run directly, __name__ is set to '__main__'.

When the script is imported as a module in another script, __name__ is set to the name of the module (i.e., the filename without the .py extension).

Purpose: The if __name__ == '__main__': block allows you to write code that will only execute when the script is run directly, not when it is imported as a module.
# my_script.py

def main():
    print("This is the main function.")

if __name__ == '__main__':
    main()
If you run my_script.py directly, the output will be:
This is the main function.
If you import my_script.py into another script, the main() function will not run automatically. '''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Writing efficient Python code can save time, reduce memory usage, and improve performance.?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time
import multiprocessing
#List Comprehesion - faster than loop
number = range(18)
squared = [x**2 for x in number]
print(squared)
#Output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Generator : memory efficient iteration 
def number_generator(n):
    for i in range(n):
        yield i**2
print(list(number_generator(18)))
#output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#multiprocessing : utilize multiple upu core 
def square(n):
    return n**2
if __name__=="__main__":
    start = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(square, range(10))
    print(result)
    #Output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print (f"Time taken :{time.time() - start:.4f} sec") #Time taken :0.0199 sec

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: OOP makes code reusable, scalable & maintainable! ?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from abc import ABC , abstractmethod
#Abstarct Class
class Device(ABC):
    def __init__(self, brand):
        self.brand = brand
    @abstractmethod
    def device_info(self):
        pass
#base class 1
class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def device_info(self):
        return f"{self.brand}{self.model} --Smartphone"
#Base Class 2
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
    def capture_pic(self):
        return f"Capturing photo at {self.resolution} resolution"
#Multiple Inheritance : Smartphone inherit from Phone & Camera
class SmartPhone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)
    #Polymorphism: Overriding device_info method
    def device_info(self):
        return f"{self.brand} {self.model} --Smartphone with {self.resolution} camera"
#usagee
iphone = SmartPhone("Apple", "15Pro", "45MP" )
print(iphone.device_info())
print(iphone.capture_pic())
   
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Multiple Abstraction
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from abc import ABC, abstractmethod
# First Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Second Abstract Base Class
class Color(ABC):
    @abstractmethod
    def get_color(self):
        pass

# Subclass inheriting from multiple abstract classes
class ColoredCircle(Shape, Color):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def get_color(self):
        return f"The color is {self.color}"

# Create an instance of ColoredCircle
circle = ColoredCircle(5, "Red")
print(circle.area())       # Output: 78.5
print(circle.perimeter())  # Output: 31.400000000000002
print(circle.get_color())  # Output: The color is Red
'''
When to Use Multiple Abstraction:
When you want to enforce a contract (set of methods) from multiple sources.
When you want to combine behaviors or properties from multiple abstract classes into a single class.
When designing complex systems where classes need to adhere to multiple interfaces.
Limitations:
Complexity: Multiple inheritance can make the code harder to understand and maintain.
Diamond Problem: If two parent classes have a method with the same name, it can lead to ambiguity. 
Python resolves this using the Method Resolution Order (MRO).
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 ::  classic multiple inheritance + MRO (Method Resolution Order)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet() #Super B Means next after B in MRO → C 

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()  #Super C Means next after C in MRO → A

class D(B, C):
    pass
# Create an instance of D
d = D() #Build te MRO for D: D → B → C → A -> object
d.greet() # Output:
# Hello from B  
'''
The diamond problem occurs when a class inherits from two classes that both inherit from a common base class. 
Python's MRO resolves this problem elegantly.
How MRO Works:
Depth-First Search (DFS): Python traverses the inheritance graph depth-first.
Left-to-Right: When multiple inheritance is involved, Python prioritizes the leftmost parent class first.
C3 Linearization: This algorithm ensures that the MRO is consistent and avoids ambiguity.
Key Points About MRO:
Subclasses Come First:
In the MRO, subclasses always appear before their parent classes.
Left-to-Right Order:
If a class inherits from multiple classes, the order of inheritance (left-to-right) is preserved.
No Ambiguity:
The C3 Linearization algorithm ensures that there are no conflicts or ambiguities in the MRO.
super() and MRO:
The super() function uses the MRO to call methods from the parent classes.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Differences Between Constructor Overloading and Method Overloading?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

Feature	            Constructor Overloading	                                     Method Overloading
Purpose	            Allows multiple ways to initialize an object.	            Allows multiple ways to call a method.
Implementation	    Uses a single __init__ method with default arguments or     Uses a single method with default arguments or variable-length arguments.
                    conditional logic.	
Python Support	    Not natively supported; simulated using default arguments.	Not natively supported; simulated using default arguments or *args, **kwargs.
Example	            __init__(self, name, age=None, city=None)	                add(self, a, b=None, c=None)
Use Case	        Flexible object initialization.	                            Flexible method behavior based on inputs.
'''
#ConsturctorOverloading
class Person:
    def __init__(self, name, age=None, city=None):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# Different ways to initialize the object
person1 = Person("Alice")
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30, "New York")

person1.display()  # Output: Name: Alice, Age: None, City: None
person2.display()  # Output: Name: Bob, Age: 25, City: None
person3.display()  # Output: Name: Charlie, Age: 30, City: New York
#MethodOverloading
class MathOperations:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c
        
# Different ways to call the method
math = MathOperations()
print(math.add(5))          # Output: 5
print(math.add(5, 10))      # Output: 15
print(math.add(5, 10, 15))  # Output: 30
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: _ Single underscore leading and traling 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 1. Single leading underscore "_var"
# Indicate internal use (not enforced but a convention)
class MyClass:
    def __init__(self):
        self._internal_var = 43 #ment for internal use
obj = MyClass()
print(obj._internal_var) #accesble but should be treat as private

# 2. Single traling  underscore "var_"
#Used to avoid naming confict with python keywords
def my_fun(class_): #class is a keyword so we use "class_"
    return f"Recoved : {class_}"
print(my_fun("Python"))

# 3. Single underscore "_"
# Used for insignificant values 
for _ in range(3): # loop variable we dont care
    print("Deepak Ok")

#Double Leading Underscore “__var”: Triggers name mangling when used in a class context. Enforced by the Python interpreter. 
#Double Leading and Trailing Underscore “__var__”: Indicates special methods defined by the Python language. Avoid this naming scheme for your own attribute

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What Context Managers are in Python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Context Managers in Python
# Context managers are a way to allocate and release resources precisely when you want to. The most common use case is file handling,  
# where you want to ensure that a file is properly closed after its suite finishes, even if an error occurs.
# The most common way to use a context manager is with the `with` statement, which ensures that resources are properly managed.
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Can return any object to be used within the `with` block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        # Handle exceptions if needed
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
        return False  # If True, exceptions are suppressed
# Usage
with MyContextManager() as manager:
    print("Inside the context")
##############################################################
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is not None:
            print(f"Error occurred: {exc_val}")
        return False
# Usage
with FileHandler('example.txt', 'w') as file:
    file.write("Hello, Context Managers!")
            
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Parallelizing a Task with multiprocessing.Pool
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import multiprocessing
import time

# A sample task (CPU-bound)
def square(n):
    print(f"Process {multiprocessing.current_process().name} squaring {n}")
    time.sleep(1)  # simulate heavy work
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of worker processes (size = number of CPU cores)
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(square, numbers)   # run in parallel

    print("Results:", results)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Parallelizing a Task with multiprocessing.process
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import multiprocessing

def worker(num):
    print(f"Worker {num} running...")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All workers finished!")


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Just A Question Acessing the variable
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class opp:
    def __init__(self):
        self.m = 10
        self.__n = 20
    def op(self):
        return self.__n
obj1 = opp()
print(obj1.m) # Output: 10 #Why we can access m but not n  
print(obj1.op())    # Output: 20 #We can access n through the method op() 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: What is _name__ == '__main__': in python?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
