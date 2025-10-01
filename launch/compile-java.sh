#!/bin/bash

rootFolderPath="$1"
javaPath="${1}/io/github/tyd2018"
mainClass="$3"
projectName="$2"
packageName="io.github.tyd2018.${projectName}"

echo "compiling Java source files"
javac ${javaPath}/${projectName}/*.java

echo "running java program"
java $packageName.$mainClass