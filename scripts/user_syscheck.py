#!usr/bin/python3

import shutil
import psutil

str1 = "CPU Check"
str2 = "Storage Check"

usrinp = input("Select \"CPU Check\" or \"Storage Check\">>> ")

if  usrinp == str1:
	cpupercent =psutil.cpu_percent(0.1)
	print(cpupercent)
if usrinp == str2:
	Du = shutil.disk_usage("/")
	print(Du)


