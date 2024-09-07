#!/bin/bash


for file in trandata/*.ttl; do
    cd gStore
    start_time=$(date +%s)
    bin/gadd -db trandb -f ../$file
    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))  # Calculate the elapsed time in seconds
    echo "Execution time: $elapsed_time seconds"
    cd ..
done