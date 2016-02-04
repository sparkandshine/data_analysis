#plot data with/without XOR in a graph


#set term post color solid enh eps
set terminal png
#set term epslatex standalone
set out 'pride_and_prejudice_all.png'   #设置输出文件名
set multiplot layout 2,2 

set grid    #设置网格

set key top left 
#set key width 1
#set key box

#set xtics 0,1,11
#set format x "%.s*10^%T"
#set mxtics 4
set key top right 
set key box

##third graph
set key top right 
set key box

set xrange [0:6000]   
set xtics 0, 1500, 6000
set yrange [0:4000]   

set title 'Times of each words appeared'
set xlabel 'ID of words'
set ylabel 'Times of each words'
plot "Pride_and_Prejudice_count_words.txt" using 2 with lp pt 12 lw 2 lt 1 title ""

##fourth graph
set key top right 
set key box

set yrange [0:600]   
set title 'Times of each words appeared'
set xlabel 'ID of words'
set ylabel 'Times of each words'
plot "Pride_and_Prejudice_count_words.txt" using 2 with lp pt 12 lw 2 lt 1 title ""

##first graph
set key top right 
set key box

set xrange [0:4000]   
set xtics 0, 1500, 4000 
set yrange [0:0.41]

set title 'Probability of times of words appeared'
set xlabel 'Times of words appeared'
set ylabel 'Probability'
plot "distribution.txt" using 1:3 with lp pt 12 lw 2 lt 1 title ""

##second graph
set key top right 
set key box

set xrange [0:600]   
set xtics 0, 150, 600
set yrange [0:0.005]
set title 'Probability of times of words appeared'
set xlabel 'Times of words appeared'
set ylabel 'Probability'
plot "distribution.txt" using 1:3 with lp pt 12 lw 2 lt 1 title ""


