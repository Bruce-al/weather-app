# Author: MBM
# Important Dates: 22/06/23, Mj, Md, 28/02/06, 01/03/04, 30/06/66, 21/06/67

import requests
city = input('City: ')
res = requests.get(f'https://wttr.in/{city}?format=3')
print(res.text)