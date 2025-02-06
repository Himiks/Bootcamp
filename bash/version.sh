#!/bin/bash
if [ "$#" -ne 3 ]; then
        echo "You should pass source, option(increment/full), backup dir"
        exit 1
fi

Dir=$1
option=$2
bkdir=$3

if [ ! -d "$bkdir" ]; then
        mkdir "$bkdir"
fi
lastbk=$(ls -t "$bkdir" | head -n 1)


if [ "$option" == "increment" ]; then
        if [ ! -d "$bkdir/increment" ]; then
                mkdir "$bkdir/increment"
        fi
        for file in $(find $Dir -printf "%P\n") ; do
    if [ -a "$bkdir/increment/$file" ] ; then
        if [ $Dir/$file -nt "$bkdir/increment/$file" ] ; then
            cp -r $Dir/$file "$bkdir/increment/$file"
        fi
    else
    echo "$file is being copied over to $bkdir"
    cp -r $Dir/$file "$bkdir/increment/$file"
   fi
done
else
        bkfile="$bkdir/$(basename "$Dir")_full_$(date +"%Y%m%d%H%M%S")"
        cp -r "$Dir" "$bkfile"
        echo "full"
fi


Count=$(ls -l "$bkdir" | grep -c ^d)
if [ $Count -gt 5 ]; then
        old=$(ls -t "$bkdir" | tail -n 1)
        rm -rf "$bkdir/$old"
fi

echo "Success"





