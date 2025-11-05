# PersianDate

**PersianDate** is a lightweight Python library that provides the current date in three different calendar systems:
- **Gregorian**
- **Solar Hijri (Persian)**
- **Hijri (Islamic)**

## 🧩 About this project

A while ago, I needed a reliable way to get the Persian date on a remote server that didn’t support Solar Hijri calendars.
Most libraries depended on the system clock or failed due to timezone issues, so I built a lightweight, dependency-free solution that fetches accurate dates directly from Time.ir.

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

## 📚 Classes

The library provides three main classes, one for each calendar type:

| Class          | Description                  | Methods                                 |
|----------------|-----------------------------|----------------------------------------|
| `SolarDate`    | Persian (Solar Hijri) date  | `show_numeral()`, `show_char()`        |
| `GregorianDate`| Gregorian date              | `show_numeral()`, `show_char()`        |
| `HijriDate`    | Islamic (Hijri) date        | `show_numeral()`, `show_char()`        |

**Methods:**

- `show_numeral()` → Returns the date in numeric format (e.g., `1404-08-13`)  
- `show_char()` → Returns the date in textual format (e.g., `Tuesday - 2025 04 November`)



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
