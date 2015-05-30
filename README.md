

/dev/random plotter

##Requirements: 
* python
* matplotlib
* bash, I guess.  Use your favorite shell :)

## Run

First, you must create an input file.  Do for example

	$ dd if=/dev/urandom of=randfile bs=1024 count=20
	$ hexdump -C randfile > infile
	$ ./linePlot.py infile

For the impatient: do

	$ ./linePlot.sh

or

	$ ./histogram.sh 

to generate something right away.  Edit the block size and count parameters to adjust the plot. Large block counts dont like to write in linux, unless you use /dev/urandom.  In OSX, /dev/random and /dev/urandom are identical.

 

