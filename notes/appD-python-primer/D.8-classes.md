---
appendix: D
section: "D.8"
title: "Classes"
pdf_pages: "492-494"
---

## D.8 Classes

Recall that objects are of fundamental importance in Python — indeed, data types and functions are all objects. A *class* is an object type, and writing a class definition can be thought of as creating a template for a new type of object. Each class contains a number of attributes, including a number of inbuilt methods. The basic syntax for the creation of a class is:

```
class <class_name>:
   def __init__(self):
       <statements>
   <statements>
```

The main inbuilt method is `__init__`, which creates an *instance* of a class object. For example, `str` is a class object (string class), but `s = str('Hello')` or simply `s = 'Hello'`, creates an instance, `s`, of the `str` class. Instance attributes are created during initialization and their values may be different for different instances. In contrast, the values of class attributes are the same for every instance. The variable `self` in the initialization method refers to the current instance that is being created. Here is a simple example, explaining how attributes are assigned.

```python
class shire_person:
   def __init__(self,name): # initialization method
       self.name = name    # instance attribute
       self.age = 0             # instance attribute
   address = 'The Shire'        # class attribute

print(dir(shire_person)[1:5],'...',dir(shire_person)[-2:])
                                  # list of class attributes

p1 = shire_person('Sam')   # create an instance
p2 = shire_person('Frodo') # create another instance
print(p1.__dict__)   # list of instance attributes

p2.race = 'Hobbit'   # add another attribute to instance p2
p2.age = 33          # change instance attribute
print(p2.__dict__)

print(getattr(p1,'address'))   # content of p1's class attribute
```
Output:
```
['__delattr__', '__dict__', '__dir__', '__doc__'] ...
['__weakref__', 'address']
{'name': 'Sam', 'age': 0}
{'name': 'Frodo', 'age': 33, 'race': 'Hobbit'}
The Shire
```

It is good practice to create all the attributes of the class object in the `__init__` method, but, as seen in the example above, attributes can be created and assigned everywhere, even outside the class definition. More generally, attributes can be added to any object that has a `__dict__`.

> **Tip:** An "empty" class can be created via
> ```
> class <class_name>:
>     pass
> ```

Python classes can be derived from a parent class by *inheritance*, via the following syntax.

```
class <class_name>(<parent_class_name>):
   <statements>
```

The derived class (initially) inherits all of the attributes of the parent class.

As an example, the class `shire_person` below inherits the attributes `name`, `age`, and `address` from its parent class `person`. This is done using the `super` function, used here to refer to the parent class `person` without naming it explicitly. When creating a new object of type `shire_person`, the `__init__` method of the parent class is invoked, and an additional instance attribute `Shire_address` is created. The `dir` function confirms that `Shire_address` is an attribute only of `shire_person` instances.

```python
class person:
   def __init__(self,name):
       self.name = name
       self.age = 0
       self.address= ' '

class shire_person(person):
   def __init__(self,name):
       super().__init__(name)
       self.Shire_address = 'Bag End'

p1 = shire_person("Frodo")
p2 = person("Gandalf")
print(dir(p1)[:1],dir(p1)[-3:] )
print(dir(p2)[:1],dir(p2)[-3:] )
```
Output:
```
['Shire_address'] ['address', 'age', 'name']
['__class__'] ['address', 'age', 'name']
```
