import re
def make_slug(text):
	
	
	text = re.sub("!", " ", text)  # ==> chuyen ky tu dac biet ve " " ==> de strip
	text = re.sub("-", " ", text)  # dung de chuyen ky tu dac biet - o hai dau thanh " "   ==> de sau nay strip
	text = re.sub("#", " ", text)
	text= text.strip()
	text = re.sub(" +", "-", text)  #replace 1 space  [" "], for many continuous space by "-"
	return text
	

print("hello world", "-->",  make_slug("hello world"))
print("hello world ","-->",make_slug("hello world "))
print("   hello world ","-->",make_slug("   hello world "))
print("hello world!", "-->",make_slug("hello world!"))
print("hello world#", "-->",make_slug("hello world#"))
print("!!hello world#", "-->",make_slug("!!hello world#"))
print("!!hello world   from   vietname#", "-->",make_slug("!!hello world   from   vietname#"))
print(" --hello-  world--", "-->",make_slug(" --hello-  world--"))

print("!!hello world  -!  from  -! vietname#", "-->",make_slug("!!hello world  -!  from  -! vietname#"))