import requests
from bs4 import BeautifulSoup as bts
import pandas as pd

data = {'Page': [], 'Title': []}
df = pd.DataFrame(data)

i = 1
base_url = "https://unair.ac.id/category/featured/"

while True:
    url = f"{base_url}page/{i}/"
    response = requests.get(url)

    # checking status
    if response.status_code == 404:
        break

    soup = bts(response.text, "html.parser")

    # article title process
    for article in soup.find_all('div', class_='elementor-post__text'):
        h3 = article.find('h3', class_='elementor-post__title')
        if h3:
            title = h3.get_text(strip=True)
            df = df.append({'Page': f"Page {i}", 'Title': title}, ignore_index=True)
    i += 1

# save to a CSV file
df.to_csv("Nomor_2.csv", index=False)