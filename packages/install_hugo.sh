#!/bin/bash

# Pass the version number of hugo as seen on the github page for packages
VERSION=$1
tar_file="hugo_${VERSION}_linux-amd64.tar.gz"

# Check to make sure the link is valid. Unlikely to change, but it is important to validate if enough time has passed from last run of this script
link="https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${tar_file}"

location="${HOME}/bin/."

mkdir -p $location

wget "${link}"
tar -xzf $tar_file

mv hugo $location

rm $tar_file

echo "finished script. Hugo is in ${location}"
