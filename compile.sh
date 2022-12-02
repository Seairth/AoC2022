#!/usr/bin/env bash

DIR=./day$1/cxx
FILE_ROOT=puzzle

if [ -d $DIR ]; then
    for i in {1..2}; do
        FILE=$DIR/$FILE_ROOT$i

        if [ -f $FILE.cxx ]; then
            clang++ -Wall -g -std=c++17 -stdlib=libstdc++ $FILE.cxx -o $FILE
        else
            echo $FILE.cxx does not exist
        fi
    done
else
    echo $DIR does not exist
fi
