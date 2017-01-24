Preparing the Development Environment
**************************************

.. |br| raw:: html

   <br />
       
*Windows*
#########
  Notation:
    * ``C:\Users\Username>`` signals that you should enter the commands afterward in the command prompt.
    
  * **Install Git and clone the Dojo Website repo**

    * If you do not have Git installed, check the `tutorial here <http://dojo.stuycs.org/tutorials/git.htmlc>`_
      for instructions on installing it along with a brief introduction to git.
    * It is recommended for you set up your ssh keys, information can be found in the `git tutorial
      <http://dojo.stuycs.org/tutorials/git.htmlc>`_.
    * Create a folder for the project and clone the repo inside the directory with the following commands:
            
      ::

	 C:\Users\Username> mkdir <name of directory>
	 C:\Users\Username> cd <name of directory>
         C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-website.git
         
  * **Install Python**
    |br|
    If you do not already have Python installed, download it from `here <https://www.continuum.io/downloads>`_. 
    Anaconda Python has a few advantages:

    * Automatically adds itself to path
    * Comes with multiple libraries pre-installed including the ones we need: flask and sphinx

  * **Add Python and pip to path**
    |br|
    If you have vanilla Python [#f1]_ installed, there is a chance that Python and/or pip is not in your path.
    Open up command prompt and test if python and pip are in your path:

    ::

       C:\Users\Username> python --version
       C:\Users\Username> pip --version

    If either command gave you an error, then you need to add them to your path.
    |br|
    Here are the steps (You will need Administer access):

    * Open Control Panel
    * Click System and Security
    * Select System
    * Select Advanced System Settings on the left side
    * Click Environment Variables in the pop up window
    * On the bottom window, click on PATH and then click Edit

      * If executing ``python --version`` gave you an error:

	* At the end of the bottom text box, add a semicolon followed by the path to the Python executable

      * If executing ``pip --version`` gave you an error:
	
	* At the end of the bottom text box, add a semicolon followed by the path to the pip executable
    * Make sure you save as you close all the pop up window.
    * Close the current command prompt and open up another one
    * Try executing Python and/or pip again in the command prompt:

      ::

	 C:\Users\Username> python --version
	 C:\Users\Username> pip --version

    It is recommended that you learn how to modify the path in Windows, but there is an alternative.  At the root
    of the repo, there is a directory named devUtilities where you will find a Windows script named setPath.bat.

    * Run the script as administrator or it would ask for admin privileges.
    * When it prompts you for the path:

      * If both ``python --version`` and ``pip --version`` gave you errors, enter the directory where python is
	installed, a semicolon, and then directory where pip is installed
	(something like C:\\Python27;C:\\Python27\\Scripts)
      * If only ``python --version`` gave an error, enter the directory where python is installed
	(probably C:\\Python27)
      * If only ``pip --version`` gave an error, enter the directory where pip is installed
	(probably C:\\Python27\\Scripts) 

    * After making the necessary changes for you, it will reboot the machine so make sure you save your work!
    
  * **Installing and creating virtualenv**
    |br|
    If you installed Anaconda Python, you may skip this step.  Otherwise, install the virtualenv library which

      * Allows you to create isolated python environments to install libraries without cluttering the system
      * Allows you to test for compatibility with newer libraries without breaking current products.

    Simply execute the following:
    
    ::
       
       C:\Users\Username> pip install virtualenv
     
    Inside the directory containing the git repo, create a virtualenv for the dojo website (the result would be a
    directory):

    ::

       C:\Users\Username> virtualenv <name of virtualenv>

  * **Installing dependencies**
    |br|
    You can skip this step if you installed Anaconda Python as the dependencies would already be installed.
    Otherwise...

    * Activate the virtualenv

      ::

         C:\Users\Username> cd <name of virtualenv>
	 C:\Users\Username> Scripts\activate
      
    * Install the dependencies via pip:

      ::

         C:\Users\Username> pip install -r ..\dojo-website\requirements.txt

.. rubric:: Footnotes
	      
.. [#f1] Version of Python downloaded from `python.org <https://www.python.org/>`_

*Unix*
######
  * **Install Git and clone the Dojo website repo**

    * If you do not have Git installed, check the `tutorial here <http://dojo.stuycs.org/tutorials/git.htmlc>`_
      for instructions on installing it along with a brief introduction to git.
    * It is recommended for you set up your ssh keys, information can be found in the `git tutorial
      <http://dojo.stuycs.org/tutorials/git.htmlc>`_.
    * Create a folder for the project and clone the repo inside the directory with the following commands:

      ::
	 
         $ mkdir <name of directory>
	 $ cd <name of directory>
	 $ git clone git@github.com:StuyCSDojo/dojo-website.git
	 
  * **Install Python and pip**
    
    * **Linux**
      |br|
      Check if Python is already installed by running the following in a terminal (``Ctrl-Alt-T``):
    
      ::

	 $ python --version

      If the command does not return an error, make sure that the version reported is in the format of 2.x.x.
      Most distros ship with Python2 by default.  If yours does not (currently Arch Linux & Gentoo), do whatever
      you need to install Python2 (or use `pyenv <https://github.com/yyuu/pyenv>`_)
      |br|
      |br|
      Pip is the package manager for Python and we need it to install extra libraries.

      * On Ubuntu/Mint/Debian system:

	::

	   $ sudo apt-get install python-pip

      * On Fedora 21:

	::

	   $ sudo yum upgrade python-setuptools
	   $ sudo yum install python-pip python-wheels

      * On Fedora 22:

	::

	   $ sudo dnf upgrade python-setuptools
	   $ sudo dnf install python-pip python-wheels

      * If you are using some other distro, you probably know how to install Python/pip.
    * **Mac OS**

      * Install `homebrew <http://dojo.stuycs.org/tutorials/emacs.htmlc>`_
      * Install Python

	* If you did not install Python via homebrew on the current machine, execute the following command:

	  ::

	     $ brew install python

	* Otherwise, update Python via the following command:

	  ::
	     
	     $ brew update python
             
  * **Install and create virtualenv**
    |br|
    Why install virtualenv?

      * Allows you to create isolated python environments to install libraries without cluttering the system
      * Allows you to test for compatibility with newer libraries without breaking current products.
        
    If you have not already done so in the past, do so via:
    
    ::

       $ sudo pip install virtualenv

    Inside the directory containing the git repo, create a virtualenv for the dojo website (the result would be a
    directory):

    ::

       $ virtualenv <name of virtualenv>
       
  * **Install dependencies**

    * Activate the virtualenv

      ::

	 // the virtualenv should be in the present directory
	 $ cd <name of virtualenv>
	 $ source bin/activate

    * Install the dependencies via pip:

      ::

	 $ pip install -r ../dojo-website/requirements.txt
