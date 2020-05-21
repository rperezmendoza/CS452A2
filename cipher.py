#Roberto Perez Mendoza
#cipher

import sys
import os

#importing cipher classes
from DES import DES
from AES import AES

#main class
def main(*arg):
        # REMOVE
        #des = DES()
        #des.setKey('0123456789abcdef')
        #ciphertext = des.encrypt("123456789a") 

        
       # print "Result: " + des.decrypt(ciphertext)
       # exit(0)

	#Ckecks that length of path meets the requirement CHECK
	if len(arg) < 6:
		print("\nError!!!\nArgument is too long/less\n")
		print("\nPlease try entering the following path:\n python ./cipher <CIPHER NAME><KEY><ENC/DEC><IPUT FILE><OUTPUT FiLE>")
		exit(-1)
	
	#declaring arguments 
	cname = arg[1]
	key = arg[2]
	encdec = arg[3]
	iFile = arg[4]
	oFile = arg[5]

	cipher = None
    #opens in.txt file and reads from it to encrypt/decrypt the message provided 
	with open(iFile, "r") as f:
		iString = f.read()	
			

	#This is for DES encryption
	if cname == "des":
		cipher = DES()
		if cipher.setKey(key):
			if encdec == "enc":
				output = cipher.encrypt(iString)
			elif encdec == "dec":
				output = cipher.decrypt(iString)
			else:
				print("\nError enc/dec not entered\n")
				exit(-1)
		else:
			print("\nError. Invalid des key\n")
			exit(-1)
	#This is for AES encryption
	elif cname == "aes":
		cipher = AES()
		if cipher.setKey(key):
			if encdec == "enc":
				output = cipher.encrypt(iString)
			elif encdec == "dec":
				output = cipher.decrypt(iString)
			else:
				print("\nError enc/dec not entered\n")
				exit(-1)
		else:
			print("\nError. Invalid aes key\n")
			exit(-1)
		
	#END, below is a selection for a cipher error selection	
	else:
		print("\nError. No class has been selected.\n")
		exit(-1)
		
	#displays the user's input and output
	print("\nWhat goes to the in.txt file (user's input): " + iString)
	print("\nWhat goes to the out.txt file (user's output): " + output)
	print("\n\n")

	#writing to the output file
	with open(oFile, "w") as out_f:
		out_f.write(output)
		print("\nEncryption was written to out.txt/Decryption was written to out2.txt")
		print("\NOTE: to decrypt message use out.txt first and then out2.txt.\n")

	#close all txt files
	f.close()
	out_f.close()

if __name__ == '__main__':
	main(*sys.argv)
