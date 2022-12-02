#!/usr/bin/env bash

DIR=`dirname $(readlink -f $0)`
DAY_DIR=$DIR/day$1

CXX_DIR=$DAY_DIR/cxx
OUT_DIR=$DAY_DIR/out

FILE_ROOT=puzzle

if [ -d $DAY_DIR ]; then
    if [ -d $CXX_DIR ]; then
        mkdir -p $OUT_DIR
        
        for i in {1..2}; do
            IN_FILE=$CXX_DIR/$FILE_ROOT$i
            OUT_FILE=$OUT_DIR/$FILE_ROOT$i

            if [ -f $IN_FILE.cxx ]; then
                clang++ -Wall -g -std=c++17 -stdlib=libstdc++ -I $DIR/include/ $IN_FILE.cxx -o $OUT_FILE
            else
                echo $IN_FILE.cxx does not exist
            fi
        done
    else
        echo $CXX_DIR does not exist
    fi
else
    echo $DAY_DIR does not exist
fi
