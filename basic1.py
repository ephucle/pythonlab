text = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

print (text, '\n', '*'*10)
words = text.split()
#print (words)
sentence = ""

for word in words:
	
	#gap chu hoa thi in them ky tu xuong dong, ngoai tru chu I
	if word[0].isupper() == True and len(word) > 1:
		print ("\n")

	print(word,' ',end = '')

print ('\n')

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
