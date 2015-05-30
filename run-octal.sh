#!/usr/bin/env bash

dd if=/dev/random of=./randfile bs=64 count=100 && od randfile > infile; ./plotoct.py infile


