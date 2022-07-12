# PersianCalender
 
## Introduction :
This package library helps user to get date in 3 kinds of calandar types: Georgian, Solar(Persian), Hijri(arabic).
internet connection is requiered for this library. because this library is a web scraping project. the library gives you information with scraping (https://www.time.ir/).



## Installation :

use this command on your terminal to install this package:
```
pip install persian-date
```

### classes :

There are 3 classes for each kind of calendars
- SolarDate
- GregorianDate
- HijriDate


### methods :
Each class contains 2 method for themselves , one of that methods uses for show date with numbers and another one is for showing date with charachters
- ` show_numeral() ` is for show date with numbers.
- ` show_char() ` is for show date with charachters.



## Examples:
This example is for showing date with numbers:

```
from PersianDate import GregorianDate

today = GregorianDate.show_numeral()
print(today)
```
> 2022-07-12


This example is for showing date with charachters:

```
from PersianDate import GregorianDate

today = GregorianDate.show_char()
print(today)
```

> Tuesday - 2022 12 July

