#!/usr/bin/env bash

##!/bin/sh
#https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file
#          || visible in terminal ||   visible in file   || existing
#  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file  
# | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
# | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append

#echo "remove old log file"

#dt=`date '+%d%m%Y_%H%M%S'`
dt=`date '+%d%m%Y_%H%M%S'`
echo $dt
#echo "${dt::-1}"

touch /mnt/c/cygwin/home/ephucle/tool_script/python/durucrashlog_$dt.txt
#rm /mnt/c/cygwin/home/ephucle/tool_script/python/durucrashlog.txt

#dung bien ngay thang de luu file
/mnt/c/cygwin/home/ephucle/tool_script/python/new_crash.py du_crash.csv | tee durucrashlog_$dt.txt
/mnt/c/cygwin/home/ephucle/tool_script/python/new_crash.py ru_crash.csv | tee -a durucrashlog_$dt.txt

echo "Log file is saved to file: /mnt/c/cygwin/home/ephucle/tool_script/python/durucrashlog_$dt.txt"