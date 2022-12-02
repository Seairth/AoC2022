#!/usr/bin/env bash

SESSION=$(<SESSION)
DIR=day$1

FILE_ROOT=puzzle

if [ -d $DIR ]; then
    echo 'Already Created' ./$DIR. 'Copying templates and downloading input...'
else
    mkdir -p $DIR
    mkdir -p $DIR/py
    mkdir -p $DIR/cxx
fi

for i in {1..2}; do
    for lang in cxx py; do
        DST_FILE=$DIR/$lang/$FILE_ROOT$i.$lang
        SRC_FILE=./template/$lang/$FILE_ROOT$i.$lang
        
        if [ ! -f $DST_FILE ]; then
            cp $SRC_FILE $DST_FILE
        fi
    done
done

curl https://adventofcode.com/2022/day/$1/input --cookie session=$SESSION --output $DIR/input.txt