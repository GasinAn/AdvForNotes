# Array

In Fortran, the scalar are defined to be zero-rank.

In Fortran, the lower bound of index can be any integer, and default lower bound of index is NOT `0` but `1`. The elements of array in Fortran are in column-major order, like \\(a_{00} \to a_{10} \to a_{01} \to a_{11}\\), which is DIFFERENT the row-major order in Python and C.

`rank(a)`, `lbound(a)`, `ubound(a)`, `shape(a)` and `size(a)` are the rank, the lower bounds of indexes, the upper bounds of indexes, the shape and the size of array `a`.

## Array construction

List elements between `(/`/`[` and `/)`/`]` to construct an array.
```fortran-free-form
program main
    implicit none
    print *, [1, 2, 3]
    print *, (/1, 2, 3/)
end program main
```

Implied-DO-loop can be used in an array constructor, which makes the array constructor similar to a list comprehension in Python. You should notice that the loop variable for the implied-DO-loop needs to be declared.
```fortran-free-form
program main
    implicit none
    integer :: i
    print *, [(i**2, i = 1, 9)]
    print *, (/(i**2, i = 1, 9, 1)/)
end program main
```
However, an array constructor in Fortran can only construct a rank-one array, even though using a nested implied-DO-loop. To maintain a higher rank array, you can use the `reshape` intrinsic function to reshape the rank-one array. See subsection 16.9.175 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for documentation of the `reshape` intrinsic function.
```fortran-free-form
program main
    implicit none
    integer :: i, j
    integer :: a(9)
    a = [(((i+j)**2, i = 1, 3), j = 1, 3)]
    print *, a
    print *, shape(a)
    print *, reshape(a, [3, 3])
    print *, shape(reshape(a, [3, 3]))
end program main
```
The `reshape` intrinsic function can also be used to transpose an array.
```fortran-free-form
program main
    implicit none
    integer :: i, a(9), b(3, 3)
    a = [(i, i = 1, 9)]
    b = reshape(a, [3, 3])
    print *, reshape(b, shape(b), order=[2, 1])
    print *, reshape(a, shape(b), order=[2, 1])
end program main
```
Using a subscript triplet in an array constructor, like `[1:9:1]` or `[(1:9:1)]`, in an array constructor is INVALID.

## Array element and array section

The method to maintain array element or array section is very similar to the method in [Numpy](https://numpy.org/), but you should use `(`/`)` instead of `[`/`]`. However, there is a difference that the "stop" of a subscript triplet can be INCLUDED. 
```fortran-free-form
program main
    implicit none
    integer :: i, a(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    print *, a(2, 2)
    print *, a(1:3:2, ::2)
end program main
```

We CAN'T maintain an array section of an array section, since the array section is not a "whole array" and the lower and upper bounds of indexes of the array section is not determined. The following program is NOT valid.
```fortran-free-form
program main
    implicit none
    integer :: i, a(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    print *, a(:, :)(:, :) ! Invalid!
end program main
```
If an array `a` is not a "whole array", `lbound(a)` and `ubound(a)` will return the bounds as if lower bounds of indexes of `a` are all `1`, though it is not true.
```fortran-free-form
program main
    implicit none
    integer :: i, a(0:2, 0:2)
    a = reshape([(i, i = 1, 9)], [3, 3])
    print *, lbound(a), ubound(a)
    print *, lbound(a(:, :)), ubound(a(:, :))
end program main
```

## Array declaration

There are two ways to declare an array. One is to add a `` `attr-spec` `` which is `` dimension(`bound-list`) ``. The other is to add a `` (`array-spec`) `` which is `` (`bound-list`) `` behind the `` `object-name` ``. `` `bound` `` is `` {`lower-bound`:}`upper-bound` ``, and if there is no `` `lower-bound`: ``, the lower bound of the index will be `1`.
```fortran-free-form
program main
    implicit none
    real :: array1(1, 10)
    real, dimension(1, 10) :: array2
    real :: array3(1:1, 1:10)
    real, dimension(1:1, 1:10) :: array4
end program main
```

We can declare a deferred-shape array, and the method is similar to that to declare a deferred-shape character. We can then apply the ALLOCATE statement and the DEALLOCATE statement to the deferred-shape array.
```fortran-free-form
program main
    implicit none
    real, allocatable :: array1(:)
    real, dimension(:, :), allocatable :: array2
    allocate(array1(10))
    allocate(array2(0:9, 0:9))
    deallocate(array1)
    deallocate(array2)
end program main
```

## Array assignment and array operations

Array assignment and array operations in Fortran are also very similar to those in [Numpy](https://numpy.org/). You can mix zero-rank normal constants and variables with arrays.
```fortran-free-form
program main
    implicit none
    integer :: a(3, 3)
    a = 1
    print *, a
    a = a + 1
    print *, a
end program main
```
When assign to a deferred-shape array, the deferred-shape array MAY be allocated or reallocated. If we assign an array `` `b` `` to a deferred-shape array `` `a` ``, and `` `a` `` is unallocated or `` `a` `` is allocated but in different shape with `` `b` ``, `` `a` `` will be allocated or reallocated, and `` lbound(`a`) ``/`` ubound(`a`) `` will be the same as `` lbound(`b`) ``/`` ubound(`b`) ``.
```fortran-free-form
program main
    implicit none
    integer :: i, b(0:2, 0:2)
    integer, allocatable :: a(:, :)
    b = reshape([(i, i = 1, 9)], [3, 3])
    a = b
    print *, lbound(a), ubound(a)
end program main
```
However, if `` `a` `` is allocated and in the same shape with `` `b` ``, `` `a` `` will NOT be allocated or reallocated.
```fortran-free-form
program main
    implicit none
    integer :: i, b1(0:2, 0:2), b2(-1:1, -1:1) 
    integer, allocatable :: a(:, :)
    b1 = reshape([(i, i = 1, 9)], [3, 3])
    a = b1
    print *, lbound(a), ubound(a)
    b2 = reshape([(i, i = 1, 9)], [3, 3])
    a = b2
    print *, lbound(a), ubound(a)
end program main
```
If `` `b` `` is not an array but a scalar, and `` `a` `` is unallocated, it is impossible to automatically allocate `` `a` ``, thus the following program is INVALID.
```fortran-free-form
program main
    implicit none
    integer, allocatable :: a(:, :)
    a = 0 ! Invalid!
    print *, lbound(a), ubound(a)
end program main
```
While, if `` `a` `` is allocated, `` `a` `` does be reallocated, but the bounds of indexes of `` `a` `` will be as before.
```fortran-free-form
program main
    implicit none
    integer, allocatable :: a(:, :)
    allocate(a(0:2, 0:2))
    a = 0
    print *, lbound(a), ubound(a)
end program main
```

You can use WHERE construct and DO CONCURRENT construct, which is defined as a kind of DO construct in [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf), to do complex and parallel array assignment, but you should not use FORALL construct, since it is obsolescent. You should notice that the syntax of WHERE construct is SLIGHTLY DIFFERENT from that of IF construct, and the syntax of DO CONCURRENT construct is SLIGHTLY DIFFERENT from those of normal DO construct, IF construct and subscript triplet of array.

### WHERE construct

The following two programs are equivalent.
```fortran-free-form
program main
    implicit none
    integer :: i, j, a(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    do i = 1, 3
        do j = 1, 3
            if (a(i, j) <= 3) then
                a(i, j) = a(i, j) + 1
            else if (a(i, j) <= 6) then
                a(i, j) = a(i, j) + 2
            else
                a(i, j) = a(i, j) + 3
            end if
        end do
    end do
    do i = 1, 3
        print *, a(i, :)
    end do
end program main
```
```fortran-free-form
program main
    implicit none
    integer :: i, a(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    where (a <= 3)
        a = a + 1 ! Parallel!
    elsewhere (a <= 6)
        a = a + 2 ! Parallel!
    elsewhere
        a = a + 3 ! Parallel!
    end where
    do i = 1, 3
        print *, a(i, :)
    end do
end program main
```

The following two programs use WHERE construct too.
```fortran-free-form
program main
    implicit none
    integer :: i, a(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    where (a(1:2, 2:3) <= 3)
        a(1:2, 2:3) = a(1:2, 2:3) + 1 ! Parallel!
    elsewhere (a(1:2, 2:3) <= 6)
        a(1:2, 2:3) = a(1:2, 2:3) + 2 ! Parallel!
    elsewhere
        a(1:2, 2:3) = a(1:2, 2:3) + 3 ! Parallel!
    end where
    do i = 1, 3
        print *, a(i, :)
    end do
end program main
```
```fortran-free-form
program main
    implicit none
    integer :: i, a(3, 3), b(3, 3)
    a = reshape([(i, i = 1, 9)], [3, 3])
    b = reshape([(i, i = 1, 9)], [3, 3])
    where (a <= 3)
        b = b + 1 ! Parallel!
    elsewhere (a <= 6)
        b = b + 2 ! Parallel!
    elsewhere
        b = b + 3 ! Parallel!
    end where
    do i = 1, 3
        print *, b(i, :)
    end do
end program main
```

However, there is a gotcha of WHERE construct. In the following program, `log` in `a = log(a)` is an elemental function, thus `a` in `log(a)` represents the "`> 0.0` part" of array `a`, and `a = log(a)` in this program is equivalent to `a(6:9) = log(a(6:9))`. While, `sum` in `a = a / sum(log(a))` is NOT an elemental function, and `a` in `sum(log(a))` is in "`()`" behind nonelemental function `sum`, thus `a` in `sum(log(a))` DOESN'T represent the "`> 0.0` part" of array `a` but represents THE WHOLE OF `a`, even though `log` is an elemental function, and `a = a / sum(log(a))` in this program is equivalent to `a(6:9) = a(6:9) / sum(log(a(:)))`.
```fortran-free-form
program main
    implicit none
    integer :: i
    real :: a(9)
    a = [(real(i), i = -4, +4)]
    where(a > 0.0)
        ! log is invoked only for positive elements,
        ! because log is elemental.
        a = log(a) 
    end where
    print *, a
    print *, a / sum(a)
    a = [(real(i), i = -4, +4)]
    where(a > 0.0)
        ! log is invoked for ALL elements,
        ! because sum is NOT elemental.
        a = a / sum(log(a)) 
    end where
    print *, a
end program main
```

### DO CONCURRENT construct

The following two programs are equivalent.
```fortran-free-form
program main
    implicit none
    integer :: i, j, a(9), b(9)
    a = [(i, i = 1, 9)]
    b = [(j, j = 1, 9)]
    do i = 1, 3, 1
        do j = 7, 9, 1
            if ((a(i) > 1) .and. (b(j) < 9)) then
                b(i) = -j
                a(j) = -i
            end if
        end do
    end do
    print *, a
    print *, b
end program main
```
```fortran-free-form
program main
    implicit none
    integer :: i, j, a(9), b(9)
    a = [(i, i = 1, 9)]
    b = [(j, j = 1, 9)]
    do concurrent (i = 1:3:1, j = 7:9:1, &
                   (a(i) > 1) .and. (b(j) < 9))
        b(i) = -j
        a(j) = -i
    end do
    print *, a
    print *, b
end program main
```
