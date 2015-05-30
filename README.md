

/dev/random plotter

## works on OSX.  Not tested on linux yet.

##Requirements: matplotlib

## Run

First, you must create an input file.  Do for example

	$ dd if=/dev/random of=randfile bs=1024 count=2
	$ hexdump randfile > infile
	$ ./hexplot.py infile

For the impatient: do

	$ ./run.sh 

to generate a plot right away.  Edit the block size and count parameters to adjust the plot.  You may need to change the first line of run.sh to work with your environment variables. Do 

	$ which bash

to find out what to put in that line.  
