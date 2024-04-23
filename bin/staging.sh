#!/bin/bash

source="../data/$1"
target=${source#*_}
dest="../data/"

find "$source" -type f -name '*.csv' -exec mv {} "$dest" \;

for file in "$dest"/*; do
  if [ -f "$file" ]; then
    echo "$file"
    target=${file%_*}.csv
    echo "$target"
    lowercase_target=$(echo "$target" | tr '[:upper:]' '[:lower:]')
    mv -- "$file" "$lowercase_target"
  fi
done

rm -rf "$source"