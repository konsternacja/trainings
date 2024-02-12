#!/bin/bash

ls -l | grep .sh

echo Hello World! > hello.txt
# this symbol always overwrites the contents
echo Hi World! > hello.txt

echo Hello World! >> hello2.txt
echo Hi World! >> hello2.txt

wc -w < hello.txt
# wc shows the file name if there is no <

wc -w <<< "Hello World"
