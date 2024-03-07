#!/bin/bash

# Define the root directory containing subdirectories
ROOT_DIR="home/c/dev/ai/ai_club/BusyBee/data/se_us_bee_data"

# Iterate over each subdirectory
for subdir in "$ROOT_DIR"/*; do
    if [ -d "$subdir" ]; then
        # Create a subdirectory called 'images' if it doesn't exist
        mkdir -p "$subdir/images"
        
        # Move all jpg images to the 'images' subdirectory
        mv "$subdir"/*.jpg "$subdir/images/"
    fi
done

