while true;
do
  wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date:
  if [ $? -eq 0 ]
  then 
    echo "Set time script - OK"
    date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
    echo "Now:"
    date
    exit 0
  else
    echo "Set time script - Fail"
  fi
done
