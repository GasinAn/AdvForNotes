# "Hello, world!"

Here is the "Hello, world!" example of Fortran.

```fortran-free-form
program main
    implicit none
    print *, 'Hello, World!'
end program main
```

- Every Fortran program executes from `` program `name` `` to ``end program `name` ``, where `` `name` `` is the name of the Fortran program. "Names" (such as variable names, procedure names and module names) in Fortran must be formed by letters, digits and underscore "\_", and must start with a letter (which means "\_\_main\_\_" is not a valid "name").

- ``implicit none`` bans the confusing "I-N implicit declaration rule" of Fortran. It is a good habit to add ``implicit none`` in every Fortran program, even if nothing is declared in the program.

- ``print`` makes an output to "file with unit \*", which is usually the screen. "\*," means that the output is in "format \*", which will be automatically determined by the processor with some restrictions of Fortran standard.
