find `pwd` -type f >> result

vim result && :%s/extension_name//g

cat resutlt perl -nle 's/(.*\/)/\1 /;print' | sort -k2 | uniq -f 1 -D | sed -e 's/ //' >> result.txt
