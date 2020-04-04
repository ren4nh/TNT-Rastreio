import tnt

class ScrapingFactory:
    def scrap(self, data):
        scraping = get_scraping(data['type'])
        return scraping.scrap(data)

def get_scraping(type):
    if type == 'TNT':
        return tnt.TntHandler()
    else:
        raise ValueError(type) 