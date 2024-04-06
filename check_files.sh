#!/bin/bash

path="/home/joseph.mitambo/Downloads"
destination_directory="/home/joseph.mitambo/Backups"
now=$(date +%s)

for f in "$path"/*; do
    if [ -f "$f" ]; then
        if [ $(stat -c %Y "$f") -lt $((now - 7 * 86400)) ]; then
            cp "$f" "$destination_directory"
            #rm "$f"
            echo "Success"
        fi
    fi
done