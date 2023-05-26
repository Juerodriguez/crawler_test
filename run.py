from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
        print(context.title)
        # Esperar explicita hasta cargar

        # Listar sucursales

        # Elegir sucursal


        # Extraer las urls de todas las categorias en una lista


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

