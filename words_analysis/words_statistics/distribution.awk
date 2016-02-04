#! /usr/bin/awk -f 

BEGIN {
    print "#times count %"
    id = 1
    sumCount = 5493 
} 

{
    times = $1
    count = $2
    print $1, $2, $2/sumCount
}

END {
}
