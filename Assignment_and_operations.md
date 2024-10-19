# Assignment and operations

## Assignment

Assignment in Fortran can be intrinsic assignment and defined assignment. We discuss intrinsic assignment here and defined assignment in another chapter.

As in many other programming languages, use `=` to make assignment. Fortran is strongly typed, implicit type conversions between numeric types and nonnumeric intrinsic types are prohibited.

If we want to use a deferred-length character, we would have needed to use a lot of ALLOCATE statements and DEALLOCATE statements as in the following program.
```fortran-free-form
program main
    implicit none
    character(:), allocatable :: char
    allocate(character(len('allocated')) :: char)
    char = 'allocated'
    print *, char, len(char), len('allocated')
    deallocate(char)
    allocate(character(len('reallocated')) :: char)
    char = 'reallocated'
    print *, char, len(char), len('reallocated')
end program main
```
While in Fortran, a deferred-length character can always be automatically allocated and reallocated to have a proper length.
```fortran-free-form
program main
    implicit none
    character(:), allocatable :: char
    char = 'allocated' ! Automatically allocated.
    print *, char, len(char), len('allocated')
    char = 'reallocated' ! Automatically reallocated.
    print *, char, len(char), len('reallocated')
end program main
```

The kind and length conversion rules of intrinsic assignment are given in paragraph 9--11 of subsubsection 10.2.1.3 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf).

We can assign to `` `z`%re `` and `` `z`%im `` to assign to the real and imaginary part of `` `z` `` respectively.
```fortran-free-form
program main
    implicit none
    complex :: i
    i%re = 0.0
    i%im = 1.0
    print *, i
end program main
```

We can assign to `` `char`({`start`}:{`stop`}) `` (NOT `` `char`[{`start`}:{`stop`}] ``) to assign to only the `` `start` ``th--`` `stop` ``th characters of `` `char` `` (The `` `stop` ``th character is INCLUDED). If `` `start` `` is omitted, it will be `1`. If `` `stop` `` is omitted, it will be `` len(`char`) ``.
```fortran-free-form
program main
    implicit none
    character(13) :: hello_world
    hello_world = 'hello, world!'
    hello_world(1:1) = 'HELLO, WORLD!'
    print *, hello_world
end program main
```
However, if `` `char` `` is itself a deferred-length character, assignment to `` `char`({`start`}:{`stop`}) `` NEVER make `char` allocated and reallocated, and the following program is not valid.
```fortran-free-form
program main
    implicit none
    character(:), allocatable :: char
    char(:) = 'allocated' ! NOT automatically allocated.
    print *, char, len(char), len('allocated')
    char(:) = 'reallocated' ! NOT automatically reallocated.
    print *, char, len(char), len('reallocated')
end program main
```

## Operations

An operation in Fortran can be an intrinsic operation and a defined operation. We discuss intrinsic operations here and defined operations in another chapter.

There are four types of intrinsic operations: numeric operations, the character operation, logical operations, and relational operations. As in many other programming languages, `(` and `)` are used to change the priority of operators

### Numeric operations

As in many other programming languages, binary operator `+`, `-`, `*`, `/`, and `**` stand for addition, subtraction, multiplication, and exponentiation respectively, and unary operator `+` and `-` stand for  identity and negation respectively. `` `a`**`b`**`c` `` is `` `a`**(`b`**`c`) ``. It does not permit expressions containing two consecutive numeric operators, such as `` a**-b `` or `` a+-b ``. However, expressions such as `` a**(-b) `` or `` a+(-b) `` are permitted.

The result of an operation with two operands of type integer is the "round to \\(0\\)" of the mathematical quotient. If `` `x1` `` and `` `x2` `` are of type integer and `` `x2` `` has a negative value, the interpretation of `` `x1` ** `x2` `` is the same as the interpretation of `` 1 / (`x1`**abs(`x2`))`` (`1` is of type integer), which is subject to the rules of integer division. In the case of a complex value raised to a complex power, the value of the operation `` `x1` ** `x2` `` is the principal value.

The type and kind conversion rules of intrinsic numeric operations are given in table 10.2 and paragraph 1 of subsubsubsection 10.1.5.2.1 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf).

### The character operation

The character intrinsic operator ``//`` is used to concatenate two operands of type character (with the same kind type parameter).

### Logical operations

Binary operator `.not.`, `.and.`, `.or.`, `.eqv.`, and `.neqv.` stand for logical negation, conjunction, inclusive disjunction, equivalence, and nonequivalence respectively. No space can appear front of or behind `not`, `and`, `or`, `eqv`, and `neqv` in `.not.`, `.and.`, `.or.`, `.eqv.`, and `.neqv.`.

### Relational operations

Binary operator `.lt.`/`<`, `.le.`/`<=`, `.gt.`/`>`, `.ge.`/`>=`, `.eq.`/`==`, and `.ne.`/`/=` (NOT `!=`) stand for "less than", "less than or equal", "greater than", "greater than or equal", "equal to", and "not equal to" respectively. No space can appear front of or behind `lt`, `le`, `gt`, `ge`, `eq`, and `ne` in `.lt.`, `.le.`, `.gt.`, `.ge.`, `.eq.`, and `.ne.`. It does not permit "complex relational expressions" such as `` 1<2<3 ``.

For numbers, relational operations are made by comparing their value. For character strings, relational operations are made by using the character collating sequence. The operands are compared one character at a time in order, beginning with the first character of each character operand. If the operands are of unequal length, the shorter operand is treated as if it were extended on the right with blanks to the length of the longer operand. If both `` `x1` `` and `` `x2` `` are of zero length, `` `x1` `` is equal to `` `x2` ``; if every character of `` `x1` `` is the same as the character in the corresponding position in `` `x2` ``, `` `x1` `` is equal to `` `x2` ``. Otherwise, at the first position where the character operands differ, the character operand `` `x1` `` is considered to be less than `` `x2` `` if the character value of `` `x1` `` at this position precedes the value of `` `x2` `` in the character collating sequence; `` `x1` `` is greater than `` `x2` `` if the character value of `` `x1` `` at this position follows the value of `` `x2` `` in the collating sequence. However, the character collating sequence is processor dependent. If you want to compare characters by using ASCII collating sequence, you can use `` llt(`x1`, `x2`) ``, `` lle(`x1`, `x2`) ``, `` lgt(`x1`, `x2`) ``, and `` lge(`x1`, `x2`) `` instead of `` `x1` .lt. `x2` ``, `` `x1` .le. `x2` ``, `` `x1` .gt. `x2` ``, and `` `x1` .ge. `x2` ``.
