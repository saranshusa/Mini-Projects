# This program downloads the github profile picture of the provided username.

import requests
from bs4 import BeautifulSoup as BS

user = input('Input GitHub Username: ')
url = f'https://github.com/{user}'
R = requests.get(url)
soup = BS(R.content, 'html.parser')
profileImage = soup.find('img', {'alt' : 'Avatar'})['src']

print(f'\nSuccessfully downloaded ! You may also go to the link below to open the image in web browser\n\n{profileImage}\n')

# Auto downloads the image
R = requests.get(profileImage, allow_redirects=True)
open(f'{user}.jpg', 'wb').write(R.content)