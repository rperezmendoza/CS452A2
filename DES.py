#Roberto Perez Mendoza
#DES.py class

import sys
import os
import binascii
#python crypto library
from Crypto.Cipher import DES as des

class DES():
	#check that length of path meets the requirement
	def setKey(self, key):
		#length must equal to 16
		if len(key) == 16:
			self.key = str(binascii.unhexlify(key))
			return 1
		else:
			print("You entered a length of " +str(len(key))+ " Keys out of 16 hex required.")
			return 0

#=================DES encryption=========================================
    #Function to encrypt des
	def encrypt(self, plaintext):
		#padded =  self.addPadding(plaintext)
		# print padded
		# print self.removePadding(padded)
		# exit(0)

		ciphertext = ""
		new_val = des.new(self.key, des.MODE_ECB)

		##########################################
		# Add padding to the plaintext
		# @param plaintext - the original plaintext
		# @return - the padded plaintext
		###########################################	
		leftOverBlockSize = len(plaintext) % 8
		pad = (8 - leftOverBlockSize)

		if leftOverBlockSize != 0:
			#adding padding
			plaintext += chr(pad)

		for i in range(0, len(plaintext), 8):
			ciphertext += new_val.encrypt(plaintext[i:i+8])

		return ciphertext

#=========================End of encryption==================================
    


#==========================DES decryption====================================
	#Function to decrypt des
	def decrypt(self, ciphertext):
		plaintext = ""
		new_val = des.new(self.key, des.MODE_ECB)

		for i in range(0, len(ciphertext), 8):
			plaintext += new_val.decrypt(ciphertext[i:i+8])

		return self.removePadding(plaintext)
#============================End of decryption ==============================


#=======Remove Padding============================
	def removePadding(self, plaintext):
		npad = ord(plaintext[-1])

		if npad > 0 and npad < 8:
			if npad == 1 and plaintext[-2] != plaintext[-1]:
				#for one padding
				return plaintext[:len(plaintext)-1]
		
			for i in range(2, npad):
				if plaintext[-i] != plaintext[-1]:
					isPad = False
		if isPad:
			return plaintext[:len(plaintext)-npad]


