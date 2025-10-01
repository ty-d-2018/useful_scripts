#!/bin/bash

guest_name="$1"
memory="$2"
vcpus="$3"
storage_path="$4"
iso_path="$5"

network_name="virbr0"
os_variant="archlinux"
os_type="linux"

echo "creating virtual machine named: *${guest_name}"
echo ""

echo "Here are the configurations passed"
echo "+++++"

echo "memory ram is *${memory}, vcpus are *${vcpus}, path to storage file \"${storage_path}\", and the iso path is \"${iso_path}\""
echo ""

echo "by default this script chose the network to be *${network_name} and os_variant to be *${os_variant} while os type is *${os_type}"
echo ""

read -p "is all of this correct? y/n -> " the_answer

if [ $the_answer = "y" ]; then
    echo "answer was yes. Creating machine..."
    echo ""
    virt-install --name $guest_name --memory $memory --vcpus sockets=1,cores=$vcpus,threads=1 --disk path=$storage_path,format="qcow2" --os-variant $os_variant --network bridge=$network_name --cdrom $iso_path --graphics spice --noreboot
elif [ $the_answer = "n" ]; then
    echo "the answer was no"
    echo "retry with different configurations"
fi