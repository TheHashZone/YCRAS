#!/bin/bash
cat html.txt | awk -F 'author": "' {'print $2'} | cut -d '"' -f1 >> users.txt
cat html.txt | awk -F 'text": "' {'print $2'} | cut -d '\' -f1 >> comments.txt