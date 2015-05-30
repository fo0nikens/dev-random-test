#!/bin/bash

dd if=/dev/random of=./randfile bs=1024 count=2 && hexdump randfile > infile; ./plothex.py infile


