from urllib.request import urlopen
from urllib.parse import urljoin
from lxml.html import fromstring

class Parser(object):
    """Parse AM.RU page"""

    page_url = ""

    def __init__(self, url):
        self.page_url = url

    def parse_auto(self):
        result = {'year':[], 'price':[], 'mileage': [], 'condition': [], 'bodytype': [], 'fueltype' :[], \
            'litre' : [], 'gearboxtype' : [], 'gearing' : []}

        current_page = 1
        link_obtained = True
        URL = self.page_url

        while link_obtained:
            link_obtained = False
            response = urlopen(URL)
            html = response.read().decode('utf-8')
            doc = fromstring(html)

            for info_block in doc.cssselect('.b-snippet'):
                year = info_block.cssselect('.title span')[0]
                year = year.text[1:]
                year = str(int(year) - 2000)
                price = info_block.cssselect('.price-block .price')[0]
                car_info = info_block.cssselect('.car-info')

                #info_top contains mileage and condition
                #new_info_top contains info about NEW auto

                new_info_top = info_block.cssselect('.status-new')
                if len(new_info_top) != 0:
                    mileage = 0
                    condition = new_info_top[0].text
                else:
                    info_top = car_info[0].text.split('\u043a\u043c\u002c')
                    if len(info_top) < 2:
                        continue
                    mileage = info_top[0].replace("\xa0",'')
                    damaged_info = info_block.cssselect('.status-damaged')
                    if len(damaged_info) != 0:
                        condition = damaged_info[0].text
                    else:
                        condition = info_top[1].strip()
                        #Sometimes the status field includes extra comma
                        if condition[len(condition) - 1] == ',':
                            condition = condition[:len(condition) - 1]

                #info_bottom contains body type, gearing, et cetera
                info_bottom = car_info[1].text.split(', ')
                if len(info_bottom) < 5:
                    continue

                litre = info_bottom[2].replace('\xa0\u043b','')
                gearing = info_bottom[4].replace(' ', '_')

                result['year'].append(year)
                result['price'].append(price.text.replace(' ', ''))
                result['mileage'].append(mileage)
                result['condition'].append(condition)
                result['bodytype'].append(info_bottom[0])
                result['fueltype'].append(info_bottom[1])
                result['litre'].append(litre)
                result['gearboxtype'].append(info_bottom[3])
                result['gearing'].append(gearing)

            doc = doc.cssselect('.au-ctrl-next')
            if len(doc) != 0:
                URL = doc[0].get('href')
                link_obtained = True


        return result