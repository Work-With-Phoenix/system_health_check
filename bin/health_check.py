#!/usr/bin/env zsh or bash 
#by With Phoenix 
#
#Does a system health check

import shutil

du = shutil.disk_usage("/")
print (du)

#calculate free space
du.free/du.total*100

