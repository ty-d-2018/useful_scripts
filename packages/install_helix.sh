#!/bin/bash

install_package.sh "applit" hx

hx --grammar fetch
hx --grammar build
