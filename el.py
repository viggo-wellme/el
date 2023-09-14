import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.elbruk.se/timpriser-se3-stockholm")
soup = BeautifulSoup(req.text, "html.parser")


def get_price(soup: BeautifulSoup, _type: str) -> float:
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

print(get_price(soup, "hr"))