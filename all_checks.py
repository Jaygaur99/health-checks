#!/usr/bin/env python3
import os
import sys
import shutil

# Hi from conflicts
def check_reboot():
    """Return True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb,min_percent):
    """Return True if there is enough disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
      return False
    return True

def main():
    if check_reboot():
        print("Oending Reboot.")
        sys.exit(1)
    if check_disk_full(disk="/",min_gb=2,min_percent=10) :
        print("disk full.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)
main()
