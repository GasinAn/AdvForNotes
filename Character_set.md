# Character set

You can use any ASCII graphical characters in Fortran programs. You can and should use End of Line characters of corresponding OS in source code of Fortran programs. You may be able to use other characters in Fortran programs, but it is processor dependent.

WARNING: Fortran is CASE-INSENSITIVE. In Fortran programs, lower-case letters are equivalent to corresponding upper-case letters of them in program units, except in character literal constants or in character string edit descriptors. If you want to use the iterative method to solve the Kepler's equation \\(E - e\sin E = M\\), and you write down `E = M + e*sin(E)`, you will not get the right answer, because `E` and `e` are the same variable!
