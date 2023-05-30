import requests
import pandas as pd
def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			return(f"{url}: is reachable")
		else:
			return(f"{url}: is Not reachable, status_code: {get.status_code}")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
# print(url_checker("https://notworking.com"))
df1 = pd.read_csv("Result.csv")
urls = df1.URL
print(urls)
print(len(urls))
for i in range(0, len(urls)):
	print(url_checker(urls[i]))