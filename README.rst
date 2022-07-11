Standard Git Library for ESMF applications.
===========================================

.. image:: https://img.shields.io/pypi/v/esmf_git.svg
    :target: https://pypi.org/project/esmf-git/
    :alt: PyPi Link

.. image:: https://github.com/ryanlong1004/emc-git/actions/workflows/pylint.yml/badge.svg
    :target: https://github.com/ryanlong1004/emc-git/actions/workflows/pylint.yml
    :alt:  Lint and Test

.. image:: https://github.com/ryanlong1004/emc-git/actions/workflows/python-publish.yml/badge.svg
   :target: https://github.com/ryanlong1004/emc-git/actions/workflows/python-publish.yml
   :alt: Upload Python Package 

.. image:: https://www.codefactor.io/repository/github/ryanlong1004/emc-git/badge/main
   :target: https://www.codefactor.io/repository/github/ryanlong1004/emc-git/overview/main
   :alt: CodeFactor

**esmf-git** is a library for implementing Git functionality inside a python application.

The ``_command_safe`` wrapper does a few things:

Foremost, the git CLI does not return robust error codes, pass or fail.  It also can return a failure for an acceptable command.  For example, calling ``git push`` raises a ``subprocess.CalledProcessError`` if there is nothing new to push.

With the wrapper, the error is first inspected.  If there is a critical error, the ``stderr`` will have a value. That value is logged at the ERROR level and the exception is re-raised.  

If ``stderr`` is **None**, a ``subprocess.CompletedProcess`` is created and returned in order to stay persistent with the standard successful return object.

``stdout`` is always logged at the INFO level is a ``subprocess.CalledProcessError`` is raised.

The wrapper also provides a backwards compatible way of handling output streams, raises an exception if return code is not 0, and sets the default encoding.


Basic Usage
-----------

::

    import esmf_git as git

    result = git.status("/path/to/repo") 
    print(result) # equivalent to 'git status'



Installation
------------

::

    $ pip install esmf-git
