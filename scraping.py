import requests
from bs4 import BeautifulSoup
import csv

class Nouvelis:
    def __init__(self, url='https://lenouvelliste.com/'):
        self.url = url

    def get_paj(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as w:
            print(f"gen yon ere : {w}")
            return None

    def scrap(self, soup):
        atiks = soup.find_all('div', class_='lnv-featured-article') + soup.find_all('div', class_='lnv-featured-article-sm')
        data_lis = []

        for atik in atiks:
            tit = atik.find('h1').text.strip()
            link = self.url + atik.find('a')['href'] if atik.find('a') else None
            imaj = atik.find('img')['src'] if atik.find('img') else None
            deskripsyon = atik.find('p').text
            print('\n')
            data_lis.append([tit])
            print('\n')
            data_lis.append([link])
            print('\n')
            data_lis.append([imaj])
            print('\n')
            data_lis.append([deskripsyon])

        return data_lis

    def save_csv(self, dat, csv_file='wen.csv'):
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow(['Titre', 'Lien', 'Imaj', 'Deskripsyon'])
            csv_writer.writerows(dat)

    def scrap_nouvelis(self):
        url = self.url
        pag = self.get_paj(url)

        if pag:
            soup = BeautifulSoup(pag, 'html.parser')
            data = self.scrap(soup)
            self.save_csv(data)
            print("sikse.")

if __name__ == "__main__":
    scrap = Nouvelis()
    scrap.scrap_nouvelis()
