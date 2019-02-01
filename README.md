# sysinfo
Python3 program to generate HTML pages showing system information

# Basic idea
The program should gather system information by either calling a program and capturing its output or by reading content from a file. The gathered information should then be saved to HTML files which are located in a web server's directory. The primary goal is to make that working on Linux systems, but there is no obvious reason why it should not work on FreeBSD, NetBSD, OpenBSD, Solaris, and other similar operating systems.

## Output from a program

For example, "free -h" is called on a Linux system and its output should be saved.

## Content of a file

For example, the last 200 lines of /var/log/auth.log on a Linux system should be saved.
