

/dev/random plotter

##Requirements: 
* python
* matplotlib
* bash, I guess.  Use your favorite shell :)

## Run

First, you must create an input file.  Do for example

	$ dd if=/dev/random of=randfile bs=1024 count=2
	$ hexdump -x randfile > infile
	$ ./hexplot.py infile

For the impatient: do

	$ ./run.sh 

to generate a plot right away.  Edit the block size and count parameters to adjust the plot. Large block counts dont like to write in linux, unless you use /dev/urandom.  In OSX, /dev/random and /dev/urandom are identical.

 

