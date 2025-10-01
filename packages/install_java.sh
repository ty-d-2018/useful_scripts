#!/bin/bash

j_package="default-jdk"
m_package="maven"
p_form="applit"

install_package.sh $j_package $p_form

install_package.sh $m_package $p_form

java -version
mvn -version