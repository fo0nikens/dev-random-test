#!/usr/bin/env bash

dd if=/dev/random of=./randfile bs=64 count=100 && hexdump randfile > infile; ./plothex.py infile


