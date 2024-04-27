#!/bin/bash

dest="../data/"

folder_name=$(find ../data -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort | head -n 1)

if [ -z "$folder_name" ]; then
    echo "ERROR: Data folder not found. Please enter a health data folder inside the 'data' directory."
    exit 1
fi

source="$dest$folder_name"
target=${source#*_}

echo "Creating data from $folder_name."

find "$source" -type f -name '*.csv' -exec mv {} "$dest" \;

for file in "$dest"/*; do
  if [ -f "$file" ]; then
    target=${file%_*}.csv
    lowercase_target=$(echo "$target" | tr '[:upper:]' '[:lower:]')
    mv -- "$file" "$lowercase_target"
  fi
done

rm -rf "$source"
find "../data" -type f ! -name "*activity.csv" ! -name "*activity_minute.csv" ! -name "*activity_stage.csv" ! -name "*heartrate_auto.csv" ! -name "*sleep.csv" ! -name "*init.sql" ! -name "*sport.csv" -delete
cp '../db/init.sql' '../data/'

python '../src/cleaning/data_cleaning.py'

echo "Data Initialization Process completed."