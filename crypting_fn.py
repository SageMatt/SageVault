#!/usr/bin/python

from Crypto.Cipher import AES
import base64

def encoder( str ):
   print "String:"+str
   secret_key = '1234567890123456'
   cipher = AES.new(secret_key,AES.MODE_ECB)
   msg_textval=str.rjust(32)
   encoded = base64.b64encode(cipher.encrypt(msg_textval))
   print "Encoded"
   print encoded.strip()
   print str
   return;

str1=raw_input("Enter the Text: ")
encoder(str1)
