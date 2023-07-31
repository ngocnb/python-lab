#!/bin/bash

while read -r library; do
    pip install "$library"
done < installation.txt