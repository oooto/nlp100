#!/bin/bash

cut -f 1 popular-names.txt | sort | uniq -c | sort -r -n -k 1