# extracting  sourcecode from url
from urllib.request import urlopen  
page=urlopen("https://www.w3schools.com/")
sourcecode=page.read()
print(sourcecode)