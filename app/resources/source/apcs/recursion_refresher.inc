Recursion: A Refresher
======================

.. |br| raw:: html

   <br />

Outline
-------
  * :ref:`what_is_recursion`
  * :ref:`base_case`
  * :ref:`what_is_head_recursion`
  * :ref:`example_of_head_recursion`
  * :ref:`what_is_tail_recursion`
  * :ref:`what_are_state_variables`
  * :ref:`example_of_tail_recursion`

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
  * Typically return a simple constant of some form (a number, a string, etc)

    * Sample values for integers: 0, 1, 2
    * Sample values for Strings: " ", "a", ""
    * Sample values for Arrays: [], [0]

.. _what_is_head_recursion:

What is a Head Recursive Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The first form of recursion you learn was head recursion and is characterize by:

  * Deferred operations: operations that cannot be evaluated because not all parameters are defined

    * This causes the stack to grow until we reach the base case

  * No wrapper functions: We do not store the answer in a variable
  * All data are processed after the recursive call
  * May be more memory intensive

.. _example_of_head_recursion:

Example of Head Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: java

   public static int factorial(int n){
       if (n < 2){
           return n;
       }else{
           return n * factorial(n - 1);
       }
   }

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

.. _example_of_tail_recursion:

Example of Tail Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: java

   public static int factorial(int n){
       return factorialHelper(n, 1);
   }
		
   public static int factorialHelper(int n, int answer){
       if (n < 2){
           return answer;
       }else{
           return factorial(n - 1, answer * n);
       }
   }
