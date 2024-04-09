#!/bin/bash

bash /home/t-pi/TB3_RPI4_WS/scripts/check_if_online.sh
result=$?

echo "res:" $result

if [ "$result" -eq 10 ]; then
  echo "Updating time"
  date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
else
  echo "Error - offline"
fi