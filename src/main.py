from bs4 import BeautifulSoup
import requests


url = 'https://www.time.ir/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


class SolarDate():

    def show_numeral():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsiNumeral").text

    def show_char():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi").text
         


class GregorianDate():

    def show_numeral():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblGregorianNumeral").text

    def show_char():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblGregorian").text


class HijriDate():

    def show_numeral():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblHijriNumeral").text

    def show_char():
        global soup
        return soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblHijri").text
        

