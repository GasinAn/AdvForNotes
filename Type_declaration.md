# Type declaration

## Attributes of data objects and procedures

Every "data object", such as a constant or as variable, has a type and rank and can have type parameters and other properties that determine the uses of the object. Collectively, these properties are the attributes of the object.

A function has a type and rank and can have type parameters and other attributes that determine the uses of the function. The type, rank, and type parameters are the same as those of the function result. A subroutine does not have a type, rank, or type parameters, but can have other attributes that determine the uses of the subroutine.

Commonly, if we say "an attribute", actually it refers to an attribute which is not a type, rank, or a type parameter. Please note that the "attribute" in Fortran is not the "attribute" in other languages such as Python.

## Type declaration statement

The type declaration statement in Fortran must be added in the specification part.

The type declaration statement in Fortran `` `type-declaration-stmt` `` should be in in following form.
```
`type-declaration-stmt` := `declaration-type-spec`{, `attr-spec`}... :: `entity-decl`{, `entity-decl`}...
```
If there are no `` , `attr-spec` ``, `::` may be able to be omitted, but I suggest you to always add `::` in the type declaration statement, or you will often face troubles.

The `` `declaration-type-spec` `` specifies the type and type parameters. An `` `attr-spec` `` specifies an attribute. An `` `entity-decl` `` should be in following form.
```
`entity-decl` := `object-name`{(`array-spec`)}{[`coarray-spec`]}{*`char-length`} {`initialization`}
              || `function-name`{*`char-length`}
```
The `` `char-length` `` specifies the length of a variable, a named constant, or a function result of character type, but I suggest that it is not good for you to add it in the type declaration statement, because it is not modern. The `` `entity-decl` `` which you add in the Fortran program should be in following form.
```
`entity-decl` := `object-name`{(`array-spec`)}{[`coarray-spec`]} {`initialization`}
              || `function-name`
```
The `` `object-name` `` specifies the name of a variable or a named constant, and the `` `function-name` `` specifies the name of a function. The `` (`array-spec`) `` specifies the rank and the bounds of indexes of an array. The `` [`coarray-spec`] `` specifies the rank and the bounds of indexes of a coarray. The `` `initialization` `` specifies the initialization.

The `` `initialization` `` should be in following form.
```
`initialization` := = `constant-expr`
                 || => null()
                 || => `initial-data-target`
```
The `` = `constant-expr` `` specifies that a normal variable or a normal named constant is initialized by assignment from `constant-expr`. The `` => null() `` specifies that a pointer is initialized by nullified, i.e., disassociated. The `` => `initial-data-target` `` specifies that a pointer is initialized by associated to `` `initial-data-target` ``.

## Explicit initialization and the SAVE attribute

The appearance of `` `initialization` `` in an `` `entity-decl` `` for a variable specifies that the variable is with explicit initialization. WARNING: Explicit initialization of a variable that is not in an obsolescent common block IMPLIES the SAVE attribute, and a variable which has the SAVE attribute in a procedure will be equivalent to a static local variable in C. This implication often cause misunderstanding, and I suggest that you should only add the `` `initialization` `` when you have explicitly specified the SAVE attribute, or the PARAMETER attribute (The PARAMETER attribute specifies that the `` `object-name` `` is not the name of a variable but a name of a named constant), by adding an `` `attr-spec` ``. For example, it is proper for you to write the following three programs,
```fortran-free-form
program main
    implicit none
    call print_zero()
end program main

subroutine print_zero()
    integer :: zero
    zero = 0
    print *, zero
end subroutine print_zero
```
```fortran-free-form
program main
    implicit none
    call print_zero()
end program main

subroutine print_zero()
    integer, save :: zero = 0
    print *, zero
end subroutine print_zero
```
```fortran-free-form
program main
    implicit none
    call print_zero()
end program main

subroutine print_zero()
    integer, parameter :: zero = 0
    print *, zero
end subroutine print_zero
```
but it is not proper for you to write the following program.
```fortran-free-form
program main
    implicit none
    call print_zero()
end program main

subroutine print_zero()
    integer :: zero = 0 ! Implies the SAVE attribute!
    print *, zero
end subroutine print_zero
```
