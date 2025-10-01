
file_name="$1"
command_path="$2/${file_name}"
script_name="$3"

echo "launching ${script_name}"

$command_path

echo "Script has finished running."