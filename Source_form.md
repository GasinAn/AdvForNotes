# Source form

Fortran has two source forms: the free source form and the fixed source form. The fixed source form is obsolescent.

## Free source form

Note: A character context is where within a character literal constant or within a character string edit descriptor.

### Commentary

The character `!` initiates a comment, except where it appears within a character context. The comment extends to the end of the line. If the first nonblank character on a line is an `!`, the line is a comment line. Lines containing only blanks or containing no characters are also comment lines. Comments may appear anywhere in a program unit and may precede the first statement of a program unit or follow the last statement of a program unit. Comments have no effect on the interpretation of the program unit.

Unfortunately, there is no block comment in Fortran. I suggest you to use a good text editor, such as [VS Code](https://code.visualstudio.com/), which has the column selection mode.

### Statement continuation

The character `&` is used to indicate that the statement is continued on the next line that is not a comment line. Comment lines cannot be continued; an `&` in a comment has no effect. Comments may occur within a continued statement. When used for continuation, the `&` is not part of the statement. No line shall contain a single `&` as the only nonblank character or as the only nonblank character before an `!` that initiates a comment.

If a noncharacter context is to be continued, an `&` shall be the last nonblank character on the line, or the last nonblank character before an `!`. There shall be a later line that is not a comment; the statement is continued on the next such line. If the first nonblank character on that line is an `&` the statement continues at the next character position following that `&`; otherwise, it continues with the first character position of that line.

If a lexical token is split across the end of a line, the first nonblank character on the first following noncomment line shall be an `&` immediately followed by the successive characters of the split token.

If a character context is to be continued, an `&` shall be the last nonblank character on the line. There shall be a later line that is not a comment; an `&` shall be the first nonblank character on the next such line and the statement continues with the next character following that `&`.

The following program is valid. The 3rd line is continued by the 5th line.
```fortran
program main
    implicit none
    print *, &
    ! A comment
    'Hello, World!'
end program main
```

The following program is valid. The 3rd line is continued by the 4th line.
```fortran
program main
    implicit none
    print *, & ! A comment
    'Hello, World!'
end program main
```

The following program is valid. The 3rd line is continued by the 4th line.
```fortran
program main
    implicit none
    print *, 'Hello, &
    &World!'
end program main
```

### Statement termination

If a statement is not continued, a comment or the end of the line terminates the statement.

A statement may alternatively be terminated by a `;` character that appears other than in a character context or in a comment. The `;` is not part of the statement. After a `;` terminator, another statement may appear on the same line, or begin on that line and be continued. A sequence consisting only of zero or more blanks and one or more `;` terminators, in any order, is equivalent to a single `;` terminator.
