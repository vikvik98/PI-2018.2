import requests
import re
def main():

	arq = open("C:/Users/Vinicius/Downloads/text.txt", 'w')

	url = input("URL : ")
	response = requests.get(url)

	
	link_re = re.findall(r"<a href[=\"http://www.\w*./?-]+[\ ]+[\w*=> ]+</a>", response.text)

	links = ""

	for link in link_re:
		links += link

	

	arq.write(links)
	arq.close()


if __name__ == '__main__':
	main()