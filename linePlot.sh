#!/usr/bin/env bash


# On linux, using /dev/random and /dev/urandom will produce different results. 
# Linux users will have to reduce the block count or wait for more
# entropy if /dev/random is used.

dd if=/dev/urandom of=./randfile bs=64 count=10 && hexdump -C randfile > infile; ./linePlot.py infile; rm randfile infile


