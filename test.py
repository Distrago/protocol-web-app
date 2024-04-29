import api_google
service = api_google.service_sheets 
import requests
from bs4 import BeautifulSoup
import json



filePath = "C:\Csort\social\component_1.png"


searchUrl = 'https://yandex.ru/images/search'
files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
response = requests.post(searchUrl, params=params, files=files)
query_string = json.loads(response.content)['blocks'][0]['params']['url']
img_search_url= searchUrl + '?' + query_string
print(img_search_url)

'https://yandex.ru/images/search?source=collections&rpt=imageview&url=https://finobzor.ru/uploads/posts/2016-10/org_bvzz343.jpg'
result = requests.get(img_search_url)
soup = BeautifulSoup(result.text, 'lxml')
similar = soup.find('div', class_="CbirObjectResponse-Title").text
print(similar)
similar = soup.find('div', class_="Tags Tags_type_expandable Tags_view_buttons")
similar = similar.findAll('a')
for element in similar:
    print(element.text)

'https://yandex.ru/images/search?source=collections&rpt=imageview&url=https://finobzor.ru/uploads/posts/2016-10/org_bvzz343.jpg'
result = requests.get('https://yandex.ru/images/search?source=collections&rpt=imageview&url=https://finobzor.ru/uploads/posts/2016-10/org_bvzz343.jpg')
soup = BeautifulSoup(result.text, 'lxml')
similar = soup.find('div', class_="CbirObjectResponse-Title").text
print(similar)
similar = soup.find('div', class_="Tags Tags_type_expandable Tags_view_buttons")
similar = similar.findAll('a')
for element in similar:
    print(element.text)