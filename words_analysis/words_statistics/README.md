# Description
Count the words for the novel "Pride and Prejudice".

Note: this shell script is quite rough and therefore the results are not very precise. For instance,

- case senstive, for instance, `have` and `Have` are regarded as the different words which doesn't make sense;
- different forms, e.g., `take` and `took`, `book` and `books`
- ...

The distribution of words is likely to follow the power law, which is interesting.

For more information, please refer to [《傲慢与偏见》英文小说中各个单词出现的频率](http://sparkandshine.net/pride-and-prejudice-the-frequency-of-every-word-in-the-english-novel/)

# Files

The novel is stored in `Pride_and_Prejudice.txt`.

**(1) Count words**

`count_words.sh`, count the words and save results to `count_words.txt`.



**(2) The distribution of words**

- `distribution.awk`, save results to `distribution.txt`.
- `distribution.plt`, plot the figure `pride_and_prejudice_all.png`.
