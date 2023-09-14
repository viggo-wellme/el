# el.py - dagens elpriser
### Jätteenkel web-scraper som hämtar dagens elpriser från elbruk.se

```py
# Exempel

# OBS! pip3 install bs4

import el
from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.elbruk.se/timpriser-se3-stockholm") # ändra länken till ditt område
soup = BeautifulSoup(req.text, "html.parser")

print(el.get_price(soup, "hr")) # -> skriver ut det aktuella timpriset
print(el.get_price(soup, "dl")) # -> skriver ut dagspriset
print(el.get_price(soup, "l_hr")) # -> skriver ut det lägsta timpriset för dagen
print(el.get_price(soup, "h_hr")) # -> skriver ut det högsta timpriset för dagen
```