# el.py - dagens elpriser
### Jätteenkel web-scraper som hämtar dagens elpriser från elbruk.se
#### OBS: Priserna skrivs alltid ut i hela kronor, inte öre


```py
# Exempel

# OBS! pip3 install bs4

import el

x = el.EPrice("se2") # ändra till ditt elområde (se1, se2, se3, se4)

print(x.get_price("hr")) # -> skriver ut det aktuella timpriset
print(x.get_price("dl")) # -> skriver ut dagspriset
print(x.get_price("l_hr")) # -> skriver ut det lägsta timpriset för dagen
print(x.get_price("h_hr")) # -> skriver ut det högsta timpriset för dagen
```