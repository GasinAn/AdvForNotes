# Program units

## Classifications

Program units are the fundamental components of a Fortran program. A program unit is a main program, an 
external subprogram, a module, a submodule, or an obsolescent block data program unit.

A subprogram is either a function subprogram or a subroutine subprogram. A module contains definitions that can be made accessible to other program units. A submodule is an extension of a module or another submodule; it can contain the definitions of procedures declared in a module or another submodule.

A program shall consist of exactly one main program, and any number (including zero) of other kinds of program units.

A program unit shall start with a program unit start statement, and end with a program unit end statement. A main program shall start with statement `` program `name` ``, and end with ``end program `name` ``, where `` `name` `` is the name of the Fortran program.

## Parts of program units

Briefly speaking, a program unit can be divided into parts in sequence: a program unit start statement, a USE  statement part, a IMPORT statement part, `implicit none`, a IMPLICIT statement part, a specification part, an execution part, `contains`, a contained subprogram part, and a program unit end statement. This is summarized in the following table.

| :--- |
| program unit start statement |
|     USE statement part |
|     IMPORT statement part |
|     `implicit none` |
|     IMPLICIT statement part |
|     specification part |
|     execution part |
|     `contains` |
|     contained subprogram part |
| program unit end statement |
