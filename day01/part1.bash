# as this was so simple went with 
# awk on the bash command line

awk 'NR>1 && $1>p {x=x+1} {p=$1} END {print x}' rawdata
