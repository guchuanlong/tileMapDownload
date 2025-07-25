#!/bin/bash

watch_dir=/export/icity/tzd-map-tdt

watch -n 5 "find $watch_dir -type f -name "*.png" | wc -l"


