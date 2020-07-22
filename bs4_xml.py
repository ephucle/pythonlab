# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
content = []
def prettify_xml_file(file_path):
	with open(file_path, 'r' , encoding ="ISO-8859-1") as file:
		# Read each line in the file, readlines() returns a list of lines
		content = file.readlines()
		# Combine the lines in the list into a string
		content = "".join(content)
		bs_content = bs(content, "lxml")

		
		print(bs_content.prettify())


def main():
	prettify_xml_file("mhweb_searchresult.xml")
	
if __name__ == "__main__":
	main()