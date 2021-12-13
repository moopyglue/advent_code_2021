# as this was so simple went with 
# awk on the bash command line

awk '{a=b;b=c;c=d;d=$1} NR<=3{next} a+b+c<b+c+d {x=x+1} END {print x}' rawdata
