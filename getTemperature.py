#!/usr/bin/env python3

# getTemperature.py

# Purpose: Get temperature reading from a Raspberry Pi CPU as a shell output.

from subprocess import Popen, PIPE

def getTemperature():
	stdout = Popen('cat /sys/class/thermal/thermal_zone0/temp', shell=True, stdout=PIPE).stdout
	output = int(stdout.read())
	temperature = str("{:.2f}".format(output/1000)) + ' °C'
	return temperature

if __name__ == '__main__':
	print(getTemperature())
