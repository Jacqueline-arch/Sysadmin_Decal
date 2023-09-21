#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    NEW=$2\ $3
    echo "$NEW" >> $PHONEBOOK_ENTRIES

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        cat $PHONEBOOK_ENTRIES
    fi

elif [ "$1" = "lookup" ]; then   
    grep "$2" $PHONEBOOK_ENTRIES | awk '{print $NF}'

elif [ "$1" = "remove" ]; then
    sed /"$2"/d $PHONEBOOK_ENTRIES > temp.txt && mv temp.txt $PHONEBOOK_ENTRIES
    
elif [ "$1" = "clear" ]; then
    cat /dev/null > $PHONEBOOK_ENTRIES

else
     echo "good job"
fi
