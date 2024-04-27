#!/bin/bash

source="../data/$1"
target=${source#*_}
dest="../data/"

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

echo "Data Initialization Process has completed."