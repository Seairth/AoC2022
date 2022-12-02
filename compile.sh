#!/usr/bin/env bash

DIR=./day$1
CXX_DIR=$DIR/cxx
OUT_DIR=$DIR/out

FILE_ROOT=puzzle

if [ -d $DIR ]; then
    if [ -d $CXX_DIR ]; then
        mkdir -p $OUT_DIR
        
        for i in {1..2}; do
            IN_FILE=$CXX_DIR/$FILE_ROOT$i
            OUT_FILE=$OUT_DIR/$FILE_ROOT$i

            if [ -f $IN_FILE.cxx ]; then
                clang++ -Wall -g -std=c++17 -stdlib=libstdc++ -I ./include/ $IN_FILE.cxx -o $OUT_FILE
            else
                echo $IN_FILE.cxx does not exist
            fi
        done
    else
        echo $CXX_DIR does not exist
    fi
else
    echo $DIR does not exist
fi
