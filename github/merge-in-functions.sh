#!/bin/bash

FUNCTIONS_FILE=combined_functions.py
cat > $FUNCTIONS_FILE << EOT
# DO NOT EDIT THIS FILE, IT IS A COMBINATION OF ALL THE FUNCTIONS IN THE functions/
# SUBDIRECTORY OF THIS REPOSITORY

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
import time
import hub

EOT


for file in $(find functions/ -type f); do
  echo >> $FUNCTIONS_FILE
  echo "###" >> $FUNCTIONS_FILE
  echo "### BEGIN FUNCTION FROM FILE: $file" >> $FUNCTIONS_FILE
  echo "###" >> $FUNCTIONS_FILE
  echo >> $FUNCTIONS_FILE
  write_line=0
  while IFS= read -r line; do
    [[ $line =~ "FUNCTION START" ]] && write_line=1 && continue
    [[ $line =~ "FUNCTION END" ]] && write_line=0
    if [[ $write_line -eq 1 ]]; then
      printf '%s\n' "$line" >> $FUNCTIONS_FILE
    fi
  done < $file
  echo >> $FUNCTIONS_FILE
  echo "###" >> $FUNCTIONS_FILE
  echo "### END FUNCTION FROM FILE: $file" >> $FUNCTIONS_FILE
  echo "###" >> $FUNCTIONS_FILE
done
