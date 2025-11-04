# PersianDate

**PersianDate** is a lightweight Python library that provides the current date in three different calendar systems:
- **Gregorian**
- **Solar Hijri (Persian)**
- **Hijri (Islamic)**

Unlike most libraries, PersianDate does **not** rely on any system clock or time server.  
Instead, it automatically scrapes the official [Time.ir](https://www.time.ir/) website to extract the current date directly from its HTML content.  
This makes it accurate and timezone-independent as long as an internet connection is available.

---

## 🚀 Installation

You can install the package using pip:

```bash
pip install persian-date
```

---

📚 Classes

The library provides three main classes, one for each calendar type:

SolarDate

GregorianDate

HijriDate


Each class contains two main methods:

Method	Description

show_numeral()	Returns the date in numeric format (e.g. 1404-08-13)
show_char()	Returns the date in textual format (e.g. Tuesday - 2025 13 November)



---

💡 Examples

Example 1 – Numeric date output:
```python
from persian_date import GregorianDate

today = GregorianDate.show_numeral()
print(today)
```

Output: 
```bash
2025-11-04
```

Example 2 – Textual date output:
```python
from persian_date import GregorianDate

today = GregorianDate.show_char()
print(today)
```

Output: 
```bash
Tuesday - 2025 04 November
```

---

🌐 Notes

Internet connection is required because the library fetches and parses live data from Time.ir.

Ideal for Persian or multilingual date applications.



---

Author: Bardia Nikbakhsh 
Email: Bardianikbakhsh@gmail.com
GitHub: https://github.com/bardianz/PersianDate-python-package