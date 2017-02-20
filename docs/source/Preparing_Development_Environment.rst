Preparing the Development Environment
=====================================

.. |br| raw:: html

   <br />

Which Operating System Are You Using?
-------------------------------------
  * :ref:`windows`
  * :ref:`unix`
  * :ref:`school_unix`

.. _windows:

Windows
^^^^^^^
.. note::
   ``C:\Users\Username>`` signals that you should enter the commands afterward in the command prompt.

Install Git and clone repo
~~~~~~~~~~~~~~~~~~~~~~~~~~
  * If you do not have Git installed, check the `tutorial here <https://dojo.stuycs.org/tutorials/git.htmlc>`_
    for instructions on installing it along with a brief introduction to git.
  * It is recommended for you set up your ssh keys, information can be found in the `git tutorial
    <https://dojo.stuycs.org/tutorials/git.htmlc>`_.
  * It is also recommended for you to install a UNIX terminal such as `Git Bash <https://git-for-windows.github.io/>`_
  * Create a folder for the project and clone the repo inside the directory with the following commands:

    ::

       C:\Users\Username> mkdir <name of directory>
       C:\Users\Username> cd <name of directory>
       C:\Users\Username> git clone git@github.com:StuyCSDojo/dojo-website.git

Install Python
~~~~~~~~~~~~~~
If you do not already have Python installed, download it from `here <https://www.continuum.io/downloads>`_.
Anaconda Python has a few advantages:

  * Automatically adds itself to path
  * Comes with multiple libraries pre-installed including the ones we need

Add Python and pip to path
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you have vanilla Python [#f1]_ installed, there is a chance that Python and/or pip is not in your path.
Open up command prompt and test if python and pip are in your path:

  ::

     C:\Users\Username> python --version
     C:\Users\Username> pip --version

If either command gave you an error, then you need to add them to your path.
|br|

.. _steps-to-add-path:
   
Here are the steps (You will need Administer access):

  * Open Control Panel
  * Click System and Security
  * Select System
  * Select Advanced System Settings on the left side
  * Click Environment Variables in the pop up window
  * On the bottom window, click on PATH and then click Edit
    
    * At the end of the bottom text box, add a semicolon followed by the path to the executable you need to add to the path.  For example:

      * If executing ``python --version`` gave you an error:
      
	* At the end of the bottom text box, add a semicolon followed by the path to the Python executable
      * If executing ``pip --version`` gave you an error:

	* At the end of the bottom text box, add a semicolon followed by the path to the pip executable

  * Make sure you save as you close all the pop up window.

  .. important::
     Remember to close the current terminal and open up a new one before trying out the next step.
    
  * Try executing the program again in the command prompt.  For example, if Python and/or pip was the issue, execute the following:

    ::

       C:\Users\Username> python --version
       C:\Users\Username> pip --version

It is recommended that you learn how to modify the path in Windows, but there is an alternative.  At the root
of the repo, there is a directory named devUtilities where you will find a Windows script named setPath.bat.

  * Run the script as administrator or it would ask for admin privileges.
  * When it prompts you for the path:
  
    * If both ``python --version`` and ``pip --version`` gave you errors, enter the directory where python is
      installed, a semicolon, and then directory where pip is installed
      (something like ``C:\Python27;C:\Python27\Scripts``)
    * If only ``python --version`` gave an error, enter the directory where python is installed
      (probably ``C:\Python27``)
    * If only ``pip --version`` gave an error, enter the directory where pip is installed
      (probably ``C:\Python27\Scripts``)

  * After making the necessary changes for you, it will reboot the machine so make sure you save your work!

Downloading and configuring MongoDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * Download the latest version of `MongoDB <https://www.mongodb.org/dl/win32/x86_64-2008plus-ssl>`_ (zip)
  * Extract the contents of the zip file to ``C:\mongodb`` and remove everything but the bin folder
  * Follow the instructions :ref:`above <steps-to-add-path>` for adding ``C:\mongodb\bin`` to your path
  * Create a MongoDB config file located at: ``C:\mongodb\mongo.config`` and add the following:

    ::

       ##store data here
       dbpath=C:\mongodb\data

       ##all output go here
       logpath=C:\mongodb\log\mongo.log

       ##log read and write operations
       diaglog=3

  .. important::
     The following steps requires running command prompt or powershell with administrative privileges. Right click command prompt or powershell and click ``run as
     administrator``
       
  * Create the log folder and the database folder

    ::

       C:\Users\Username> mkdir C:\mongodb\data
       C:\Users\Username> mkdir C:\mongodb\log

  * Run MongoDB as Windows Service so that it starts up with the system
    
    ::

       C:\Users\Username> mongod --config C:\mongodb\mongo.config --install
       
  * Start the MongoDB service
        
    ::

       C:\Users\Username> net start mongodb
       
  * Test the server connection with mongo.exe
        
    ::

       C:\Users\Username> mongo
       MongoDB shell version: 3.4.2
       connecting to: test
       > //mongodb shell
    
Installing and creating virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you installed Anaconda Python, you may skip this step.  Otherwise, install the virtualenv library which

  * Allows you to create isolated python environments to install libraries without cluttering the system
  * Allows you to test for compatibility with newer libraries without breaking current products.

Simply execute the following:

  ::

     C:\Users\Username> pip install virtualenv

Inside the directory containing the git repo, create a virtualenv for the dojo website:

   ::

      C:\Users\Username> virtualenv <name of virtualenv>

.. note::
   The parameter for the virtualenv command is simply a name of your choice.  The result of the command would be
   a directory.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~
You can skip this step if you installed Anaconda Python as the dependencies would already be installed.
Otherwise...

  * Activate the virtualenv

    ::

       C:\Users\Username> cd <name of virtualenv>
       C:\Users\Username> Scripts\activate

  * Install the dependencies via pip:

    ::

       C:\Users\Username> pip install -r ..\dojo-website\app\requirements.txt

.. rubric:: Footnotes
.. [#f1] Version of Python downloaded from `python.org <https://www.python.org/>`_

	 
.. _unix:

Unix
^^^^

Install Git and clone repo
~~~~~~~~~~~~~~~~~~~~~~~~~~

  * If you do not have Git installed, check the `tutorial here <https://dojo.stuycs.org/tutorials/git.htmlc>`_
    for instructions on installing it along with a brief introduction to git.
  * It is recommended for you set up your ssh keys, information can be found in the `git tutorial
    <https://dojo.stuycs.org/tutorials/git.htmlc>`_.
  * Create a folder for the project and clone the repo inside the directory with the following commands:

    ::

       $ mkdir <name of directory>
       $ cd <name of directory>
       $ git clone git@github.com:StuyCSDojo/dojo-website.git

Install Python and pip
~~~~~~~~~~~~~~~~~~~~~~
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

    * Install `homebrew <https://dojo.stuycs.org/tutorials/emacs.htmlc>`_
    * Install Python
      
      * If you did not install Python via homebrew on the current machine, execute the following command:

	::
	 
           $ brew install python
	 
      * Otherwise, update Python via the following command:

	::

           $ brew update python

Install and configure MongoDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * **Linux**

    * Ubuntu and Mint: `check here <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>`_
    * Debian: `check this <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/>`_
    * Other distros: Google it...
      
  * **Mac OSX**

    * Update Homebrew's package list

      ::

	 $ brew update

    * Install MongoDB

      ::

	 $ brew install mongodb --with-openssl

    * Configuring MongoDB

      ::

	 $ sudo mkdir -p /data/db
	 $ sudo chmod 755 /data/db

    * Run the MongoDB server and try connecting to it

      ::

	 $ mongod
	 $ mongo
	 MongoDB shell version: 3.4.2
	 > //mongo shell
	   
Install and create virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Why install virtualenv?

  * Allows you to create isolated python environments to install libraries without cluttering the system
  * Allows you to test for compatibility with newer libraries without breaking current products.

If you have not already done so in the past, do so via:

  ::

     $ sudo pip install virtualenv

     
Inside the directory containing the git repo, create a virtualenv for the dojo website:

  ::

     $ virtualenv <name of virtualenv>

.. note::
   The parameter for the virtualenv command is simply a name of your choice.  The result of the command would be
   a directory.

Install dependencies
~~~~~~~~~~~~~~~~~~~~
  * Activate the virtualenv

    ::

       // the virtualenv should be in the present directory
       $ cd <name of virtualenv>
       $ source bin/activate

  * Install the dependencies via pip:

    ::

       $ pip install -r ../dojo-website/app/requirements.txt

.. _school_unix:

School Unix
^^^^^^^^^^^

Currently under construction

Create project directory and clone repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Basic Git knowledge and the setting up of ssh keys can be `found here <https://dojo.stuycs.org/tutorials/git.htmlc>`_

* Create a separate directory to store all your work for the Dojo Website and clone the git repo:

  ::

     $ mkdir <name of directory>
     $ cd <name of directory>
     $ git clone git@github.com:StuyCSDojo/dojo-website.git
     
Create and activate virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Why use a virtualenv?

  * Allows you to create isolated python environments to install libraries without cluttering the system
  * Allows you to test for compatibility with newer libraries without breaking current products.
  * Allows you to install packages without admin privileges

Create one with the following command:

::

   $ virtualenv <name of virtualenv>

.. note::
   The parameter for the virtualenv command is simply a name of your choice.  The result of the command would be
   a directory.
   
Activate the virtualenv with the following command:

::

   $ cd /path/to/virtualenv
   $ source bin/activate

Install dependencies
~~~~~~~~~~~~~~~~~~~~
Install the dependencies via pip:

::

   $ pip install -r ../dojo-website/app/requirements.txt
