#!/usr/bin/env bash

SESSION=$(<SESSION)
DIR=day$1

if [ -d $DIR ]; then
    echo 'Already Created' ./$DIR.  Just downloading input...
else
    mkdir $DIR
    mkdir $DIR/py
    mkdir $DIR/cxx
fi

curl https://adventofcode.com/2022/day/$1/input --cookie session=$SESSION --output $DIR/input.txt