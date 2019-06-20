from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_1():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(executable_path='/Users/dmitrijanaskin/PycharmProjects/lessons/webdrivers/chromedriver',
                              chrome_options=chrome_options)
    driver.get('https://yandex.ru')

    def get_element(xpath):
        try:
            element = WebDriverWait(driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = driver.find_element(By.XPATH, xpath)
        return element

    def action(element, *args):
        element_type = element.tag_name
        if element_type == 'input':
            element.send_keys(*args)
        elif element_type == 'button' or element_type == 'a':
            element.click()
        elif element_type == 'select':
            if args[0].__class__ == str:
                Select(element).select_by_value(args[0])

    input_search = get_element('//input[@aria-label="Запрос"]')
    button_search = get_element('//button//*[text()="Найти"]/..')

    action(input_search, 'википедия')
    action(button_search)

    first_result = get_element('((//*[@class="main__content"]//li)[1]//a)[1]')
    action(first_result)

    driver.switch_to.window(driver.window_handles[1])

    button = get_element('//*[text()="Вклад"]')
    action(button)

    def print_tag(element):
        print(element.tag_name)

    select = get_element('//*[@class="namespaceselector"]')
    action(select, 'Обусждение')







    print()



