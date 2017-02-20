Introduction to Recursion
=========================

.. |br| raw:: html

   <br />

Outline
-------
  * :ref:`what_is_recursion`
  * :ref:`base_case`
  * :ref:`tips_for_base_case`
  * :ref:`tips_for_recursive_reduction`
  * :ref:`what_is_head_recursion`
  * :ref:`tips_for_head_recursion`
  * :ref:`sample_workflow_for_head_recursion`
  * :ref:`what_is_tail_recursion`
  * :ref:`what_are_state_variables`
  * :ref:`tips_for_tail_recursion`
  * :ref:`sample_workflow_for_tail_recursion`

.. _what_is_recursion:

What is Recursion
^^^^^^^^^^^^^^^^^
A **recursive function** is a function that calls itself during the recursive reduction until it has reached a
base case. **Recursive reduction** is the process of breaking down a larger problem into smaller pieces each time
until you reach the base case.

.. _base_case:

What is a Base Case
^^^^^^^^^^^^^^^^^^^
A **base case** is sometimes refer to as the exit case.  It should:

  * **NOT** be expressed in terms of itself
  * Typically return a constant of some form (a number, a string, etc)
  
.. _tips_for_base_case:

Tips for Finding the Base Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Define the problems in spoken English/mathematical terms first
  * Trace through an example, at what point can you not define the function in terms of itself
  * Remember that a base case should not involve any unknown variables
  * Think about the data types that the problem uses

    * Examples include, but are not limited to: floating-point numbers, Strings, Arrays, integers
  
  * Use the simplest value in the data type and see if you can derive a base case out of it

    * Sample values for integers: 0, 1, 2
    * Sample values for Strings: " ", "a", ""
    * Sample values for Arrays: [], [0]

.. _tips_for_recursive_reduction:

Tips for Finding the Recursive Reduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Draw a trace diagram and think of how you can break the problem into smaller pieces with each recursive call
  * Figure out the base case first, using the tips :ref:`above <tips_for_base_case>`

    * Think about a problem that is slightly more complex than the base case.  How can you reduce it to the base
      case?

.. _what_is_head_recursion:

What is a Head Recursive Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The first form of recursion you learn was head recursion and is characterize by:

  * Deferred operations: operations that cannot be evaluated because not all parameters are defined

    * This causes the stack to grow until we reach the base case

  * No wrapper functions: We do not store the answer in a variable
  * All data are processed after the recursive call
  * May be more memory intensive

.. _tips_for_head_recursion:

Tips for Writing Head Recursive Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Formulate the base case and the recursive reduction first
  * Draw a few flowcharts or trace through a few examples to solidify your algorithm and your understanding of how
    everything fits together
  * Write your algorithm in psuedocode, this gives you a solid outline to build up without worrying about the
    syntax and also tests your understanding of your own algorithm

.. _sample_workflow_for_head_recursion:

Sample Workflow for Head Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Under Construction

.. _what_is_tail_recursion:

What is a Tail Recursive Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The second form of recursion that you might have covered is characterized by:

  * **NO** deferred operations
  * Usage of :ref:`state variables <what_are_state_variables>`
  * All data are processed before the recursive call

.. _what_are_state_variables:
   
What are State Variables
^^^^^^^^^^^^^^^^^^^^^^^^
State variables are normal variables with a specific role in a function.  They allow us to:

  * Keep track of specific parts of the function such as the answer or the counter
  * Use the aforementioned data to continue an interrupted recursive call

Some of the most commonly asked questions about state variables are:

  * How many state variables should you use?

    * Answer: There is no definite answer. Generally, you will need one to keep track of the answer and maybe
      another for a counter.  Use however many you feel is necessary.

  * Am I doing it wrong if I use more state variables than my classmate?

    * Answer: The most important attribute of a good program is that it works correctly.  Do not worry if your
      classmate uses less state variables (especially if their solution is wrong).  With more practice, you will
      realize how to trim away unnecessary state variables.

.. tip::
   Keep in mind that more state variables can improve the readability of your code.

.. _tips_for_tail_recursion:

Tips for Writing Tail Recursive Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Writing a tail recursive function is very similar to writing a head recursive function, so start by coming up with
the recursive reduction and the base case.  Afterward:

  * Remember that tail recursion differs from head recursion in that it modifies the parameter with each recursive
    call
  * Instead of performing the operation on the recursive call, do it directly to the parameter

.. _sample_workflow_for_tail_recursion:

Sample Workflow for Tail Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Under Construction

Factorial Example (using the first idea)

Define the problem in normal English/mathematical terms. 
Since this is a math problem you would probably come up with something like:
n * (n - 1)! or n * n-1 * n-2 * ... * 1
From your definitions, attempt to eliminate all the unknowns except for the result. So, how can we get rid of n, n - 1, n - 2, etc?
Well, if n = 1, then there is no n - 1, n - 2, n - 3, etc. So, now you got 1! = 1.
So, if n = 1, then it should return 1.

Factorial Example (using idea 3)

What data types does the result fall under?
Since n! always results in an integer, the data type would be integers.
Use the simplest value for step 1.
So we want the simplest value for integers (the result of step 1). Let's make it positive for simplicity and a simple integer should only be single-digit. To make it even simpler, let us choose 0 or 1.

Well 1! = 1 and 0! = 1, so we can conclude that:

(if (< n 2) ; base case
    n
    <do whatever> ) 
