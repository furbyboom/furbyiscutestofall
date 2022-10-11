#!/bin/bash 
 
while true; do 
    number_to_guess=$RANDOM 
 
    echo "I thought a number from 0 to 32767. Can you guess it?" 
 
    while true; do 
        echo "Your guess?"; 
        read user_attempt; 
 
        if [ "$user_attempt" -eq $number_to_guess ]; then 
            echo "Great! You found it!" 
            break; 
        elif [ "$user_attempt" -lt $number_to_guess ]; then 
            echo "Try a higher number..." 
        elif [ "$user_attempt" -gt $number_to_guess ]; then 
            echo "Try a lower number..." 
        fi             
    done 
done
