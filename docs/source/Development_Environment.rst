Preparing the Development Environment
**************************************

.. |br| raw:: html

   <br />
    
*Linux*
#######
  * **Python is most likely installed by default.**
    |br|
    To check if this is the case, open up a terminal (``Ctrl-Alt-T``):

    ::

       $ python --version

    If the command does not return an error, make sure that the version reported is in the format of 2.x.x.  Most
    distros ship with Python2 by default.  If yours does not (currently Arch Linux & Gentoo), do whatever you need
    to install Python2 (or use `pyenv <https://github.com/yyuu/pyenv>`_)
    
  * **If you are using the default installation of Python, install pip.**
    |br|
    Pip is the package manager for Python and we need it to install extra libraries.

    * On Ubuntu/Debian/Mint system:

      ::
	 
	 $ sudo apt-get install python-pip

    * On Fedora 21:

      ::
	 
	 $ sudo yum upgrade python-setuptools
	 $ sudo yum install python-pip python-wheel

    * On Fedora 22+:

      ::

	 $ sudo dnf upgrade python-setuptools
	 $ sudo dnf install python-pip python-wheel

    * If you are using some other distro, you probably know how to install Python/pip.

  * **Install virtualenv**
    |br|
    Virtualenv allows one to create an isolated Python environment local to you which means you do not have to
    install extra libraries globally as that is not a good idea.  It also allows you to freeze the versions of
    these libraries so that you do not accidentally upgrade your package.  Do so via:

    ::

       $ pip install virtualenv
       
  * **Install flask and sphinx**
    |br|
    To check if you need to install either library, run the following commands in a terminal:

    ::

       $ python
       >>> import flask
       >>> import sphinx
       >>> exit()
       
    If either import statement throw an error, you would need to install the corresponding library:
    |br|
    For flask:

    ::

       $ sudo pip install flask

    For sphinx:

    ::

       $ sudo pip install sphinx==1.4.8

    We are using version 1.4.8 as the latest version seems to have trouble building the documentation.

Mac OSX
#######
  * **Install** `homebrew <http://dojo.stuycs.org/tutorials/emacs.htmlc>`_
  * **Install Python**
    * If you did not install Python with homebrew with the current machine before, execute the following command:

    ::

       $ brew install python

    * If you have already installed Python with homebrew, update it with:

    ::

       $ brew update python

  * Install flask and sphinx
    |br|
    First, let us check if that is necessary.
    ::

       $ pip freeze | grep flask
       $ pip freeze | grep sphinx

    If either of the import statement failed, you need to install the corresponding library.
    |br|
    For flask:

    ::

       $ pip install flask

    For sphinx:

    ::
       
       $ pip install sphinx==1.4.8

*Windows*
#########
  * **Install Python**
    |br|
    If you do not already have Python installed, download it from `here <https://www.continuum.io/downloads>`_. 
    Anaconda Python has a few advantages:

    * Automatically adds itself to path
    * Comes with multiple libraries pre-installed including the ones we need: flask and sphinx

  * **Add Python and pip to path**
    |br|
    If you have vanilla Python [#f1]_ installed, there is a chance that Python and/or is not in your path.  Open
    up command prompt and try executing python and then pip:

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
    
  * **Installing and Creating virtualenv**
    |br|
    If you installed Anaconda Python, you may skip this step.  Otherwise, you should install the virtualenv
    library which allows you to create isolated python environments and install extra libraries without cluttering
    your system.  It also allow you to test for compability with newer libraries without breaking current
    products.  Simply execute the following:
    
    ::

       C:\Users\Username> pip install virtualenv
     
    Create a project folder for the dojo website.  Inside that directory, create a virtualenv for the dojo
    website like this (a directory would be created):

    ::

       C:\Users\Username> virtualenv <name of virtualenv>

  * **Installing Git and Cloning the Dojo Website repo**
    |br|
    

    * If you do not have git installed, check the `tutorial here <http://dojo.stuycs.org/tutorials/git.htmlc>`_
      for instructions on installing it along with a brief introduction to git.
    * If you has not done so yet, create a folder for the project.  Inside that directory, clone the repo with the
      following command:

      ::

	 C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-website.git
    
  * **Installing dependencies**
    |br|
    You can skip this step if you installed Anaconda Python as the dependencies for this project would already be
    installed.  Otherwise:

    * Activate the virtualenv

      ::

	 C:\Users\Username> cd path\to\virtualenv\created\earlier
	 C:\Users\Username> Scripts\activate
	 
    * Copy the requirements.txt file at the root of the git repository to the virtualenv directory
    * Inside the virtualenv directory, install the dependencies via pip:

      ::

	 C:\Users\Username> pip install -r requirements.txt

.. rubric:: Footnotes
	      
.. [#f1] Version of Python downloaded from `python.org <https://www.python.org/>`_
