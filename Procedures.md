# Procedures

## Classifications

A procedure in Fortran is either a subroutine or a function.

### Subroutines

A subroutine named `ab2bc_then_sumabc` is defined in the following program. INTENT(IN) attribute makes dummy arguments to be readable only. INTENT(OUT) attribute makes dummy arguments to be writable only. INTENT(INOUT) attribute makes dummy arguments to be readable and writable.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: a, b, c
    a = 1.0_dp
    b = 2.0_dp
    c = 3.0_dp
    call ab2bc_then_sumabc(a, b, c)
    print *, a, b, c
end program main

subroutine ab2bc_then_sumabc(a, b, c)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: a
    real(dp), intent(inout) :: b
    real(dp), intent(out) :: c
    real(dp) :: s
    c = b
    b = a
    s = a + b + c
    print *, s
end subroutine ab2bc_then_sumabc
```

### Functions

Two functions named `combinatorial` and `factorial` respectively are defined in the following program. The variables in `result()` are the results of functions. You should make all dummy arguments (The result is not defined as a dummy argument) to be readable only, or you are likely to get into trouble.
```fortran-free-form
program main
    implicit none
    integer :: combinatorial
    print *, combinatorial(7, 3)
end program main

function combinatorial(n, m) result(comb)
    implicit none
    integer, intent(in) :: n
    integer, intent(in) :: m
    integer :: comb
    integer :: factorial
    comb = factorial(n) &
           / (factorial(m)*factorial(n-m))
end function combinatorial

function factorial(n) result(fact)
    implicit none
    integer, intent(in) :: n
    integer :: fact
    integer :: i
    fact = 1
    do i = 1, n
        fact = fact * i
    end do
end function factorial
```

## Procedure interface

The interface of a procedure is either explicit or implicit. The procedure defined by a separate subprogram has an implicit interface in default, while The procedure defined in a module or submodule has an explicit interface.

### Explicit interface

If you use a procedure which is "complicated", or use a procedure in a "complicated" way, you need to use an interface block to make the interface of the procedure explicit. An interface block is similar to an interface declaration in a C header file. All situations in which you need an interface block are listed in paragraph 1 of subsubsection 15.4.2.2 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf).

In the following program, we used a keyword argument, and therefore we have to add an interface block. The interface block must be added in the specification part, and USE statements and `implicit none` must be added in the interface block for necessity.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: x, y, z
    interface
        subroutine ab2bc_then_sumabc(a, b, c)
            use iso_fortran_env, only: dp => real64
            implicit none
            real(dp), intent(in) :: a
            real(dp), intent(inout) :: b
            real(dp), intent(out) :: c
        end subroutine ab2bc_then_sumabc
    end interface
    x = 1.0_dp
    y = 2.0_dp
    z = 3.0_dp
    call ab2bc_then_sumabc(x, y, c=z)
    print *, x, y, z
end program main

subroutine ab2bc_then_sumabc(a, b, c)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: a
    real(dp), intent(inout) :: b
    real(dp), intent(out) :: c
    real(dp) :: s
    c = b
    b = a
    s = a + b + c
    print *, s
end subroutine ab2bc_then_sumabc
```

### Abstract interface

An abstract interface is a set of procedure characteristics with the dummy argument names. In the following program, we first defined an abstract interface `dim2mat`, and then used `procedure(dim2mat)` to declare explicit interfaces of function `eye` and `minkowski`, which have the same procedure characteristics with abstract interface `dim2mat`.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    abstract interface
        function dim2mat(dim) result(mat)
            use iso_fortran_env, only: dp => real64
            implicit none
            integer, intent(in) :: dim
            real(dp) :: mat(0:dim-1, 0:dim-1)
        end function dim2mat
    end interface
    procedure(dim2mat) :: eye, minkowski
    real(dp), dimension(0:3, 0:3) :: mat_i, mat_m
    mat_i = eye(4)
    mat_m = minkowski(4)
end program main

function eye(n) result(mat)
    use iso_fortran_env, only: dp => real64
    implicit none
    integer, intent(in) :: n
    real(dp) :: mat(0:n-1, 0:n-1)
    integer :: i
    mat = 0.0_dp
    do i = 0, n-1
        mat(i, i) = 1.0_dp
    end do
end function eye

function minkowski(n) result(eta)
    use iso_fortran_env, only: dp => real64
    implicit none
    integer, intent(in) :: n
    real(dp) :: eta(0:n-1, 0:n-1)
    integer :: i
    eta = 0.0_dp
    eta(0, 0) = -1.0_dp
    do i = 1, n-1
        eta(i, i) = 1.0_dp
    end do
end function minkowski
```

### Generic interface

We can use generic interface to "produce a generic procedure". In the following program, we defined a generic interface `sgn`, and if we use "the generic procedure `sgn`", the arguments will be automatically associated to argument in `sgn_real64` or `sgn_real128`.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64, &
                               qp => real128
    implicit none
    interface sgn
        function sgn_real64(x) result(y)
            use iso_fortran_env, only: dp => real64
            implicit none
            real(dp), intent(in) :: x
            real(dp) :: y
        end function sgn_real64
        function sgn_real128(x) result(y)
            use iso_fortran_env, only: qp => real128
            implicit none
            real(qp), intent(in) :: x
            real(qp) :: y
        end function sgn_real128
    end interface
    print *, sgn(10.0_dp)
    print *, sgn(10.0_qp)
end program main

function sgn_real64(x) result(y)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: x
    real(dp) :: y
    if (x > 0.0_dp) then
        y = 1.0_dp
    else if (x < 0.0_dp) then
        y = -1.0_dp
    else
        y = 0.0_dp
    end if
end function sgn_real64

function sgn_real128(x) result(y)
    use iso_fortran_env, only: qp => real128
    implicit none
    real(qp), intent(in) :: x
    real(qp) :: y
    if (x > 0.0_qp) then
        y = 1.0_qp
    else if (x < 0.0_qp) then
        y = -1.0_qp
    else
        y = 0.0_qp
    end if
end function sgn_real128
```

### Defined assignment, operations, and I/O

See subsubsubsection 15.4.3.4.2--15.4.3.4.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.
 
## Attributes of dummy arguments

### OPTIONAL attribute

A dummy argument with OPTIONAL attribute is an optional dummy argument. Intrinsic function `present` can be used to check whether an optional dummy argument is present.
```fortran-free-form
program main
    implicit none
    interface
        subroutine example(arg1, arg2, arg3, arg4, arg5)
            integer, intent(in) :: arg1
            integer, intent(in), optional :: arg2
            integer, intent(in) :: arg3
            integer, intent(in), optional :: arg4
            integer, intent(in) :: arg5
        end subroutine example    
    end interface
    call example(1, 2, 3, 4, 5)
    call example(1, 2, arg5=5, arg3=3)
    call example(arg5=5, arg3=3, arg4=4, arg1=1)
end program main

subroutine example(arg1, arg2, arg3, arg4, arg5)
    integer, intent(in) :: arg1
    integer, intent(in), optional :: arg2
    integer, intent(in) :: arg3
    integer, intent(in), optional :: arg4
    integer, intent(in) :: arg5
    print *, 'arg1 =', arg1
    if (present(arg2)) then
        print *, 'arg2 =', arg2
    end if
    print *, 'arg3 =', arg3
    if (present(arg4)) then
        print *, 'arg4 =', arg4
    end if
    print *, 'arg5 =', arg5
end subroutine example
```

### SAVE attribute

A dummy argument with SAVE attribute is a saved dummy argument. The value of a saved dummy argument will be kept even if the procedure have returned. A saved dummy argument in Fortran is equivalent to a static local dummy argument in C. A saved dummy argument must be explicit initialized.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    call count() ! 0 -> 1
    call count() ! 1 -> 2
    call count() ! 2 -> 3
end program main

subroutine count()
    implicit none
    integer, save :: n = 0
    n = n + 1
    print *, n
end subroutine count
```

### Character dummy argument

Use `*` or `len=*` to make a character dummy argument to be an assumed-length character, and its length can be automatically assumed from that of the effective actual argument.
```fortran-free-form
program main
    implicit none
    character(3), parameter :: char_in = 'Hi!'
    character(1) :: char_out
    print *, char_in
    call to_screen(char_in, char_out)
    print *, char_out
end program main

subroutine to_screen(char_in, char_out)
    implicit none
    character(*), intent(in) :: char_in
    character(*), intent(out) :: char_out
    print *, char_in, len(char_in)
    char_out = char_in
    print *, char_out, len(char_out)
end subroutine to_screen
```

### Array dummy argument

#### Explicit-shape array

In the following program, `r` is a normal explicit-shape array.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: r(2)
    real(dp) :: norm_1
    r = [-1.0_dp, 2.0_dp]
    print *, norm_1(r)
end program main

function norm_1(r) result(norm)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: r(2)
    real(dp) :: norm
    norm = sum(abs(r))
end function norm_1
```

In the following program, `r` is an adjustable array, which is defined as a kind of explicit-shape array.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: r_2(2), r_3(3)
    real(dp) :: norm_1
    r_2 = [-1.0_dp, 2.0_dp]
    r_3 = [-1.0_dp, 2.0_dp, -3.0_dp]
    print *, norm_1(r_2, size(r_2))
    print *, norm_1(r_3, size(r_3))
end program main

function norm_1(r, size_r) result(norm)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: r(size_r)
    integer, intent(in) :: size_r
    real(dp) :: norm
    norm = sum(abs(r))
end function norm_1
```

In the following program, `mat` is an automatic array, which is defined as a kind of explicit-shape array. The difference between adjustable array and automatic array is that adjustable array is while automatic array is not dummy argument.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: strange_mat_element_sum
    print *, strange_mat_element_sum(50)
end program main

function strange_mat_element_sum(n) result(s)
    use iso_fortran_env, only: dp => real64
    implicit none
    integer, intent(in) :: n
    real(dp) :: s
    real(dp) :: mat(n, n)
    integer :: i, j
    do i = 1, n
        do j = 1, n
            mat(i, j) = sqrt(real(i+j-1))
        end do
    end do
    s = sum(mat)
end function strange_mat_element_sum
```

#### Assumed-shape array

In the following program, `r` is an assumed-shape array.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: r_2(2), r_3(3)
    real(dp) :: norm_1
    r_2 = [-1.0_dp, 2.0_dp]
    r_3 = [-1.0_dp, 2.0_dp, -3.0_dp]
    print *, norm_1(r_2)
    print *, norm_1(r_3)
end program main

function norm_1(r) result(norm)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: r(:)
    real(dp) :: norm
    norm = sum(abs(r))
end function
```
The lower bounds of indexes of assumed-shape array can be determined as in the following program.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp) :: r_2(2, 1), r_3(3, 1)
    interface
        function norm_1(r) result(norm)
            use iso_fortran_env, only: dp => real64
            implicit none
            real(dp), intent(in) :: r(0:,:)
            real(dp) :: norm
        end function
    end interface
    r_2 = reshape([0.0_dp, -1.0_dp], [2, 1])
    r_3 = reshape([0.0_dp, -1.0_dp, 2.0_dp], [3, 1])
    print *, norm_1(r_2)
    print *, norm_1(r_3)
end program main

function norm_1(r) result(norm)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: r(0:,:)
    real(dp) :: norm
    norm = sum(abs(r))
end function norm_1
```

### Dummy procedure

In the following program, `f` is a dummy procedure.
```fortran-free-form
program main
    use iso_fortran_env, only: dp => real64
    implicit none
    interface
        function identity(x) result(y)
            use iso_fortran_env, only: dp => real64
            implicit none
            real(dp), intent(in) :: x
            real(dp) :: y
        end function
    end interface
    real(dp) :: integrate
    print *, integrate(identity, 0.0_dp, 1.0_dp)
end program main

function integrate(f, a, b) result(s)
    ! Use trapezoidal rule.
    use iso_fortran_env, only: dp => real64
    implicit none
    interface
        function f(x) result(y)
            use iso_fortran_env, only: dp => real64
            implicit none
            real(dp), intent(in) :: x
            real(dp) :: y
        end function
    end interface
    real(dp), intent(in) :: a
    real(dp), intent(in) :: b
    real(dp) :: s
    real(dp) :: h
    integer :: i
    h = (b-a) / 10000
    s = (f(a)+f(b)) / 2
    do i = 1, 9999
        s = s + f(a+i*h)
    end do
    s = s * h
end function integrate

function identity(x) result(y)
    use iso_fortran_env, only: dp => real64
    implicit none
    real(dp), intent(in) :: x
    real(dp) :: y
    y = x
end function identity
```

## Special procedures

### Pure procedures

Characteristics of pure procedures are listed in section 15.7 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). A representative pure procedure is a procedure with only INTENT(IN) attribute, and I/O are not possible to happen during the execution of the procedure. If you understand functional programming, you will easily understand pure procedures. Add `pure` in front of `subroutine` or `function` in the start statement to make procedure pure as in following program.
```fortran-free-form
program main
    implicit none
    integer :: factorial
    print *, factorial(3)
end program main

pure function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    integer :: i 
    p = 1
    do i = 1, n
        p = p * i
    end do
end function factorial
```

### Simple procedures

Characteristics of simple procedures are listed in section 15.8 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). A representative simple procedure is a pure procedure which don't reference any procedure which is not simple procedure. Add `simple`, which implies `pure`, in front of `subroutine` or `function` in the start statement to make procedure simple as in following program. Simple procedures are too new, and your compiler may not allow definitions of them.
```fortran-free-form
program main
    implicit none
    integer :: factorial
    print *, factorial(3)
end program main

simple function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    integer :: i 
    p = 1
    do i = 1, n
        p = p * i
    end do
end function factorial
```

### Elemental procedures

Characteristics of elemental procedures are listed in section 15.9 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). A representative elemental procedure is a procedure which is similar to a "ufunc" in [Numpy](https://numpy.org/). Add `elemental`, which implies `pure`, in front of `subroutine` or `function` in the start statement to make procedure elemental as in following program.
```fortran-free-form
program main
    implicit none
    integer :: i
    interface
        elemental function factorial(n) result(p)
            integer, intent(in) :: n
            integer :: p
        end function factorial
    end interface
    print *, factorial(3)
    print *, factorial([(i, i = 1, 9)])
end program main

elemental function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    integer :: i 
    p = 1
    do i = 1, n
        p = p * i
    end do
end function factorial
```
If you want to specify that an elemental procedure is impure, additionally add `impure` in front of `subroutine` or `function` in the start statement.
```fortran-free-form
program main
    implicit none
    integer :: i
    interface
        impure elemental function factorial(n) result(p)
            integer, intent(in) :: n
            integer :: p
        end function factorial
    end interface
    print *, factorial(3)
    print *, factorial([(i, i = 1, 9)])
end program main

impure elemental function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    integer :: i 
    p = 1
    do i = 1, n
        p = p * i
    end do
    print *, p
end function factorial
```

### Recursive procedures

A recursive procedure is a procedure which can reference itself. Add `recursive` in front of `subroutine` or `function` in the start statement to make procedure recursive as in following program.
```fortran-free-form
program main
    implicit none
    integer :: factorial
    print *, factorial(3)
end program main

recursive function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    if (n == 1) then
        p = 1
    else
        ! factorial(n) == n * factorial(n-1)
        p = n * factorial(n-1)
    end if
end function factorial
```
If you want to specify that an elemental procedure is pure, simple, or elemental, additionally add `pure`, `simple`, or `elemental` in front of `subroutine` or `function` in the start statement.
```fortran-free-form
program main
    implicit none
    integer :: i
    interface
        elemental recursive function factorial(n) result(p)
            integer, intent(in) :: n
            integer :: p
        end function factorial
    end interface
    print *, factorial(3)
    print *, factorial([(i, i = 1, 9)])
end program main

elemental recursive function factorial(n) result(p)
    integer, intent(in) :: n
    integer :: p
    if (n == 1) then
        p = 1
    else
        ! factorial(n) == n * factorial(n-1)
        p = n * factorial(n-1)
    end if
end function factorial
```
