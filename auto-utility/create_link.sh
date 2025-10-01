#!/bin/bash

bin_directory="$HOME/bin/$1"

ln -s $(pwd)/$1 $bin_directory 

echo "linking $1 to $bin_directory" 
