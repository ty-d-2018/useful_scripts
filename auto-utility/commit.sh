#!/bin/bash

modeSwitch="$1"
commitMessage="$2"

doStatus="-c"
doCommit="-r"

if [ $modeSwitch = $doStatus ]; then
    git status
    echo ""
    echo ""
    echo "Your commit message will be: ${commitMessage}"
elif [ $modeSwitch = $doCommit ]; then
    git add -A
    git commit -m "${commitMessage}"
    git status
fi