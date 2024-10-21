# Derived types

## Definition and declaration

Use a TYPE block to define a derived type, and use `type(......)` to declare an instance of a derived type
```fortran-free-form
program main
    implicit none
    type :: duck
        contains
    end type duck
    type(duck) :: duck1, duck2
end program main
```

## Type components

Type components are like attributes of an object in Python. Use NOT `.` but `%` to get type components.
```fortran-free-form
program main
    implicit none
    type :: duck
        logical :: living = .true.
        logical :: swiming = .false.
        contains
    end type duck
    type(duck) :: duck1, duck2
    print *, duck1%living
    print *, duck2%swiming
end program main
```

## Type-bound procedures

Type-bound procedures are like methods of an object in Python. Use NOT `.` but `%` to get type-bound procedures. If type-bound procedure is specified by `nopass`, the instance of the type itself will not be passed to the type-bound procedure, If type-bound procedure is specified by `` pass(`self`) ``, the instance of the type itself will be passed to the `` `self` `` dummy argument the type-bound procedure. The `` `self` `` dummy argument must be declared to be type `` class(`type`) `` which stands of type `type` or a descendant type of type `type`.
```fortran-free-form
program main
    use :: mod
    implicit none
    type(duck) :: duck1, duck2
    call duck1%quack()
    call duck2%swim()
    print *, duck2%swiming
end program main

module mod
    implicit none
    type :: duck
        logical :: living = .true.
        logical :: swiming = .false.
        contains
        procedure, nopass :: quack
        procedure, pass(self) :: swim
    end type duck
    contains
    subroutine quack()
        print *, 'Quack!'
    end subroutine quack
    subroutine swim(self)
        interface
            subroutine quack()
            end subroutine quack
        end interface
        class(duck) :: self
        self%swiming = .true.
    end subroutine swim    
end module mod
```

## Type extensions

Type extension is like inheritance of a type in Python. Add `` extends(`parent-type`) `` in the start statement of the TYPE block to extend a type.
```fortran-free-form
program main
    use :: mod
    implicit none
    type(duck) :: duck1, duck2
    call duck1%quack()
    call duck2%swim()
    print *, duck2%swiming
end program main

module mod
    implicit none
    type :: animal
        logical :: living = .true.
        logical :: swiming = .false.
        contains
    end type animal
    type, extends(animal) :: duck
        contains
        procedure, nopass :: quack
        procedure, pass(self) :: swim
    end type duck
    contains
    subroutine quack()
        print *, 'Quack!'
    end subroutine quack
    subroutine swim(self)
        interface
            subroutine quack()
            end subroutine quack
        end interface
        class(duck) :: self
        self%swiming = .true.
    end subroutine swim    
end module mod
```
