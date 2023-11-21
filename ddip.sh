#!/bin/bash
#This script is used to Divide The Docs into Parts(DDIP)
#Input = Docs -- Output txt
if [ $# -lt 1 ]; then
  echo "Usage: $0 <document_file> [-n <num_parts>]"
  exit 1
fi

document_file=""
num_parts=2  # Default number of parts

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -n|--num-parts)
      num_parts="$2"
      shift
      ;;
    *)
      document_file="$1"
      ;;
  esac
  shift
done

if [ -z "$document_file" ]; then
  echo "Usage: $0 <document_file> [-n <num_parts>]"
  exit 1
fi

output_dir="${document_file%.*}"

# Create output directory
mkdir -p "$output_dir"

# Use LibreOffice to convert the document to plain text
unoconv --format=txt --output="$output_dir/$(basename "${document_file%.*}.txt")" "$document_file"


#move to the output directory
cd "$output_dir"

# Split the plain text document into the specified number of parts
split -d -a 1 -n l/"$num_parts" --additional-suffix=".txt" "$(basename "${document_file%.*}.txt")" "part"

echo "Document divided into $num_parts parts successfully in the '$output_dir' directory."

