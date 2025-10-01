#!/bin/bash

javaPath="./io/github/tyd2018"
mainClass="$2"
projectName="$1"
packageName="io.github.tyd2018.${projectName}"

echo "compiling Java source files"
javac ${javaPath}/${projectName}/*.java

echo "running java program"
java $packageName.$mainClass