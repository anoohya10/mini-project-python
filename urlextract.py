from urllib.request import urlopen  
page=urlopen("https://www.w3schools.com/")
print(page.headers)