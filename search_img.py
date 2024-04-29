import requests
from bs4 import BeautifulSoup
import json
import base64

def search_img(filePath):    
    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    
    result = requests.get(img_search_url)
    soup = BeautifulSoup(result.text, 'lxml')
    try:
        similar = soup.find('div', class_="CbirObjectResponse-Title").text
    except:
        pass
        
    similar = soup.find('div', class_="Tags Tags_type_expandable Tags_view_buttons")
    similar = similar.findAll('a')
    
    similar_arr = []
    for element in similar:
        similar_arr.append(element.text)
    
    return similar_arr

def parce_textContent(textContent):
    soup = BeautifulSoup(textContent, 'lxml')
    try:
        similar = soup.find('div', class_="CbirObjectResponse-Title").text
    except:
        pass
        
    similar = soup.find('div', class_="Tags Tags_type_expandable Tags_view_buttons")
    similar = similar.findAll('a')
    
    similar_arr = []
    for element in similar:
        similar_arr.append(element.text)
    
    return similar_arr
    
def parce_URL(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'lxml')
    try:
        similar = soup.find('div', class_="CbirObjectResponse-Title").text
    except:
        pass
        
    similar = soup.find('div', class_="Tags Tags_type_expandable Tags_view_buttons")
    similar = similar.findAll('a')
    
    similar_arr = []
    for element in similar:
        similar_arr.append(element.text)
    
    return similar_arr