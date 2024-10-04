# Introduction

Fortran is a modern high-performance parallel programming language with a long history. The current standard of Fortran is Fortran 2023, which is given by [Fortran 2023 standard document](https://www.iso.org/standard/82170.html). The standard document should be purchased for reading. A free equivalent document of Fortran 2023 standard document is [Fortran 2023 interpretation document](https://j3-fortran.org/doc/year/24/24-007.pdf). Fortran has its [official website](https://fortran-lang.org/), on which you can find good resources.

Fortran has its advantages, which are given on the official website:

High performance: Fortran has been designed from the ground up for computationally intensive applications in science and engineering. Mature and battle-tested compilers and libraries allow you to write code that runs close to the metal, fast.

Statically and strongly typed: Fortran is statically and strongly typed, which allows the compiler to catch many programming errors early on for you. This also allows the compiler to generate efficient binary code.

Easy to learn and use: Fortran is a relatively small language that is surprisingly easy to learn and use. Expressing most mathematical and arithmetic operations over large arrays is as simple as writing them as equations on a whiteboard.

Versatile: Fortran allows you to write code in a style that best fits your problem: imperative, procedural, array-oriented, object-oriented, or functional.

Natively parallel: Fortran is a natively parallel programming language with intuitive array-like syntax to communicate data between CPUs. You can run almost the same code on a single CPU, on a shared-memory multicore system, or on a distributed-memory HPC or cloud-based system. Coarrays, teams, events, and collective subroutines allow you to express different parallel programming patterns that best fit your problem at hand.

Fortran has its disadvantages:

The syntax of Fortran has many leakages and gotchas, which should be carefully kept away from. (By programming in a suitable way, Fortran will become easy to use.)

Fortran may not be fastest. See [*Scientific Computing Languages - University of Pennsylvania*](https://www.sas.upenn.edu/~jesusfv/Lecture_HPC_5_Scientific_Computing_Languages.pdf) for results of testing.
