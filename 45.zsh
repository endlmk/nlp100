cat ./corpus.txt | sort | uniq -c | sort -nr | head -n 10

cat ./corpus.txt | grep '^行う\s' -w | sort | uniq -c | sort -nr | head -n 10
cat ./corpus.txt | grep '^なる\s' | sort | uniq -c | sort -nr | head -n 10
cat ./corpus.txt | grep '^与える\s' -w | sort | uniq -c | sort -nr | head -n 10