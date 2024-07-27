#! /bin/bash

for i in {1..1000};
do
    random_string=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w $i | head -n 1)
    result=$(py RSA_parity_attack.py $random_string)
    if [[ ! py RSA_parity_attack.py $random_string ]]; then
        
        break
    fi
done