import urllib.request

def main():

	url = input("URL da imagem: ")
	urllib.request.urlretrieve(url,"local-filename.jpg")

if __name__ == '__main__':
	main()