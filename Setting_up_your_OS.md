# Setting up your OS

Two mini-book tutorials, [*Setting up your OS*](https://fortran-lang.org/learn/os_setup/) and [*Building programs*](https://fortran-lang.org/learn/building_programs/), on Fortran official website will help you.

There are many Fortran compilers listed on [this website](https://fortran-lang.org/compilers/). In my opinion, [GNU Fortran Compiler (gfortran)](https://gcc.gnu.org/fortran/) is good for debugging, and [Intel Fortran Compiler (ifx)](https://software.intel.com/content/www/us/en/develop/articles/intel-oneapi-fortran-compiler-release-notes.html) is good for generating executable files with the fastest speed.

There are many text editors listed on [this website](https://fortran-lang.org/learn/os_setup/text_editors/). My favorite text editor which I am using for writing these Notes is [Visual Studio Code (VS Code)](https://code.visualstudio.com/). If you want to use VS Code for writing Fortran programs, you can install extension "[Modern Fortran](https://marketplace.visualstudio.com/items?itemName=fortran-lang.linter-gfortran)", and moreover, if you also use [Python](https://www.python.org/), you can also install [Fortran Language Server (fortls)](https://fortls.fortran-lang.org/). Extension "[Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)" may also be helpful to you.

There are many IDEs listed on [this website](https://fortran-lang.org/learn/os_setup/ides/). I don't use them at all, since VS Code is the best.

There are many build tools listed on [this website](https://fortran-lang.org/learn/building_programs/build_tools/). Fortran has no intrinsic way to do preprocessing, but preprocessor [fypp](https://fypp.readthedocs.io/en/stable/) is easy to use and widely used. Fortran is developing [the Fortran Package Manager (fpm)](https://fpm.fortran-lang.org/), which is a package manager and build system for Fortran, but there is a long way to go.
