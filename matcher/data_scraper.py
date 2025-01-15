import requests
from bs4 import BeautifulSoup

class Scraper():
    
    def __init__(self):
        self.parts = []
        self.base_url = "https://www.jensonusa.com/"
        self.search_url = "https://www.jensonusa.com/search?q="
        self.search_term = ""


    def add_part(self, name, price, specs, url):
        part = {
            "name": name,
            "brand": brand, 
            "specifications": specifications,
            "url": url
        }
        self.parts.append(part)


    def scrape(self):
        response = requests.get(self.search_url + self.search_term)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print information about the search term
        print("Searching for: " + self.search_term)
        



if __name__ == "__main__":
    scraper = Scraper()
    scraper.search_term = "hub"
    scraper.scrape()
