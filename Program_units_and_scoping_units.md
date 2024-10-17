# Program units and scoping units

## Program units

### Classifications

Program units are the fundamental components of a Fortran program. A program unit is a main program, an 
external subprogram, a module, a submodule, or an obsolescent block data program unit.

A subprogram is either a function subprogram or a subroutine subprogram. A module contains definitions that can be made accessible to other program units. A submodule is an extension of a module or another submodule; it can contain the definitions of procedures declared in a module or another submodule.

A program shall consist of exactly one main program, and any number (including zero) of other kinds of program units.

A program unit shall start with a program unit start statement, and end with a program unit end statement. A main program shall start with statement `` program `name` ``, and end with ``end program `name` ``, where `` `name` `` is the name of the Fortran program.

### Parts of program units

Briefly speaking, a program unit can be divided into parts in sequence: a program unit start statement, a USE  statement part, a IMPORT statement part, `implicit none`, a IMPLICIT statement part, a specification part, an execution part, `contains`, a contained subprogram part, and a program unit end statement. This is summarized in the following table.

| :--- |
| Program unit start statement |
| &nbsp; &nbsp; &nbsp; &nbsp; USE statement part |
| &nbsp; &nbsp; &nbsp; &nbsp; IMPORT statement part |
| &nbsp; &nbsp; &nbsp; &nbsp; `implicit none` |
| &nbsp; &nbsp; &nbsp; &nbsp; IMPLICIT statement part |
| &nbsp; &nbsp; &nbsp; &nbsp; Specification part |
| &nbsp; &nbsp; &nbsp; &nbsp; Execution part |
| &nbsp; &nbsp; &nbsp; &nbsp; `contains` |
| &nbsp; &nbsp; &nbsp; &nbsp; Contained subprogram part |
| Program unit end statement |

## Scoping units

Any program unit, excluding all nested scoping units in it, is a scoping unit. Any BLOCK construct, derived-type definition, interface body, or internal subprogram, excluding all nested scoping units in it, is a nested scoping unit. I would not like to discuss internal subprograms, since they are confusing, and I will discuss derived-type definitions and interface bodies later.

A BLOCK construct must be added in the execution part of another scoping unit. It has its own USE statement part, IMPORT statement part, specification part, and execution part. Anything defined in the scoping unit which contains the BLOCK construct is available in the BLOCK construct, while anything defined in the BLOCK construct is not available in scoping unit which contains the BLOCK construct. For example, in the following program, `x` and `y` are available in (the execution part of) the whole main program, while `tmp` is only available in (the execution part of) the BLOCK construct.
```fortran-free-form
program main
    implicit none
    integer :: x, y
    x = 1
    y = 2
    block
        integer :: tmp
        tmp = x
        x = y
        y = tmp
    end block
    print *, x
    print *, y
end program main
```
