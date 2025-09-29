#!/bin/bash

storage_file_path="${HOME}/Documents/t_iso"
storage_name=$1
storage_amount=$2

vm_name="$3"
memory="$4"
vcpus="$5"
vm_storage_path="${storage_file_path}/${storage_name}.img"
iso_path="${HOME}/Documents/t_iso/$6"


echo "creating qcow file at ${storage_file_path} by the name of \"${storage_name}\" with ${storage_amount} of storage"

./create_qcow_file.sh $storage_file_path $storage_name $storage_amount

echo "Now creating the virtual machine"
echo "*Note* the machine should not start. The machine will only be created"

./create_arch_machine.sh $vm_name $memory $vcpus $vm_storage_path $iso_path
