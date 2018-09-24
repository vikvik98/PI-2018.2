import requests
def main():

	url = input("URL : ")
	response = requests.get(url)
	print(response.status_code)
	print(response.headers['content-type'])

if __name__ == '__main__':
	main()