# !/usr/bin/env bash
solution=0
array=($(ggrep -oP "mul\([0-9]+,[0-9]+\)" inputs/day_3.txt | ggrep -oP "[0-9]+,[0-9]+"))
for el in $array; do
    IFS=',' read -rA numbers <<< "$el"
    num1=$numbers[1]
    num2=$numbers[2]
    solution=$((solution +($num1 * $num2)))
done
echo $solution

