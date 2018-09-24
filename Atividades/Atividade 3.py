import requests
def main():

	arq = open("C:/Users/Vinicius/Downloads/text.txt", 'w')

	url = input("URL : ")
	response = requests.get(url)
	
	arq.write(response.text)
	arq.close()


if __name__ == '__main__':
	main()