import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.aruodas.lt/gyvenamieji-namai/"
resource = requests.get(url)
content = resource.text
soup = BeautifulSoup(content,'html.parser')
skelbimai = soup.find_all('div', class_= 'list-row-v2 object-row selhouse advert')
duomenys= []
unikalus = set() #naujamas unikalioms reiksmės

for skelbimas in skelbimai:
    kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
    lokacija =skelbimas.select_one('.list-adress-v2 h3').text.strip() #h3 teksto dydis selektorius
    plotas = skelbimas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
    kaina= ''.join(c for c in kaina if c.isdigit())

    unikalus_id = (kaina, lokacija, plotas)

    if unikalus_id not in unikalus:

        duomenys.append({
            'kaina' : kaina,
            'lokacija' : lokacija,
            'plotas' : plotas
        })

df=pd.DataFrame(duomenys)
print(df)

ploto_vidurkis = df['plotas'].min()
print(ploto_vidurkis)

