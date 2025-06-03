Simple Shell

The goal in this project is to know how a shell works. To single out some items: what is the environment, the difference between functions and system calls, how to create processes using execve...

Usage
In order to run this program,

compile it with

gcc -Wall -Werror -Wextra -pedantic *.c -o hsh.
You can then run it by invoking ./hsh in that same directory.

Output: prompt to terminal: $ 
Syntax
The shell works by using commands given by the user input. The shell commands take in the following syntax: command name {arguments}. The shell executes a command after it is written by user using the command followed by the arguments.

cat holberton.h The above example takes in a command by the user followed with the arguments. In this case the command is cat (to view file without opening file) followed by argument the file name in this case holberton.h.

For more information on cat, you can use the man command which will show a manual of the given command or any command you wish to know more information on. It contains system calls, libraries and other important files.

The shell also contains two builtins which are commands that are within the shell itself. The two builtins are exit and env. You can also use help command to know which builtins are provided by the shell. The help command works similarly to the manual where it provides further detail or information on given builtin.

Compilation
All files will be compiled with the following: $ gcc -Wall -Werror -Wextra -pedantic *.c

List of useful commands
cat - prints and concatenates files to the standard output
cp -copies a file into another file
grep - helps to search for a file in a specific pattern
less - will let you go backward and forward in the files
ls - will list all files and directories in current working directory
mv - helps to move one file into another file
pwd - given you the current working directory
Builtins
There are two builtins programmed into the shell. Below is a description and use for each builtin.

env - The env command is a command that tells the shell program to display all of the environment variables with their values. It is a way to access those values through the shell.

exit - If you wish to exit out of the shell the user can use the builtin exit.

Exiting commands and the shell
To exit out of a command or process the user can use ctrl c. Control c stops a process and causes it to abort. The user can also utilize the command ctrl D which will just exit. When the command ctrl D is used an exit status of 0 is given. Using exit, you can input its exit status or it is defaulted to the status of the last command executed.

Files
README.md : Current file, contains information about this project
holberton.h : Header file, contains all prototypes for funcitons used, as well as libriaries
hsh.c: Main file that uses most functions and executes them within this file
ghostinshell.png: Image in readme file
_getenv.c : Contains the code for _printf
_getline.c: File for getting prompt and user input
which.c: File containing the specific functions for conversion specifiers
builtin_execute.c: Executing the builtins
builtins.c: File containing the two builtins
child.c: File that forks and creates parent child processee
free.c: File with free malloc functions
prompt.c: File with actual prompt line $
tokenizer.c: File that creates function to tokenize an array of strings
utility_functions.c: helper functions