cut -f1 popular-names.txt | sort | uniq -c | sort -k1,1nr 
