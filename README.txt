CPSC452 Assignment2

Name: Roberto Perez Mendoza
Email: perezmendoza_roberto@csu.fullerton.edu

Programming language used: Python 2.7

How to execute the program: The program can be executed by openning the terminal
and looking the path to the folwer were the assingment2 is located. Look for the folder
p2_rperezmendoza1 and start typing the following: python ./cipher.py <CIPHER NAME><KEY><DEC/ENC><in.txt><out.txt>
As an example to what I did was python ./cipher.py des 0B02679B49A5FCEA enc in.txt out.txt and 
a successful output is being displayed. Note that for decrypting the message, one must have to use the file where the encryption message is and create a second outfile. e.g. ./cipher.py des 0B02679B49A5FCEA dec out.txt out2.txt  

Extra credit: Extra credit was implemented. The implementation is located under the extraCredit
directory. The process of running the program is similar to the assignment. 

Anything special: 
cipher names for assignment 2: 
     * des and aes
cipher names for extra credit:
     * dcbc and dcfb for DES
     * acbc and acfb for AES

Note: This program only works on pyton 2.7 and must have python crypto installed in order for it to work.
To install it do the following:
     * sudo apt-get update
     * sudo apt install python-pip
     * pip install pycrpto
