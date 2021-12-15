#!/bin/bash

# getTemperature.sh

# Purpose: Get temperature reading from a Raspberry Pi.
# Note: The bash shell returns only integer values.

temperature=$(cat /sys/class/thermal/thermal_zone0/temp)

temperature=$((temperature/1000))
temperature="$temperature °C"

echo "${temperature}"
