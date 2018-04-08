PyChan 3
========

Topics Covered
--------------
  * :ref:`print_statements`
  * :ref:`range`
  * :ref:`division`
  * :ref:`contains`
  * :ref:`input`
  * :ref:`keeping_compability`

.. _print_statements:

You Must Call Print or Die
^^^^^^^^^^^^^^^^^^^^^^^^^^
In Python 2, you are used to doing:
::

   >>> print 'hi'
   hi

In Python 3, if you try that...
::

   >>> print 'hi'
     File "<stdin>", line 1
       print 'hi'
                ^
   SyntaxError: Missing parentheses in call to 'print'
   >>> print('hi')
   hi

Key Note:

  * ``print`` is now a function in Python 3 and requires parentheses

.. _range:

The Letter X is Bad
^^^^^^^^^^^^^^^^^^^
In Python 2, there exists a more memory efficient brother to ``range()`` named ``xrange()``.  The syntax
for ``xrange()`` is the same as ``range()``.
::

   >>> for i in range(5):
   ...     print i
   ...
   0
   1
   2
   3
   4
   >>> for i in xrange(5):
   ...     print i
   ...
   0
   1
   2
   3
   4
   >>>

``xrange()`` generates the each element of the sequence as you need it instead of holding everything in
memory at once.

In Python 3,  ``xrange()`` has been removed and the new ``range()`` does the same thing as the old
``xrange()``.

.. _division:

The Furrows of War
^^^^^^^^^^^^^^^^^^
In Python 2, the ``/`` operator performs integer division when both operands are integers.  In Python 3,
all calculations done with the ``/`` operator are "true division".

**True Division** refers to the standard mathematical division.  In true division:

  * 5 / 2 = 2.5
  * 6 / 2 = 3
  * 5.0 / 2 = 2.5
  * 6.0 / 2 = 3.0

Recall that in Python 2, the ``/`` operator might result in an **integer division** or a *floating-point
division*...
::

   >>> 5 / 2    # Integer division
   2
   >>> 5.0 / 2  # Floating-Point division
   2.5

.. _contains:

Containing Things is Good
^^^^^^^^^^^^^^^^^^^^^^^^^
In Python 3, ``range()`` now has a ``__contains__`` method allowing faster looks-up than Python 2:
::

   >>> n in range(6, 10) # check if n is inside the interval, [6, 10)

In Python 2, you can still do: ``n in range(6, 10)``, but it would be a lot slower.

.. _input:

Your Input Would Affect Our Decisions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In Python 2, the ``input()`` method would evalulate what the user enters.  This can be dangerous as it
allows for arbitrary code execution.  Here is an example:
::

   >>> user_input = input("Choose a number: ")
   Choose a number: [x for x in xrange(10)]
   [0, 1, 2, 3, 4, 5, 6, 7,8, 9]
   >>>

In Python 3, the ``input()`` method would store the value as a string, allowing you to check for
malicious input.  The Python 2 equivalence would be ``raw_input()``.  To get the old behavior of
``input()`` (which is not recommended), use ``eval(input())``.

.. _keeping_compability:

We Like Being Compatible
^^^^^^^^^^^^^^^^^^^^^^^^
It is possible to access some of the Python 3 goodies in Python 2 by inserting the following statements at
the very top:

::

   # Future statements must be the very first statement below module docstrings, comments, blank lines,
   # and other future statements
   from __future__ import print_function # grant access to Python 3 print function
   from __future__ import division       # grant access to Python 3 true divison operator

   def test():
       print('hello')
       print(5 / 2)

If we were to run ``test()`` in a Python 2 environment...
::

   >>> test()
   hello
   2.5

