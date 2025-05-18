# holberton_exercises
Holberton Exercises

This project is collaborative, a basic implementation of a Unix command-line interpreter (shell), It handles input both interactively and non-interactively, using the `/bin/sh`.

# Features
- Display a shell prompt (`$`) before waiting for input.
- Read user input using `getline()`.
- Print the input back to the user.
- Display the prompt before `main()` using constructor functions.
- Print the parent process ID.
- Print all command-line arguments.
- Retrieve and display the maximum PID value.
- Support both interactive and non-interactive shell modes.

# Compilation
All files compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
----------------------------------------------------------------

# Tasks Overview
Task0: getppid
Prints: the PID of the parent process.
Demonstrates: use of getppid().

# Task1: Print the Maximum Process ID
/proc/sys/kernel/pid_max
Shell: script that prints the maximum possible process ID by reading the value from the kernel.
Uses: cat /proc/sys/kernel/pid_max.

# Task2: av
Program: that prints all arguments passed to it using only av, not argc.

# Task3: Read line
Displays: the prompt $ , waits for user input, and prints the input.
Uses: getline() for robust input handling.
Addition: Prompt Before main
Prints: the $ prompt before main() is called using a function with __attribute__((constructor)).

# Usage:-
Run: ./hsh
$ echo Hello
Hello
$ exit

# AUTHORS:
Monica,Boodenator,Abubakermubarak.