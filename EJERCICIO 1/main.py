import logging
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# vars
url_main = "https://www.demoblaze.com"
logger = logging.getLogger(__name__)


def get_driver() -> webdriver:
    """
    Obtiene el driver de conexión del cliente web.
    :return: driver de conexión
    """

    options = webdriver.ChromeOptions()

    # Agente
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')

    # Install driver
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def add_products(driver):
    """
    Agregar dos productos al carrito
    """

    # agregando dos productos
    max_quantity = 1
    len_cart = 0
    counter = 1  # Identificador del producto
    while len_cart <= max_quantity:
        url_product = url_main + '/prod.html?idp_=%s' % counter
        driver.get(url_product)
        time.sleep(5)

        ActionChains(driver).click(driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]")).perform()
        try:
            # Confirmar alert
            driver.switch_to.alert.accept()
        except Exception as e:
            pass

        len_cart += 1
        counter += 1
        logger.warning("Productos agregados: %s" % len_cart)


def complete_checkout(driver):
    """
    Completar el formulario de compra
    """
    # Visualizar el carrito
    url = url_main + '/cart.html'
    driver.get(url)

    # Invocando acción de formulario de compra
    ActionChains(driver).click(driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")).perform()

    # Completar datos de formulario
    data_fields = [
        {'id': 'name', 'value': 'Usuario Prueba'},
        {'id': 'country', 'value': 'Ecuador'},
        {'id': 'city', 'value': 'Quito'},
        {'id': 'card', 'value': '1234 5678 9132 4567'},
        {'id': 'month', 'value': '06'},
        {'id': 'year', 'value': '2022'},
    ]

    for field in data_fields:
        time.sleep(2)
        id = field.get('id')
        value = field.get('value')
        driver.find_element(By.ID, id).send_keys(value)

    # invocar a botón 'Purchase'
    time.sleep(2)
    ActionChains(driver).click(driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")).perform()
    time.sleep(5)
    # Pulsar el botón OK (Finalizar Compra)
    ActionChains(driver).click(driver.find_element(By.XPATH, "//button[contains(text(),'OK')]")).perform()


if __name__ == '__main__':
    # Obteniendo driver de conexión
    driver = get_driver()
    # añadir productos
    add_products(driver)
    time.sleep(2)
    # Completar compra
    complete_checkout(driver)
