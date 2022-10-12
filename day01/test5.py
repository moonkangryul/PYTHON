from urllib import response
import requests

URL =  'https://www.naver.com'
response = requests.get(URL)
html_text = response.text
# print(html_text)
print(html_text.find('<h3 class="blind">'))