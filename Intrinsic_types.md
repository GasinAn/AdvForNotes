# Intrinsic types

Each intrinsic type is classified as a numeric type or a nonnumeric type. The numeric types are integer, real, and complex. The nonnumeric intrinsic types are character and logical.

Each intrinsic type has a kind type parameter named KIND. The intrinsic character type has a length type parameter named LEN which is the length of character string. Each type parameter is integer. `` kind(`data-object`) `` and `` len(`data-object`) `` will be the kind and length type parameter of `` `data-object` `` respectively. If not specified, the type parameter KIND is "the default kind", which is processor dependent, and the type parameter LEN is the default length \\(1\\). The compiler may have a compilation option for explicitly choosing a certain kind as the default kind, which makes the program flexible.

That what kind does an integer stand for is actually processor dependent, so you should use standard kinds which are defined in the standard intrinsic module `iso_fortran_env`. To use standard kinds, you can first add `use, intrinsic :: iso_fortran_env, only: ` in the USE statement part, then add `` `kind-spec`{, `kind-spec`}... `` behind `only: `. Each `` `kind-spec` `` is `` `kind-name` `` or `` `local-name` => `kind-name` ``. A `` `kind-name` `` specifies that standard kind named `` `kind-name` `` is used. A `` `local-name` => `kind-name` `` specifies that standard kind named `` `kind-name` `` is used, but it is renamed to `` `local-name` `` in the program unit. For example, in the following program, the variable `a` has the standard kind ``int64``, but it is renamed to ``l`` in the main program unit, and the variable `b` has the standard kind ``real32``, which is not renamed.
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: l => int64, real32
    implicit none
    integer(l) :: a
    real(real32) :: b
end program main
```

In the modern way, each `` `declaration-type-spec` `` of intrinsic types should be `` `type-keyword` `` or `` `type-keyword`(`type-param-selector`) ``. The `` `type-keyword` `` specifies the type. For type integer, real, complex, character and logical, the `` `type-keyword` `` are `integer`, `real`, `complex`, `character` and `logical` respectively. The `` (`type-param-selector`) `` specifies the type parameters, and a type parameter can have not been specified, when the type parameter is the default type parameter. For types which only have kind type parameter, the `` (`type-param-selector`) `` can be `` (`kind`) `` or `` (kind=`kind`) ``, which both specify the kind named or renamed to `` `kind` ``. For example, in the following program, `c` is of type integer and kind `int32`, `d` is of type real and kind `real64`, and `e` is of type complex and the default kind.
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: int32, dp => real64
    implicit none
    integer(int32) :: c
    real(kind=dp) :: d
    complex :: e
end program main
```
For character type, usually we use the default kind, and there is no standard character kind in `iso_fortran_env`. The `` (`type-param-selector`) `` of character type can be `` (`len`) `` or `` (len=`len`) ``, which both specify the length to `` `len` ``. For example, in the following program, `f` is of type character, the default kind and length \\(0\\), `g` is of type character, the default kind and length \\(1000000000\\), and `h` is of type character, the default kind and the default length \\(1\\).
```fortran-free-form
program main
    implicit none
    character(0) :: f
    character(len=1000000000) :: g
    character :: h
end program main
```

A `` `attr-spec` `` which is `parameter` specifies that the declaration is not for variables but for named constants. Named constants have the PARAMETER attribute, and must always be initialized by `` `initialization` ``. For example, in the following program, `i` is a named constant, which is initialized by `= 0`, and `j` is a variable, which is not initialized.
```fortran-free-form
program main
    implicit none
    integer, parameter :: i = 0
    real :: j
end program main
```

## Integer

Default kind integer literal constants have the common form as the other languages. You can add a "tail" `` _`kind` `` just behind (with NO space between) default kind integer literal constants to produce `` `kind` `` kind integer literal constants as in the following program.
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: int32, l => int64
    implicit none
    print *, 0_int32
    print *, +1000000000_l
    print *, -1
end program main
```

Standard integer kinds are `int8`, `int16`, `int32`, and `int64`, which specify that the storage size, expressed in bits, of the integer value is 8, 16, 32, and 64 respectively.

Fortran do have binary, octal, and hexadecimal literal constants. However, they are NOT of type integer. See section 7.7 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

## Real

Default kind real literal constants have the common form as the other languages, and they can have an exponent part `` e`int` `` which represents \\(10\\) to the power of `` `int` ``. You can add a "tail" `` _`kind` `` just behind (with NO space between) default kind real literal constants to produce `` `kind` `` kind real literal constants as in the following program, but you can not add a "tail" to `` `int` ``.
```fortran-free-form
program main
    program main
    use, intrinsic :: iso_fortran_env, only: real32, dp => real64
    implicit none
    print *, 0.0_real32
    print *, +1.0e9_dp
    print *, -1.0
end program main
```

Standard real kinds are `real16`, `real32`, `real64`, and `real128`, which specify that the storage size, expressed in bits, of the real value is 16, 32, 64, and 128 respectively.

A `` `declaration-type-spec` `` which is `double precision` specifies a real kind which is not the default real kind, and mustn't follow by `` (`type-param-selector`) ``. The real literal constants of that kind must have an exponent part `` d`int` `` instead of `` e`int` `` and mustn't have a "tail".

The default real kind and the real kind which can be specified by `double precision` is usually `real32` and `real64`, and also `4` and `8`, respectively, but they don't need to be.

## Complex

Complex literal constants have the form `` (`real`, `imag`) ``, where `` `real` `` and `` `imag` `` are real type or integer type constants, and stands for real and imaginary parts respectively. You CAN'T add a "tail" to complex literal constants. The complex kinds are the same as the real kinds, and always keep the same with the kind of both real and imaginary part. The kind of complex literal constants are determined by `` `real` `` and `` `imag` ``.

- If `` `real` `` and `` `imag` `` of a complex literal constant are both real, the kind type parameter value of the complex literal constant is the kind type parameter value of the part with the greater decimal precision; if the precisions are the same, it is the kind type parameter value of one of the parts as determined by the processor. If a part has a kind type parameter value different from that of the complex literal constant, the part is converted to the approximation method of the complex literal constant.

- If only one of `` `real` `` and `` `imag` `` is an integer, it is converted to the approximation method selected for the part that is real and the kind type parameter value of the complex literal constant is that of the part that is real.

- If both `` `real` `` and `` `imag` `` are integer, they are converted to the default real approximation method and the constant is default complex.

In the following program, `(0.0_sp, 0.0_real64)` has kind `real64`, `(+1.0e9_sp, 0)` has kind `real32`, and `(-1, 0)` has the default real kind.
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: sp => real32, real64
    implicit none
    print *, (0.0_sp, 0.0_real64)
    print *, (+1.0e9_sp, 0)
    print *, (-1, 0)
end program main
```

If `` `z` `` is of type complex, `` real(`z`) `` and `` aimag(`z`) `` will be the real and imaginary part of `` `z` `` respectively, and if `` `z` `` is also a variable, `` `z`%re `` and `` `z`%im `` will also be the real and imaginary part of `` `z` `` respectively.

## Character

Default kind character literal constants have the common form as the other languages like Python, except C, and enclosed by `'`/`"`. If you do want to specify a kind of character, see subsection 7.4.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details, and you should notice that: In `` character(`l`, `k`) ``, `` `l` `` specifies the length and `` `k` `` specifies the kind, and you CAN'T add a "tail" `` _`k` `` but can add a "braid" `` `k`_ `` just front of (with NO space between) character literal constants.

Unfortunately, character literal constants in Fortran have no way, such as using `\`, to escape characters. If you want to add `'`/`"` in a character literal constant enclosed by `'`/`"`, you should not use `\` to escape `'`/`"` as `\'`/`\"`, but should repeat `'`/`"` as `''`/`""`. It is impossible for you to add a nongraphical character in a character literal constant (in free source form), but you can use `new_line('A')` to get a "LF" new line character and use `` achar(`i`) `` to get a character whose ASCII code value is `` `i` ``.

In `` (`type-param-selector`) `` of the character type declaration, `` `len` `` can be `*`. If `` `len` `` is `*`, the declared character will be an assumed-length character, and its length can be automatically assumed for convenience. All way to automatically assumed the length of the assumed-length character is listed in paragraph 7 of section 7.2 and paragraph 5 of subsubsection 7.4.4.2 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). For a character named constant, it can be assumed-length, and its length is the same as `` `constant-expr` `` in the initialization ``= `constant-expr` `` as in the following program.
```fortran-free-form
program main
    implicit none
    character(*), parameter :: hello_world = 'Hello, world!'
    print *, hello_world, len(hello_world)
    print *, 'Hello, world!', len('Hello, world!')
end program main
```

In `` (`type-param-selector`) `` of the character type declaration, `` `len` `` can be `:`. If `` `len` `` is `:`, the declared character will be a deferred-length character. A normal deferred-length character must be specified to have the ALLOCATABLE attribute by adding an `` `attr-spec` `` which is ``allocatable`` in the type declaration statement. Just after declaration of a deferred-length character `` `char` ``, `` `char` `` is unallocated and the length of `` `char` `` is indetermined. ALLOCATE statement `` allocate(character(`len`) :: `char`) ``/`` allocate(character(len=`len`) :: `char`) `` will make unallocated `` `char` `` allocated and the length of `` `char` `` determined to be `len`. DEALLOCATE statement `` deallocate(`char`) `` will make allocated `` `char` `` unallocated and the length of `` `char` `` indetermined again. You should not add allocated `` `char` `` in ALLOCATE statement or unallocated `` `char` `` in DEALLOCATE statement. ALLOCATE statement and DEALLOCATE statement in Fortran is similar but not equivalent to function `calloc` and function `free` in C. [An example of allocatable character string](https://fortran-lang.org/learn/quickstart/arrays_strings/#id5) is on the official website.

In Fortran, you can maintain a substring `` `char`({`start`}:{`stop`}) `` (NOT `` `char`[{`start`}:{`stop`}] ``) of a character string `` `char` `` when `` `char` `` is NOT ITSELF A SUBSTRING. `` `char`({`start`}:{`stop`}) `` is the `` `start` ``th--`` `stop` ``th characters of `` `char` `` (The `` `stop` ``th character is INCLUDED). If `` `start` `` is omitted, it will be `1`. If `` `stop` `` is omitted, it will be `` len(`char`) ``.

## Logical

Default kind logical literal constants are two. They are `.true.` and `.false.`, which represent true and false respectively. No space can appear front of or behind `true` and `false` in `.true.` and `.false.`. You can add a "tail" `` _`kind` `` just behind (with NO space between) default kind logical literal constants to produce `` `kind` `` kind logical literal constants.

Standard logical kinds are `logical8`, `logical16`, `logical32`, and `logical64`, which specify that the storage size, expressed in bits, of the logical value is 8, 16, 32, and 64 respectively.

Fortran do not permit the direct conversion between the integer value and the logical value, although some compilers may permit it.
