#!/bin/bash

if [ ${1,,} = "konstancja" ]; then
	echo "Hi konstancja"
elif [ ${1,,} = "help" ]; then
	echo "Enter your name..."
else
	echo "I dont know you"
fi

# ${1,,} converts  the first positional
# parameter $1 to lowercase
