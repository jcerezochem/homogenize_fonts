#!/bin/bash

# Apply ps2pdf to custom size ps files

size=$(identify $1 | egrep -o "[0-9]+x[0-9]+" | head -n 1)
width=${size%x*}
height=${size##*x}
ps2pdf -dDEVICEWIDTHPOINTS=$width -dDEVICEHEIGHTPOINTS=$height $1


