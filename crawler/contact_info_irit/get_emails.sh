#!/usr/bin/env bash

filename='contacts_info.dat'

#skip the first line (table header)
#get email list
#remove empty lines
tail -n +2 $filename | cut -f 4 | sed '/^[[:space:]]*$/d' #sed '/^\s*$/d'


