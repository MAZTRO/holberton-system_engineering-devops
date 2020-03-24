# Web server
## Project 0x0C Scripting to manage a server
In this project you find usefull scripts to manage files between local server(Your PC) and remote server.
## For this project, students are expected to look at these concepts:
 - DNS
 - Web Server app
 - CI/CD -  (Continuous Integration/Continuous Deployment)
 - Docker
 - Web Satck debugging
 - DevOps
 - System Administration
 - Site Reliability Engineering

In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

#### Tips: to test your answer Bash script, feel free to reproduce the checker environment:
 - start an ubuntu:16.04 Docker container
 - run your script on it
 - see how it behaves
Check out the Docker concept page for more info about how to manipulate containers.

## Learning Objectives:
### General:
 - What is the main role of a web server
 - What is a child process
 - Why web servers usually have a parent process and child processes
 - What are the main HTTP requests
### DNS:
 - What DNS stands for
 - What is DNS main role
### DNS Record Types:
 - A
 - CNAME
 - TXT
 - MX

## Requirements:
 - All your files should end with a new line
 - A README.md file, at the root of the folder of the project, is mandatory
 - All your Bash script files must be executable
 - Your Bash script must pass Shellcheck (version 0.3.7) without any error
 - The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
 - The second line of all your Bash scripts should be a comment explaining what is the script doing

## Authors:
[Jonatan Mazo](https://www.linkedin.com/in/jonatan-ricardo-mazo-castro-75633390/)
