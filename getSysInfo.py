#!/usr/bin/env python3

# getSysInfo.py

# Purpose: Obtain system information (no sudo required)

import subprocess
from datetime import datetime

class Cmd():

    def __init__(self):
        self.uptime = 'cat /proc/uptime'
        self.cpuinfo = 'cat /proc/cpuinfo'
        self.kernel = 'uname -a'
        self.ipaddr = 'ip addr show'

    def getUptime(self):
        process = subprocess.Popen(self.uptime, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        out = out.decode()
        out = out.split()
        errcode = process.returncode

        unixTimeVal1 = float(out[0])
        unixTimeVal2 = float(out[1])
        regtime1 = datetime.fromtimestamp(unixTimeVal1)
        regtime2 = datetime.fromtimestamp(unixTimeVal2)
        print()
        screeninfo = '-' * 15 + ' System Uptime'
        if len(screeninfo) < 50:
            placeholder = 50 - len(screeninfo)
            rightClosure = '-' * placeholder
            screeninfo = screeninfo + ' ' + rightClosure
        print(screeninfo)
        print('Unix timestamp:', unixTimeVal1, 'equals:')
        print(regtime1)
        print('Unix timestamp:', unixTimeVal2, 'equals:')
        print(regtime2)

    def getCPUinfo(self):
        process = subprocess.Popen(self.cpuinfo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        errcode = process.returncode
        print()
        screeninfo = '-' * 15 + ' CPU information'
        if len(screeninfo) < 50:
            placeholder = 50 - len(screeninfo)
            rightClosure = '-' * placeholder
            screeninfo = screeninfo + ' ' + rightClosure
        print(screeninfo)
        print(out.decode())
        print()

    def getKernel(self):
        process = subprocess.Popen(self.kernel, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        errcode = process.returncode
        print()
        screeninfo = '-' * 15 + ' Kernel information'
        if len(screeninfo) < 50:
            placeholder = 50 - len(screeninfo)
            rightClosure = '-' * placeholder
            screeninfo = screeninfo + ' ' + rightClosure
        print()
        print(screeninfo)
        print(out.decode())
        print()

    def getIPaddr(self):
        process = subprocess.Popen(self.ipaddr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        errcode = process.returncode
        print()
        screeninfo = '-' * 15 + ' IP information'
        if len(screeninfo) < 50:
            placeholder = 50 - len(screeninfo)
            rightClosure = '-' * placeholder
            screeninfo = screeninfo + ' ' + rightClosure
        print()
        print(screeninfo)
        print(out.decode())
        print()

oCmd = Cmd()
oCmd.getUptime()
oCmd.getCPUinfo()
oCmd.getKernel()
oCmd.getIPaddr()
