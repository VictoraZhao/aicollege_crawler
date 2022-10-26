# Author: Victor Zhao

import requests
homepage = 'http://b.ai-collage.com/login'
# open and read the urls containing lecture materials from urls.txt
# format: one url in each line
#  a valid url looks like: 
# http://b.ai-collage.com/main/gateway?id=<id>&title=<title>&ico=<ico>
with open('urls.txt','r') as f:
    urls = f.readlines()
# login: enter your username and password here
credentials = {
    'userName': '',
    'password': '',
    'checked': '1'
}
with requests.Session() as s:
    # initiate login session (using correct credentials)
    p = s.post(homepage, data = credentials)
    for i in range(len(urls)):
        # open a url and retrieve page
        url = urls[i].strip()
        r = s.get(url)
        page = r.text
        # locate file full url
        start = page.find('furl=') + 5
        fileUrl = ''
        offset = 0
        while True:
            if page[start + offset] == "'":
                break
            else:
                fileUrl = fileUrl + page[start+offset]
                offset += 1
        # locate file name
        start = page.find('<title>') + 7
        fileName = ''
        offset = 0
        while True:
            if page[start + offset] == "<":
                break
            else:
                fileName = fileName + page[start+offset]
                offset += 1
        # retrieve file and save it
        r2 = requests.get(fileUrl)
        with open(fileName, 'wb') as f:
            f.write(r2.content)
        print(fileName + ' downloaded.')