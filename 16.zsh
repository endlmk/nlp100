total_lines=$(wc -l < popular-names.txt)
lines_per_file=$(( (total_lines + 3 - 1) / 3 ))
split -l $lines_per_file popular-names.txt