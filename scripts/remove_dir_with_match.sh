# remove a directory if it contains a file that matches grep

for d in *; do
    grep -R "coordinate integer" $d > /dev/null
    if [[ 0 = $? ]]; then
        rm -rfv $d
    fi
done