# Modules and submodules

Although in examples I write the main program, modules and submodules, modules and submodules should be stored in a separate file.

A module contains declarations and procedures which can be used in another program unit. In a module, all variables declared implicitly have SAVE attribute, and all procedure declared have an explicit interface, which means if we use a module procedure, we never need to add an explicit block. 
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, i, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```

A submodule CANNOT be used, and it only makes a module "bigger". The procedure defined in a submodule must have `module` in front of `subroutine` or `function` in the start statement of the procedure, and its interface must be declared in its ancestor. Add `` (`ancestor-module`) `` behind `submodule` in the start statement to specify which ancestor module does the submodule extend.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, i, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    interface
        module impure elemental subroutine print_a_and_array(array)
            integer, intent(in) :: array
        end subroutine print_a_and_array
    end interface
    contains
end module mod1

submodule (mod1) mod1_submod1
    implicit none
    contains
    module impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end submodule mod1_submod1
```
Add `` (`ancestor-module`:`parent`-submodule) `` behind `submodule` in the start statement to specify which ancestor module and parent submodule does the submodule extend.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, i, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    interface
        module impure elemental subroutine print_a_and_array(array)
            integer, intent(in) :: array
        end subroutine print_a_and_array
    end interface
    contains
end module mod1

submodule (mod1) mod1_submod1
    implicit none
    contains
end submodule mod1_submod1

submodule (mod1:mod1_submod1) mod1_submod1_subsubmod1
    implicit none
    contains
end submodule mod1_submod1_subsubmod1

submodule (mod1:mod1_submod1_subsubmod1) mod1_submod1_subsubmod1_subsubsubmod1
    implicit none
    contains
    module impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end submodule mod1_submod1_subsubmod1_subsubsubmod1
```

# Statements related to modules and submodules

## USE statement

USE statement makes a module used in another program unit.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, i, a, b
    call print_a_and_array(b)
    a = -1
    print *, i, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```

To use an intrinsic module like `iso_fortran_env`, you should add `, intrinsic` behind `use`.

A "bare" USE statement `` use :: `module` `` is like `` from `module` import * `` statement in Python, and everything public defined in `` `module` `` is used. A USE statement `` use :: `module`, only: ...... `` is like `` from `module` import ...... `` statement in Python, and `......` defined in `` `module` `` is used.
```fortran-free-form
program main
    use :: mod1, only: a, b, print_a_and_array
    implicit none
    print *, a, b
    call print_a_and_array(b)
    a = -1
    print *, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```
The variable defined in a submodule CAN'T be used, and the following program is invalid.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a, b
    call print_a_and_array(b)
    a = -1
    print *, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1

submodule (mod1) mod1_submod1
    implicit none
    integer :: b(9) = [(i, i = 1, 9)]
    contains
end submodule mod1_submod1
```

## IMPORT statement

In a submodule, what defined in its parent can all be referenced in default. You can use IMPORT statement `import, only: ......` to make the submodule be only able to reference `......` in its parent. This feature is new, and your compiler may not allow it.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a, b
    call print_a_and_array(b)
    a = -1
    print *, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    interface
        module impure elemental subroutine print_a_and_array(array)
            integer, intent(in) :: array
        end subroutine print_a_and_array
    end interface
    contains
end module mod1

submodule (mod1) mod1_submod1
    import, only: a, print_a_and_array
    implicit none
    contains
    module impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end submodule mod1_submod1
```

## PRIVATE statement

PRIVATE statement should be added at the top of the specification part of a module, and it makes everything defined in the module inaccessible to the program unit which is not a descendant submodule of the module and uses the module.
```fortran-free-form
program main
    use :: mod1
    implicit none
end program main

module mod1
    implicit none
    private
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```

## PUBLIC statement

PUBLIC statement overwrite the inaccessibility of something defined in a module, and again make it accessible to the program unit which uses the module.
```fortran-free-form
program main
    use :: mod1
    implicit none
    call print_a_and_array([0])
end program main

module mod1
    implicit none
    private
    integer :: i
    integer, save :: a = 0, b(9) = [(i, i = 1, 9)]
    public :: print_a_and_array
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```

# Attributes related to modules and submodules

## PUBLIC attribute

The specifications of PUBLIC attribute overwrite the inaccessibility of something defined in a module, and again make it accessible to the program unit which uses the module.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a, b
    call print_a_and_array(b)
    a = -1
    print *, a, b
    call print_a_and_array(b)
end program main

module mod1
    implicit none
    private
    integer :: i
    integer, save, public :: a = 0, b(9) = [(i, i = 1, 9)]
    public :: print_a_and_array
    contains
    impure elemental subroutine print_a_and_array(array)
        integer, intent(in) :: array
        print *, a, array
    end subroutine print_a_and_array
end module mod1
```

## PROTECTED attribute

The specifications of PROTECTED attribute makes the value of a variable can only be changed by a procedure defined in the module or its descendant submodules, and also it cannot be an effective argument to be associated with a dummy argument.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a
    call change_a(1)
    print *, a
end program main

module mod1
    implicit none
    private
    integer, save, public, protected :: a = 0
    public :: change_a
    contains
    subroutine change_a(val)
        integer, intent(in) ::  val
        a = val
    end subroutine change_a
end module mod1
```
The following two programs are INVALID.
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a
    a = 1 ! Invalid!
    print *, a
end program main

module mod1
    implicit none
    private
    integer, save, public, protected :: a = 0
    public :: change_a
    contains
    subroutine change_a(val)
        integer, intent(in) ::  val
        a = val
    end subroutine change_a
end module mod1
```
```fortran-free-form
program main
    use :: mod1
    implicit none
    print *, a
    call change(a, 1) ! Invalid!
    print *, a
end program main

module mod1
    implicit none
    private
    integer, save, public, protected :: a = 0
    public :: change
    contains
    subroutine change(var, val)
        integer, intent(out) ::  var
        integer, intent(in) ::  val
        var = val
    end subroutine change
end module mod1
```
