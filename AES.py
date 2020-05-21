#Roberto Perez Mendoza
#AES.py class

import sys
import os
import binascii
#python crypto library 
from Crypto.Cipher import AES as aes

class AES():
	#check that length of path meets the requirement
	def setKey(self, key):
		#length must equal to 32
		if len(key) == 32:
			self.key = str(binascii.unhexlify(key))
			return 1
		else:
			print("You entered a length of " +str(len(key))+ " Keys out of 32 hex required.")
			return 0

#=================AES encryption=========================================
	#Function to encrypt AES
	def encrypt(self, plaintext):
		ciphertext = ""
		new_val = aes.new(self.key, aes.MODE_ECB)

		##########################################
		# Add padding to the plaintext
		# @param plaintext - the original plaintext
		# @return - the padded plaintext
		###########################################	
		leftOverBlockSize = len(plaintext) % 16
		pad = (16 - leftOverBlockSize)

		if leftOverBlockSize != 0:
			#adding padding
			plaintext += chr(pad)

		for i in range(0, len(plaintext), 16):
			ciphertext += new_val.encrypt(plaintext[i:i+16])

		return ciphertext
#=========================End of encryption==================================

#==========================AES decryption====================================
	#Function to decryt AES
	def decrypt(self, ciphertext):
		plaintext = ""
		new_val = aes.new(self.key, aes.MODE_ECB)

		for i in range(0, len(ciphertext), 16):
			plaintext += new_val.decrypt(ciphertext[i:i+16])

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
