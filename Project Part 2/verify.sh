#! /bin/bash

for i in {250..1};
do
    random_string=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w $i | head -n 1)
    result=$(python3 RSA_parity_attack.py $random_string)
    exit_code=$?
    if [ $exit_code -eq 1 ]; then
        echo "Error: "
        echo $(tail -4 <<< $result)
    fi
done