# Pointer

WARNING: Pointer in Fortran is DIFFERENT to pointer in C.

# POINTER attribute and TARGET attribute

A pointer is what can point to a target, and a target is what can be pointed by a pointer. In Fortran, a pointer have the POINTER attribute, which should be specified by adding an `` `attr-spec` `` which is ``pointer``, and a target which IS NOT A PROCEDURE have the TARGET attribute, which should be specified by adding an `` `attr-spec` `` which is ``target``. There is nothing that can be both a pointer and a target in Fortran, which means there is no "pointer of pointer" in Fortran.

# Pointer association status

A pointer has a pointer association status of associated, disassociated, or undefined. If a pointer is pointed to ``null()``, it is disassociated, and if a pointer is pointed to something else, it is associated.

# Pointer to scalar

We use `=>` to make pointer assignment, and after that the pointer is pointed to the target. Then, if we make reference to the pointer, we will actually make reference to the target. We can't and don't need to get the value of the target which a pointer is pointing to by applying an operator to the pointer. If we change the value of the target, we will also change the value of the pointer, since the value of the pointer is actually the value of the target.
```fortran-free-form
program main
    implicit none
    integer, pointer :: p
    integer, target :: a, b
    a = 1
    b = 2
    print *, 'a b = ', a, b
    p => a
    print *, 'p a b = ', p, a, b
    a = 3
    b = 4
    print *, 'p a b = ', p, a, b
    p => b
    print *, 'p a b = ', p, a, b
    a = 5
    b = 6
    print *, 'p a b = ', p, a, b
end program main
```
And also, If we change the value of the pointer, we will also change the value of the target, since the value of the pointer is actually the value of the target.
```fortran-free-form
program main
    implicit none
    integer, pointer :: p
    integer, target :: a, b
    a = 1
    b = 2
    print *, 'a b = ', a, b
    p => a
    print *, 'p a b = ', p, a, b
    p = 3
    print *, 'p a b = ', p, a, b
    p => b
    print *, 'p a b = ', p, a, b
    p = 4
    print *, 'p a b = ', p, a, b
end program main
```

A pointer can not have the ALLOCATABLE attribute. However, A pointer can point to a target with the ALLOCATABLE attribute. In the following program, pointer `p` was pointed to allocatable character `a`, but when `a` was reassigned, `a` was deallocated and then reallocated, and when `a` was deallocated, `p` was not point to `a` again. We used `associated(p, a)` to check whether `p` was pointed to `a` in the following program.
```fortran-free-form
program main
    implicit none
    character(:), pointer :: p
    character(:), allocatable, target :: a
    a = 'Hello, world!'
    p => a
    print *, p, a, associated(p, a)
    p(1:1) = 'h'
    print *, p, a, associated(p, a)
    a = 'Bye bye, world!'
    print *, p, a, associated(p, a)
end program main
```
However, in the following program, when `p` was assigned, `a` was NOT deallocated and then reallocated.
```fortran-free-form
program main
    implicit none
    character(:), pointer :: p
    character(:), allocatable, target :: a
    a = 'Hello, world!'
    p => a
    print *, p, a, associated(p, a)
    p(1:1) = 'h'
    print *, p, a, associated(p, a)
    p = 'Bye bye, world!'
    print *, p, a, associated(p, a)
end program main
```

## Pointer to array

First we should declare an array pointer. We must use `` :{, :}... `` to specify the rank but not the bounds of indexes of the array pointer, which makes the array pointer to be a "deferred-shape array". Then we can simply make the array pointer pointed to an array target, and the bounds of indexes of the array pointer will be automatically determined by the array target.
```fortran-free-form
program main
    implicit none
    integer, dimension(:, :), pointer :: p
    integer, dimension(3, 3), target :: a
    integer :: i
    a = reshape([(i, i = 1, 9)], [3, 3])
    p => a
    print *, p, a
    p = 0
    p(2, 2) = -1
    print *, p, a
end program main
```

We can redetermine the bounds of indexes of the array pointer. In the following program, the lower bounds of indexes of `a` are `1`. We redetermine the lower bounds of indexes of `p` to be `0`.
```fortran-free-form
program main
    implicit none
    integer, dimension(:, :), pointer :: p
    integer, dimension(1:2, 1:2), target :: a
    a = 0
    p(0:, 0:) => a
    print *, p, a
    a(1, 1) = 1
    print *, p, a
    p(1, 1) = 2
    print *, p, a
end program main
```

An array pointer can only point to an array section.
```fortran-free-form
program main
    implicit none
    integer, dimension(:, :), pointer :: p
    integer, dimension(3, 3), target :: a
    integer :: i
    a = reshape([(i, i = 1, 9)], [3, 3])
    p => a(:2, :2)
    print *, p, a
    p = 0
    print *, p, a
end program main
```

The rank of the array pointer and the array target can be different when the array target is a rank-one array, but at this time, we must explicitly determine the bounds of indexes of the array pointer, or the bounds can not be automatically determined. The elements of the array pointer are pointed to the elements of the array target in the sequence of the array elements.
```fortran-free-form
program main
    implicit none
    integer, dimension(:, :), pointer :: p
    integer, dimension(2*5), target :: a
    integer :: i
    a = [(i, i = 1, 10)]
    p(1:2, 1:5) => a
    print *, p, a
    p(:, 3) = 0
    print *, p, a
end program main
```

The rank of the array pointer and the array target can also be different when the array pointer is a rank-one array, but at this time, we must explicitly determine the bounds of indexes of the array pointer, or the bounds can not be automatically determined. The elements of the array pointer are pointed to the elements of the array target in the sequence of the array elements.
```fortran-free-form
program main
    implicit none
    integer, dimension(:), pointer :: p
    integer, dimension(3, 3), target :: a
    integer :: i
    a = reshape([(i, i = 1, 9)], [3, 3])
    p(1:6) => a(:, :2)
    print *, p, a
    p(3) = 0
    print *, p, a
end program main
```
However, at this time, the array target should be simply contiguous, therefore the following program is invalid.
```fortran-free-form
program main
    implicit none
    integer, dimension(:), pointer :: p
    integer, dimension(3, 3), target :: a
    integer :: i
    a = reshape([(i, i = 1, 9)], [3, 3])
    p(1:6) => a(:2, :) ! Invalid, because `a(:2, :)` is not simply contiguous!
    print *, p, a
    p(3) = 0
    print *, p, a
end program main
```

## Pointer to procedure

In the following program, we first made an abstract interface, and used that abstract interface to make the interface of `p`, `ab2bc` and `ab2cb` conformable. We used `point` to make `p` be a procedure pointer. We can't and don't need to use `target` to make `ab2bc` and `ab2cb` a target pointer, and they can be directly pointed.
```fortran-free-form
program main
    implicit none
    abstract interface
        subroutine func_in_inout_out(arg_in, arg_inout, arg_out)
            integer, intent(in) :: arg_in
            integer, intent(inout) :: arg_inout
            integer, intent(out) :: arg_out
        end subroutine func_in_inout_out
    end interface
    procedure(func_in_inout_out), pointer :: p
    procedure(func_in_inout_out) :: ab2bc, ab2cb
    integer :: a, b, c
    a = 1
    b = 2
    c = 3
    p => ab2bc
    call p(a, b, c)
    print *, a, b, c
    a = 1
    b = 2
    c = 3
    p => ab2cb
    call p(a, b, c)
    print *, a, b, c
end program main

subroutine ab2bc(a, b, c)
    integer, intent(in) :: a
    integer, intent(inout) :: b
    integer, intent(out) :: c
    c = b
    b = a
end subroutine ab2bc

subroutine ab2cb(a, b, c)
    integer, intent(in) :: a
    integer, intent(inout) :: b
    integer, intent(out) :: c
    b = b
    c = a
end subroutine ab2cb
```
