===================
Goals and Non-Goals
===================

Bash (and shell scripting languages in general) make it incredibly easy
to run any program available in the operating system. However, Bash has
the following drawbacks:

- There is no concept of a *package*, *module*, or *library*, making it
  difficult to reuse code in a different context.

- There is no standard way to install a Bash script, or a set of related
  Bash scripts.

- There is no standard way to specify the dependencies of a Bash script.

- There is no dependency resolution tool for Bash scripts.

- There is no repository of reusable Bash scripts or functions.

The Python ecosystem solves all of these reuse, packaging, and
distribution problems. However, it is difficult to run arbitrary
programs in Python. Python's ``subprocess`` module presents a low-level
API for running subprocesses, but is not convenient for day-to-day
scripting.

The goal of ``scriptutils`` is to enable Bash-like simplicity within the
Python packaging and distribution ecosystem. ``scriptutils`` is not
limited to only implementing Bash features; any feature which makes
general scripting more convenient is potentially within the scope of
``scriptutils``.

Goals
=====

This section outlines specific features that ``scriptutils`` would like
to support in the near future.

commands
--------

Support **commands** with the ``CommandRunner`` class. User creates and
configures ``CommandRunner``, then runs commands by passing a variable
number of strings to the ``run()`` method.

Configuration options include:

``nonzero_exit='throw' (str)``
  action to take on non-zero exit status
    - ``'throw'``: throw exception on non-zero exit status
    - ``'ignore'``: ignore non-zero exit status

``print=True (bool)``
  alias to control both ``print_stdout`` and ``print_stderr`` options

``print_stdout (bool)``
  print command's stdout on ``sys.stdout``

``print_stderr (bool)``
  print command's stderr on ``sys.stderr``

``stdin=sys.stdin (file)``
  readable file object to act as command's stdin

``stdin_log=None (file)``
  writable file object to duplicate command's stdin

``stdout_log=None (file)``
  writable file object to duplicate command's stdout

``stderr_log=None (file)``
  writable file object to duplicate command's stderr

Conceptually, a ``CommandRunner`` is configured in its constructor, and
is immutable after creation. The only way to re-configure a
``CommandRunner`` after construction is through a context manager. For
example:

.. code:: python

  cmdrunner.run('echo', 'you can see this')
  with cmdrunner.reconfigure(silent=true):
    cmdrunner.run('echo', 'you cannot see this')
  cmdrunner.run('echo', 'you can see this too')

Conceptually, the user does not inspect the output or return status of a
command. Therefore, the ``CommandRunner`` API:

- always returns ``None``
- never buffers command output in memory; it is suitable for commands
  that run forever or produce infinite output

Running a command is a blocking operation. Commands do not run in the
background. As a result, you cannot pipe the output of one command to
the input of another.
