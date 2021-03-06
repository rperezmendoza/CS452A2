#Roberto Perez Mendoza
#################################################
############EXTRA CREDIT PORTION#################
#################################################
#############CBC and CFB "DES"###################

import sys
import binascii
import os
#python crypto library
from Crypto.Cipher import DES as des

class DES():
	def setKey(self, key):
		#length must equal to 16
		if len(key) == 16:
			self.key = str(binascii.unhexlify(key))
			return 1
		else:
			print("You entered a length of " +str(len(key))+ " Keys out of 16 hex required.")
			return 0

#=====Function for initialization "CHECKLINES 26-31"
############NOTE: THIS WILL DO RANDOM INITIALIZATION AS IT######################
##################IT WORKS FOR DECRYPTION ######################################
	def setInitial(self, isEncryption):
		randomBytes = 8
		if isEncryption:
			self.Initial = os.urandom(randomBytes)
			print("Below is a randomly selected initial: \n" + binascii.hexlify(self.Initial) + "\n")
		return 1

#==========================CBC====================================================
#Start here
#=======================ENCRYPT=========================================
	def encryptCBC(self, plaintext):
		ciphertext = ""
		#if statement to store the bytes from the ciphertext
		if not self.setInitial(True):
			ciphertext += str(self.Initial)

		n_val = des.new(self.key, des.MODE_ECB)

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

		bplaintext = ""
		for i in range(0, 8):
			# XOR
			bplaintext += chr(ord(self.Initial[i]) ^ ord(plaintext[i]))

		for i in range(0, len(plaintext), 8):
			bcipher = n_val.encrypt(bplaintext)
			ciphertext += bcipher

			if i+8 < len(plaintext):
				XOR = [None] * 8
				bplaintext = plaintext[i+8:i+16]
				#XOR of bcipher and bplaintext
				for mlist in range(0, len(bcipher)):
					XOR[mlist] = chr(ord(bcipher[mlist]) ^ ord(bplaintext[mlist]))

				bplaintext = "".join(XOR)

		return ciphertext

#==========================DECRYPT===================================================
	#function to decrypt des in CBC
	def decryptCBC(self, ciphertext):
		plaintext = ""
		if not self.setInitial(False):
			self.Initial = ciphertext[0:8] 
			ciphertext = ciphertext[8:] 

		n_val = des.new(self.key, des.MODE_ECB)

		for i in range(0, len(ciphertext), 8):
			bplaintext = n_val.decrypt(ciphertext[i:i+8])

			if i == 0:
				# XOR
				XOR = [None] * 8
				for mlist in range(0, 8):
					XOR[mlist] = chr(ord(self.Initial[mlist]) ^ ord(bplaintext[mlist]))
				plaintext += "".join(XOR)

			elif i+8 <= len(ciphertext):
				Block = [None] * 8
				#XOR of bcipher and bplaintext
				for mlist in range(0, len(bcipher)):
					Block[mlist] = chr(ord(bcipher[mlist]) ^ ord(plaintextBlock[mlist]))

				plaintext += "".join(Block)

			bcipher = ciphertext[i:i+8]

		return self.removePadding(plaintext)

#==========================END OF CBC========================================

#==========================CFB====================================================
#=======================ENCRYPT=========================================
	#function to encrypt des in CFB
	def encryptCFB(self, plaintext):
		ciphertext = ""
		n_val = des.new(self.key, des.MODE_ECB)
		if not self.setInitial(True):
			ciphertext += str(self.Initial)

		for char in plaintext:
			o = n_val.encrypt(self.Initial)
			ciphertext += chr(ord(o[0]) ^ ord(char))
			self.Initial = self.Initial[1:] + ciphertext[len(ciphertext)-1]

		return ciphertext

	#function to decrypt des in CFB
	def decryptCFB(self, ciphertext):
		plaintext = ""
		n_val = des.new(self.key, des.MODE_ECB)
		if not self.setInitial(False):
			self.Initial = ciphertext[0:8] 
			ciphertext = ciphertext[8:] 

		for char in ciphertext:
			b = n_val.encrypt(self.Initial)
			plaintext += chr(ord(b[0]) ^ ord(char))
			self.Initial = self.Initial[1:] + char

		return plaintext

#==========================END OF CFB========================================

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
