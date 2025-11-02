from urllib.request import urlopen
import gzip
import urllib
from bs4 import BeautifulSoup

web_url="http://python.org"

#request like a browser
browser_req=urllib.request.Request(web_url,data=None, headers={"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"})

#open data from the brwosed data
ptr=urllib.request.urlopen(browser_req)

#try to apply beautifulSoup to extract style and js
render_data=BeautifulSoup(ptr)

for filter_data in render_data(["script","style"]):
    filter_data.extract()

finaldata=render_data.get_text()
print(finaldata)



'''
ptr=urlopen(web_url)

#print(ptr.read())
#print(ptr.read().decode())


# Read all the data
data = ptr.read()


# Check if the response is gzip-compressed
if ptr.headers.get("Content-Encoding") == "gzip":
    data = gzip.decompress(data)

# Decode safely (using the right charset if available)
encoding = "utf-8"
text = data.decode(encoding, errors="replace")

print(text)
'''




