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

ignore_failure
  ignore non-zero exit status; default throws an exception

silent
  do not produce output on stdout or stderr; default echoes output to
  ``sys.stdout`` and ``sys.stderr``

silent_stdout
  do not produce output on stdout

silent_stderr
  do not produce output on stderr

stdin_from
  file object to act as command's stdin; default ``sys.stdin``

tee_stdin
  file object to duplicate stdin on

tee_stdout
  file object to duplicate stdout on; this file will be written to even in
  silent mode

tee_stderr
  file object to duplicate stderr on; this file will be written to even in
  silent mode

User may re-configure CommandRunner after creation, but this is always
done through a context manager. For example:

.. code:: python

  cmdrunner.run('echo', 'you can see this')
  with cmdrunner.configure(silent=true):
    cmdrunner.run('echo', 'you cannot see this')
  cmdrunner.run('echo', 'you can see this too')

Conceptually, the user does not inspect the output or return status of a
command. Therefore, the command API:

- always returns ``None``
- never buffers command output in memory; it is suitable for commands
  that run forever or produce infinite output

Running a command is a blocking operation. Commands do not run in the
background (use ``AsyncCommandRunner`` for that).
