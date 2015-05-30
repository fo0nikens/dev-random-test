

/dev/random plotter

## run-hex.sh works on OSX.  Not tested on linux yet.
## run-octal still broken (problem with plotoct.py

##Requirements: matplotlib

## Run

First, you must create an input file.  Do for example

	$ dd if=/dev/random of=randfile bs=1024 count=2
	$ hexdump randfile > infile
	$ ./hexplot.py infile

For the impatient: do

	$ ./run.sh 

to generate a plot right away.  Edit the block size and count parameters to adjust the plot. Large block counts dont like to write in linux, unless you use /dev/urandom.  In OSX, /dev/random and /dev/urandom are identical.

 

