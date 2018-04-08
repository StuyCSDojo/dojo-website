PyChan Objection Syntax
=======================

Topics Covered
--------------
  * :ref:`object_oriented`
  * :ref:`basic_class`
  * :ref:`constructors`
  * :ref:`expanding_the_basics`
  * :ref:`inheritance`

.. _object_oriented:

Python is Object Oriented
^^^^^^^^^^^^^^^^^^^^^^^^^
The syntax for writing Python classes are awkward, but Python is still an object oriented language.  Take
a look at Python list:
::

   >>> a = []
   >>> a.append(3)
   >>> print a
   [3]

Python lists are one example of a Python object

* The first line instantiates an instance of a ``list`` and binds it to ``a``
* In the second line, we call the ``append`` method of the ``list`` class
    
.. _basic_class:

The Basics of Writing a Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Let us start off with the syntax of a basic Python class:
::

   class <ClassName>:

       def <method_name>(self, args1, args2, ...):
           <stuff to do>
   
Here is an example:
::

   class Hello:

       def say_hello(self):
           print 'Hello'

How would you use it?
::

   >>> a = Hello()
   >>> a.say_hello()
   Hello
	   
Things to note:

* You declare a class with the ``class`` keyword
* Each method takes ``self`` as the first argument
* Instantiating a class is similar to calling a function

  * Simply set a variable equal to the class name and a pair of parentheses
    ::

       variable = ClassName()
* Access the methods of a class with the dot operator
  ::

     ClassName.method_name()
     # or
     variable = ClassName()
     variable.method_name()

.. _constructors:

Constructing Classes
^^^^^^^^^^^^^^^^^^^^
The next step is constructors:
::

   class BankAccount:

       def __init__(self):
           pass

       def deposit(self, amount):
           return 'You deposited some cash!'

The above constructor is the same thing as the default constructor.  Let us make it more useful:
::

   class BankAccount:

       def __init__(self):
           self.money = 50

       def deposit(self, amount):
           self.money += amount

If you were to use it:
::

   >>> bankaccount = BankAccount()
   >>> bankaccount.deposit(400)
   >>> print bankaccount.money
   450

Some Things to Note:

* Python has a special keyword, ``__init__``, for constructing a class

  * Like usual, you would need to specify ``self`` as the first argument
* Instance variables are prefixed with ``self.``

  * These variables are accessible anywhere in the class and each instance has its own copy
   
.. _expanding_the_basics:

Expanding the Basics
^^^^^^^^^^^^^^^^^^^^
Next, we would expand upon our basic knowledge and tie up a few loose ends:

* Modifying instance variables directly
  ::

     >>> b = BankAccount()
     >>> print b.money
     50
     >>> b.money = 500
     >>> print b.money
     500

  * Key Notes:

    * In Python, you can modify the instance variables directly.
    * Python prefers simplicity over the possibility that the user might do something stupid
    * Ways to control how the user may alter instance variables are beyond the scope of this lesson

* Who am I?
  ::

     class BankAccount:

         ...
     
         def deposit(self, amount):
	     self.money += amount
	     
  Key Notes:

    * In Java, you refer to the current instance with the ``this`` keyword
    * In Python, you use the ``self`` keyword

* Static methods
  ::

     class BankAccount:

         def __init__(self):
	     self.money = 50

	 @staticmethod
	 def name():
	     print 'BankAccount'

  A static method is declared by utilizing the ``staticmethod`` decorator.  It can be called without
  creating an instance:
  ::

     >>> BankAccount.name()
     BankAccount
     >>> BankAccount().name()
     BankAccount
   
* Static Variables
  ::

     class BankAccount:

         money = 50

	 def deposit(self, amount):
	     money += amount

  Key Notes:
  
  * Are declared without the ``self`` prefix
  * These variables can be accessed without declaring an instance of the class
  * If you modify the class copy and not the instance copy, the instance copy will change as well
  * Not truly static, each instance has their own copy
  
    * If you change the instance's copy, it will no longer sync up with the class copy

  ::

     >>> BankAccount.money
     50
     >>> b = BankAccount()
     >>> print b.money
     50
     >>> BankAccount.deposit(400)
     >>> BankAccount.money
     450
     >>> print b.money
     450
     >>> b.money = 400
     >>> print b.money
     400
     >>> print BankAccount.money
     450
     
* toString()
  ::
     
     class BankAccount:
       
         def __init__(self):
	     self.money = 50

	 def __repr__(self):
	     return 'BankAccount Representation Form'

	 def __str__(self):
	     return 'BankAccount String Form'

  ::

     >>> ba = BankAccount()
     >>> ba
     BankAccount Representation Form
     >>> print ba
     BankAccount String Form
     >>> [BankAccount(), BankAccount()]
     ['BankAccount Representation Form', 'BankAccount Representation Form']
     >>> 
	     
  Key Notes:

  * Generally ``__repr__`` is defined as a string representation of the object

    * This means ``eval(repr(object)) == object == True``
  * ``__str__`` is similar to ``__repr__``, but does not have the same constraints
  * By default, both ``__str__`` and ``__repr__`` simply contains the id (memory address) and object
    name
  * If ``__str__`` is not found, it falls back to ``__repr__``
  * ``__repr__`` is used when printing a container of objects

.. _inheritance:
       
Inheritance
^^^^^^^^^^^
Now that we have cover the basics, the next step is inheritance...

::

   class DerivedClassName(BaseClassName):
       pass

Simply pass the name of the parent class as an argument to the derived class.  For example:
::
   
   class Animal:

       def __init__(self, name):
           self.name = name

       def speak(self):
           return '??'

   class Dog(Animal):

       pass           

Let's see what we can do with this:
::

   >>> tom = Dog('tom')
   >>> tom.name
   tom
   >>> tom.speak()
   ??
       
Here the ``Dog`` class is inheriting both the ``__init__()`` method and the ``speak()`` method from
``Animal``

The next part is overriding methods, which is pretty simple:
::
   
   class Animal:

       def __init__(self, name):
           self.name = name

       def speak(self):
           return '??'

   class Dog(Animal):

       def speak(self):
           return 'woof!'

And the result is...
::

   >>> a = Animal('a')
   >>> a.speak()
   ??
   >>> tom = Dog('tom')
   >>> tom.name
   tom
   >>> tom.speak()
   woof!

Notice how ``tom`` says 'woof!' while ``a`` says '??'.  While *overriding* is simple in Python,
**overloading** is a lot more complicated.

::
   
   class Animal:

       def __init__(self, name):
           self.name = name

       def speak(self):
           return '??'

   class Dog(Animal):

       def eat(self):
           return 'Yummy!'

       def eat(self, food_name):
           if food_name == 'dogfood':
	       return 'Yummy!'
	   else:
	       return 'Disgusting!'

Testing it out, we get...
::

   >>> tom = Dog('tom')
   >>> tom.eat('dogfood')
   Yummy!
   >>> tom.eat()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: eat() takes exactly 2 arguments (1 given)

Key Notes:

* When you want to override a method, simply implement the method again in the child class
* When you try to overload a method, the last method implemented simply overrides the rest of them

We can sort of get around this with either default arguments or argument packing/unpacking:
::

   class Animal:

       def __init__(self, name):
           self.name = name

       def speak(self):
           return '??'

   class Dog(Animal):

       def eat(self, dogfood=None):
           if not dogfood or dogfood == 'dogfood':
               return 'Yummy!'
	   else:
	       return 'Disgusting!'

       def eat2(self, *args):
           if not len(*args) or args[0] == 'dogfood':
	       return 'Yummy!'
	   else:
	       return 'Disgusting!'

When we test it...
::

   >>> tom = Dog('tom')
   >>> tom.eat('dogfood')
   Yummy!
   >>> tom.eat()
   Yummy!
   >>> tom.eat('halal')
   Disgusting!
   >>> tom.eat2()
   Yummy!
   >>> tom.eat2('catfood')
   Disgusting!
 
