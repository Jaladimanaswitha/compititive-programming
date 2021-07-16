# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	res=''
	for i in msg:
		if(i.isalpha()==False):
			res+=i
		a=ord(i)
		if((a+shift<91 and a+shift>64) or(a+shift<123 and a+shift>96)):
			res+=chr(a+shift)
		elif(shift<0):
			res+=chr(a+shift+26)
		else:
		# elif(a+shift>90 or a+shift<122 ):
		# elif(shif<0):
			res+=chr(a+shift-26)
		# else:
		# 	res+=chr(a+shift+26)
	return res

print(fun_applycaesarcipher("We Attack At Dawn", 1))


