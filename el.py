import requests
from bs4 import BeautifulSoup

class EPrice:
    def __init__(self, area: str) -> None:
        areas = {
            "se1": "https://www.elbruk.se/timpriser-se1-lulea",
            "se2": "https://www.elbruk.se/timpriser-se2-sundsvall",
            "se3": "https://www.elbruk.se/timpriser-se3-stockholm",
            "se4": "https://www.elbruk.se/timpriser-se4-malmo"
        }
        
        self.area = areas[area]
    

    def get_price(self, _type: str) -> float:
        r = requests.get(self.area)
        soup = BeautifulSoup(r.text, "html.parser")

        types = {
            "dl": 0,   # daily price
            "hr": 1,   # hourly price
            "l_hr": 2, # lowest hourly price
            "h_hr": 3  # highest hourly price
        }

        # get the prices
        values = soup.find_all("span", {"class": "info-box-number"})
        # get the price and stringify it
        str_price = values[types[_type]].string
        # change "," to "." so python can understand
        str_price = str_price.replace(",", ".") 

        # make the price a float and divide by 100 to make it "kronor" and not "öre"
        fl_price = float(str_price)/100

        return fl_price