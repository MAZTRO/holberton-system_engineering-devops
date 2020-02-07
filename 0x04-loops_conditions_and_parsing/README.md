# Loops, conditions and parsing.
## Project 0x04 BASH Scripts.

You may notice that most shell and Perl script starts with the following line:
#!/bin/bash
OR
#!/usr/bin/perl

It is called a shebang. It consists of a number sign and an exclamation point character (#!), followed by the full path to the interpreter such as /bin/bash. All scripts under Linux, *BSD, macOS, and Unix-like system execute using the interpreter specified on a first line. However, there is a small problem. BASH or Perl is not always in the same location (PATH) such as /bin/bash or /usr/bin/perl. If you want to make sure that script is portable across different UNIX like operating systems you need to use /usr/bin/env command as shebang.
The advantage of #!/usr/bin/env bash is that it will use whatever bash executable appears first in the running user’s $PATH variable.

## Learning Objectives:
 - How to create SSH keys
 - What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
 - How to use while, until and for loops
 - How to use if, else, elif and case condition statements
 - How to use the cut command
 - What are files and other comparison operators, and how to use them

## Requirements:
 - All your files should end with a new line
 - A README.md file, at the root of the folder of the project, is mandatory
 - All your Bash script files must be executable
 - You are not allowed to use awk
 - Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
 - The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
 - The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Authors:
(Jonatan Mazo)[https://twitter.com/JonatanRMC]
