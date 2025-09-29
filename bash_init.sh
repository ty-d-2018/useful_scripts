#!/bin/bash

first_command="change_permission.sh"
second_command="create_link.sh"

echo "two commands: $first_command and $second_command"

$first_command $1
$second_command $1
