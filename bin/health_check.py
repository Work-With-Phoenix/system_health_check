#!/usr/bin/env python3
#by With Phoenix 
#
#Does a system health check

import shutil
import psutil

#check disk usage
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

#calculate free space
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

#condition
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is fine!")

#cpu 

