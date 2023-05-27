from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv


class ContextWebDriver:
    """

    """

    def __init__(self):
        self.option = None
        self.driver = None

    def start(self):
        """

        :return:
        """
        self.option = Options()
        self.option.add_argument('--headless')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.option)
        return self.driver

    def close(self):
        """

        :return:
        """
        # Cerrar el navegador
        self.driver.quit()


class PageUrlScraper:
    """
    Este objeto esta implementado para obtener todas las URLS de las distintas categorias.

    """

    def __init__(self):
        self.sucursal = None
        self.url = "https://www.hiperlibertad.com.ar/"

    def scrape_categories_names_urls(self, context):
        """

        :param context:
        :return:
        """
        context.get(self.url)
        context.implicitly_wait(10)
        self._choose_sucursal(context=context)

        # html_source = context.page_source
        # soup = BeautifulSoup(html_source, 'lxml')

        # Extraer las urls de todas las categorias en una lista

    def _choose_sucursal(self, context):
        """


        :param context:
        :return:
        """
        list_identifier = []
        location_options = [["state", "26l3qy"], ["store", "1w9j89e"]]

        sucursal = context.find_element(By.CSS_SELECTOR, "body > div.jss15.jss1.styled__Popup-sc-17gyuk9-0.gHcMyJ.styles__StoreSelectorPopup-sc-3xue66-0.iOsPHA > div.jss4.jss2 > div > div > div > div > div.styles__Content-sc-1grwrp2-1.eOuAGp > button:nth-child(2)")

        sucursal.click()
        context.implicitly_wait(10)

        for id, location in enumerate(location_options):

            # Seleccionar menu desplegable
            selector_driver = context.find_element(By.CSS_SELECTOR, f'#{location[0]} > div > div.react-select__value-container.css-1hwfws3')
            selector_driver.click()
            context.implicitly_wait(10)

            # Conseguir el html con la lista de identificadores
            all_options_driver = context.find_element(By.CSS_SELECTOR, f'#{location[0]} > div.react-select__menu.css-{location[1]}-menu > div')
            identifier_html = all_options_driver.get_attribute('innerHTML')
            raw_list = identifier_html.split("</div>")
            raw_list.pop()

            # Filtrar el texto del identificador
            for i, raw_location_identifier in enumerate(raw_list):
                _, identifier = raw_location_identifier.split(">")
                list_identifier.append((i, identifier))

            id_identifier = str(input(f"Elegir el numero de la {location[0]} donde esta la sucurcal a consultar: {list_identifier}"))
            identifier_driver = context.find_element(By.ID, f'react-select-{id+2}-option-{id_identifier}')
            identifier_driver.click()
            list_identifier.clear()
            context.implicitly_wait(10)

        confirmar = context.find_element(By.CSS_SELECTOR, "body > div.jss15.jss1.styled__Popup-sc-17gyuk9-0.gHcMyJ.styles__StoreSelectorPopup-sc-3xue66-0.iOsPHA > div.jss4.jss2 > div > div > div > div > form > div.styles__Content-sm1gtl-2.BoPEx > button")
        confirmar.click()


class WebSiteScraper:

    def __init__(self, num_threads):
        self.num_threads = num_threads

    def web_scraper(self, url_list_categories):
        """
        Método que extrae los productos de cada categoria.

        :param url_list_categories:
        :return:
        """
        pass


if __name__ == "__main__":
    context = ContextWebDriver().start()
    PageUrlScraper().scrape_categories_names_urls(context=context)
    context.close()
