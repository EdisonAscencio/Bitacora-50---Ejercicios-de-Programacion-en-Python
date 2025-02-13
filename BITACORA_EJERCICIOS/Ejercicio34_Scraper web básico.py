'''
Ejercicio 34: Scraper web básico

Crea un programa que haga un web scraping simple. 
Puedes usar una biblioteca como BeautifulSoup para extraer 
información de una página web.
'''

import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML de la página web
        soup = BeautifulSoup(response.text, 'html.parser')

        # Aquí puedes realizar la extracción de la información que necesitas
        # Por ejemplo, puedes encontrar e imprimir todos los enlaces de la página
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        # Si la solicitud no fue exitosa, imprimir un mensaje de error
        print("Error al acceder a la página:", response.status_code)

# URL de la página web a la que quieres hacer scraping
url = "https://www.youtube.com/"

# Llamar a la función web_scraper con la URL
web_scraper(url)