#!/bin/bash

storage_path=$1
file_name=$2
amount=$3

qemu-img create -f qcow2 ${storage_path}/${file_name}.img $amount