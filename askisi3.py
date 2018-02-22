#!/usr/bin/python

plaintext = raw_input('Enter the message: ')
key = 13
ciphertext = ""
for character in plaintext:
  #if its alphabetic
   if character.isalpha():
     #if its upper
     if character.isupper():
       is_uppercase = True
       #change to lower
       character = character.lower()
     else:
       is_uppercase = False
     #From ascii to decimal and add the key
     character = ord(character) + key
     #checking if character is decimal 122
     if character > 122:
	character = character - 26
     character = chr(character)
     #if character is upper
     if is_uppercase:
	character = character.upper()
     ciphertext = ciphertext + character
   #if character not alphabetic
   else:
      ciphertext = ciphertext + character
#print encrypted message
print "Encrypted message: " + ciphertext
