#!/usr/bin/env bash

filename="Pride_and_Prejudice.txt"

#1. 通过当前脚本的pid，生成awk脚本的临时文件名。
#2. 捕捉信号，在脚本退出时删除该临时文件，以免造成大量的垃圾临时文件。
awk_script_file="/tmp/scf_tmp.$$"
count_words_file="/tmp/cwf_tmp.$$"
trap "rm -f $awk_script_file $count_words_file" EXIT
#3. while循环将以当前目录下的testfile作为输入并逐行读取，在读取到末尾时退出循环。
#4. getline读取到每一行将作为awk的正常输入。在内层的for循环中，i要从1开始，因为$0表示整行。NF表示域字段的数量。
#5. 使$i作为数组的键，如果$i的值匹配正则表达式"^[a-zA-Z]+$"，我们将其视为单词而不是标点。每次遇到单词时，其键值都会递增。
#6. 最后通过awk脚本提供的特殊for循环，遍历数组的键值数据。
cat << 'EOF' > $awk_script_file
BEGIN {
while (getline < "Pride_and_Prejudice.txt" > 0) {
    for (i = 1; i <= NF; ++i) {
        if (match($i,"^[a-zA-Z]+$") != 0)
            arr[$i]++
        }
    }
    for (word in arr) {
        printf "%-*s\t%s\n", 20, word, arr[word]
    }
}
EOF

awk -f $awk_script_file > $count_words_file
sort -k2nr $count_words_file > count_words.txt
