#!bin/bash
File=$1
Key=$2
time=0
if [ "$#" -ne 2 ]; then
	echo "You should pass a log file aand key"
	exit 1
fi

tail -F "$File" | while read line; do
	if echo "$line" | grep -q "$Key"; then
		now=$(date +%s)
		if (( now - time >= 60 )); then
			echo "The key $Key found in log file"
			time=$now
		fi
	fi
done



