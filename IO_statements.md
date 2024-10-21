# I/O statements

## Files

A file is composed of either a sequence of file storage units or a sequence of records, which provide an extra level of organization to the file. A file composed of records is called a record file. A file composed of file storage units is called a stream file.

A file is either an external file or an internal file.

## Records

A record is a sequence of values or a sequence of characters. For example, a line on a terminal is usually considered to be a record. However, a record does not necessarily correspond to a physical entity.

There are three kinds of records: formatted records, unformatted records, and endfile records. See section 12.2 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

## File storage units

A file storage unit is the basic unit of storage in a stream file or an unformatted record file.

The number of bits in a file storage unit is given by the constant `file_storage_size` defined in the intrinsic module `iso_fortran_env`.
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: file_storage_size
    implicit none
    print *, file_storage_size
end program main
```

## External files

An external file is any file that exists in a medium external to the program.

### File access

There are three methods of accessing the data of an external file: sequential access, direct access, and stream access. See subsection 12.3.3 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

### File position

The file position is like a cursor which point to the beginning of a file storage unit or a record. See subsection 12.3.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

Reading and writing change the file position. File positioning statements also change the file position. See section 12.8 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

## Internal files

An internal file is a character variable in a Fortran program. See section 12.4 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

## OPEN statement and CLOSE statement

OPEN statement opens an external file, and close statement closes an external file. An internal file CAN'T and don't need to be opened and closed.

The OPEN statement accepts a lot of arguments, which are all listed in subsection 12.5.6 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). The first argument should be `` `unit` `` or `` unit=`unit` ``, where `unit` is a nonnegative integer, and it makes `unit` to be the file unit which stands for the external file. The other important keyword arguments are `access=......`, `action=......`, ` file=......`, `form=......`, `position=......`, and `status=......`.

The external file unit mustn't be equal to one of the named constants `input_unit`, `output_unit`, or `error_unit`, of the intrinsic module `iso_fortran_env`. `input_unit`, `output_unit`, and `error_unit` in the intrinsic module `iso_fortran_env` stand for standard input, standard output, and standard error respectively, and the value of them are usually less than \\(10\\).
```fortran-free-form
program main
    use, intrinsic :: iso_fortran_env, only: input_unit, output_unit, error_unit
    implicit none
    print *, input_unit, output_unit, error_unit
end program main
```

The CLOSE statement accepts a lot of arguments, which are all listed in subsection 12.5.7 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). The first argument should be `` `unit` `` or `` unit=`unit` ``, where `unit` is an external file unit.

## READ statement and WRITE statement

READ statement reads data from an external file, an internal file, or standard input, and WRITE statement writes data to an external file, an internal file, standard output, or standard error. The READ statement and the WRITE statement accepts a lot of arguments, which are all listed in section 12.6 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). The first argument should be `` `unit` `` or `` unit=`unit` ``, where `unit` is an external file unit which stands for an external file, a character variable stands for the internal file, `input_unit`, `output_unit`, `error_unit`, or `*` which stands for standard input/output. The second argument should be `` `fmt` `` or `` fmt=`fmt` `` which specify the format of input/output. If `` `fmt` `` is a character, it specifies explicit formatting, and if `` `fmt` `` is `*`, it specifies list-directed formatting. See chapter 13 of [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf) for details.

`` read `fmt`, `` and `` print `fmt`, `` are equivalent to `` read(*, `fmt`) `` and `` write(*, `fmt`) `` respectively.
