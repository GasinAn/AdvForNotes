# Execution control

## Execution control constructs

### IF construct

`read *, score` makes the program read data from the "file with standard input unit", which is usually from the keyboard, and then assign the data to `score`.
```fortran-free-form
program main
    implicit none
    integer :: score
    read *, score
    print *, score
    if ((score < 0) .or. (score > 100)) then
        print *, 'Invalid Score!'
    else if (score >= 60) then
        print *, 'Succeed.'
    else
        print *, 'Fail.'
    end if
end program main
```

### SELECT CASE construct

```fortran-free-form
program main
    implicit none
    integer :: n
    read *, n
    print *, n
    select case (n)
    case(:-1) ! n <= -1
        print *, -1
    case(0) ! n = 0
        print *, 0
    case(+1:) ! n >= -1
        print *, +1
    end select
end program main
```
```fortran-free-form
program main
    implicit none
    character :: y_or_n
    read *, y_or_n
    print *, y_or_n
    select case (y_or_n(1:1))
    case('y') ! y_or_n == 'y'
        print *, 'Continue...'
    case('n') ! y_or_n == 'n'
        print *, 'Quit.'
    case default ! Other situations
        print *, 'Invalid!'
    end select
end program main
```

### SELECT TYPE construct

Similar to the SELECT CASE construct. Use `` type is (`type-mane`) `` to check whether it is of type `type-mane`. Use `` class is (`type-mane`) `` to check whether it is of a descendant type of type `type-mane`. Use `class default` to check whether it is in other situations.

### DO construct

The "start", "stop", "step" shall be type integer. The "step" can be omitted, and if omitted it is `1`.
```fortran-free-form
program main
    implicit none
    integer :: n
    real :: s
    s = 0.0
    do n = 1, 1000
        s = s + 1.0/n**2.0
    end do
    print *, (6.0*s) ** (1.0/2.0)
end program main
```

### DO WHILE construct

The DO WHILE construct is defined as a kind of DO construct in [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf).
```fortran-free-form
program main
    implicit none
    integer :: n
    real :: s
    n = 0
    s = 0.0
    do while (s < (3.14**2.0 / 6.0))
        n = n + 1
        s = s + 1.0/n**2.0
    end do
    print *, n
end program main
```

## Execution control statements

### CONTINUE statement

WARNING: CONTINUE statement in Fortran is equivalent to PASS statement in Python and C, while CONTINUE statement in Python and C is equivalent to CYCLE statement in Fortran.
```fortran-free-form
program main
    implicit none
    integer :: number
    read *, number
    print *, number
    if (number /= 0) then
        continue
    else
        print *, 'The number is 0!'
    end if
end program main
```

### GO TO statement

If you do need to use GO TO statement, you should first add a label `` `label` ``, which must be an integer in range \\([0,99999]\\), in front of the statement you want to "go to", and make at least one space between `` `label` `` and the statement. Then, you can add a GO TO statement `` go to `label` `` to "go to" the statement with the label `` `label` ``.

### EXIT statement

EXIT statement can be used to exit any construct. It is usually used to exit a DO construct, and in this situation EXIT statement is equivalent to BREAK statement in Python and C.
```fortran-free-form
program main
    implicit none
    integer :: n
    real :: s
    s = 0.0
    do n = 1, 1000
        s = s + 1.0/n**2.0
        if (s < (3.14**2.0 / 6.0)) then
            exit
        end if
    end do
end program main
```
If you want to exit a nested DO construct, you had better use tag of construct, which can be added on any kind of construct. A tag must be a "name", To add a tag, add `` `tag:` `` in front of the start statement of the construct, with making at least one space between `` `tag: `` and the statement, and add `` `tag` `` behind the end statement of the construct, with making at least one space between `` `tag` `` and the statement.
```fortran-free-form
program main
    implicit none
    integer :: i, j, n
    logical :: is_prime
    read *, n
    outer_loop: do i = n**2, (n+1)**2
        is_prime = .true.
        do j = 2, i-1
            if (i == i/j*j) then
                is_prime = .false.
                exit outer_loop       ! ----------+
            end if                                !
        end do                                    !
        print *, i, is_prime                      !
    end do outer_loop                             !
end program main                      ! <---------+
```

### CYCLE statement

EXIT statement can be used to curtail the execution of a loop, and it is equivalent to CONTINUE statement in Python and C.
```fortran-free-form
program main
    implicit none
    integer :: i, j, n
    logical :: is_prime
    read *, n
    outer_loop: do i = n**2, (n+1)**2 ! <---------+
        is_prime = .true.                         !
        do j = 2, i-1                             !
            if (i == i/j*j) then                  !
                is_prime = .false.                !
                cycle outer_loop      ! ----------+
            end if
        end do
        print *, i, is_prime
    end do outer_loop
end program main
```

### STOP statement

Execution of STOP statement `stop` initiates normal termination of execution. Extra message of the normal termination can be added. See section 11.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

### ERROR STOP statement

Execution of STOP statement `error stop` initiates error termination of execution. Extra message of the normal termination can be added. See section 11.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

### RETURN statement

Execution of the RETURN statement completes execution of the instance of the subprogram in which it appears. There is no "ERROR RETURN statement" in Fortran.
