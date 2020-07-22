import re, sys
#text = sys.argv[1]

def make_slug(text):
	special_character = "!@#$%^&*()[]{};:,./<>?\|`~=_ +"
	'''
	#>>> make_slug("hello world")
	#'hello-world'
	#>>> make_slug("hello  world!")
	#'hello-world'
	#>>> make_slug(" --hello-  world--")
	#'hello-world'
	'''
	#print(special_character)
	print(f"Origin text:{text}")
	
	#replace end special character with ""
	
	text_after_replace1 = re.sub(r'[" !-"]+$',"", text)
	#print('text_after_replace1', text_after_replace1)
	
	
	text_after_replace2 = re.sub(r'^[" !-"]+',"", text_after_replace1)
	#print('text_after_replace2', text_after_replace2)
	#replace midle special character with "-"
	
	
	text_after_replace3 = re.sub(r'[" !-"]+',"-", text_after_replace2)
	#print('text_after_replace3', text_after_replace3)
	return text_after_replace3

#new_text = make_slug(text)
#print(f"new text: {new_text}")