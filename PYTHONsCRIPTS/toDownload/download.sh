#!/bin/bash



for i in `cat s.url`; 
do 
	wget "$i" -O tmp.html
	UU=$(grep -B2 "Download book PDF" tmp.html  | grep pdf| cut -d= -f2| cut -d\" -f2)
	wget "http://link.springer.com/${UU}"
	rm -f tmp.html index.html*

done
