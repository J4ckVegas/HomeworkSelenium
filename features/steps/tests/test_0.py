from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


INPUT_SEARCH = '//input[@class="input__control input__input"]'
BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'


def test():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(executable_path='/Users/dmitrijanaskin/PycharmProjects/lessons/webdrivers/chromedriver',
                              chrome_options=chrome_options)

    driver.get('https://yandex.ru')

    def get_element(xpath: str):
        try:
            element = WebDriverWait(driver=driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = driver.find_element(By.XPATH, xpath)
        return element

    def click(xpath):
        element = get_element(xpath=xpath)
        element.click()

    def fill_input(xpath, value):
        element = get_element(xpath=xpath)
        element.send_keys(value)

    click(xpath=INPUT_SEARCH)
    fill_input(xpath=INPUT_SEARCH, value='Питон')

    click(xpath=BUTTON_SEARCH)

    print()
