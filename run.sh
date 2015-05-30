#!/usr/bin/env bash

dd if=/dev/random of=./randfile bs=64 count=10 && hexdump -C randfile > infile; ./plothex.py infile; rm randfile infile


