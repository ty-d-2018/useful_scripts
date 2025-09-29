#!/bin/bash

package_name=$1
pack_form=$2

for_snap="snappage"
for_apt="applit"

echo "$0 is using $pack_form to install a package named -> $package_name"
echo "<---**--->"
echo ""

if [ $pack_form = $for_snap ]; then
  sudo snap install $package_name
  echo "installed $1 -> using snapd"
elif [ $pack_form = $for_apt ]; then
  sudo apt update
  sudo apt install $package_name
  echo "installed $1 -> using apt"
fi

sudo -k
