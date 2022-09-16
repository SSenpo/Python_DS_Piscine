#bin/sh

INPUT_FILE="../ex01/hh.csv"

OUTPUT_FILE=hh_sorted.csv

cat $INPUT_FILE \
| head -n 1 \
> $OUTPUT_FILE

cat $INPUT_FILE \
| tail -n +2 \
| sort --field-separator=',' --key=1,1 --key=2,2 \
>> $OUTPUT_FILE