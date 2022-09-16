#!/bin/sh

OUTPUT_FILE="./hh.json"
PAGE_SELECT="20"

SEARCH_NAME="data&scientist"

curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$SEARCH_NAME&page=0&per_page=$PAGE_SELECT" | jq > $OUTPUT_FILE
