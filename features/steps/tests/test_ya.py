from features.steps.pages.ya_page import MainYaPage


def test_ya():
    page = MainYaPage()

    page.driver.get('https://yandex.ru')
    page.click(xpath=page.INPUT_SEARCH)
    page.fill_input(xpath=page.INPUT_SEARCH, value='Как открыть тапком банку шпрот?')
    page.click(xpath=page.BUTTON_SEARCH)
    page.click(xpath=page.INPUT_SEARCH_WithText)
    page.clear_input(xpath=page.INPUT_SEARCH_WithText)
    page.fill_input(xpath=page.INPUT_SEARCH_WithText, value='Как найти правильный XPath для этой долбанной картинки?')
    page.click(xpath=page.BUTTON_SEARCH_WithText)
    page.click(xpath=page.PIC_BUTTON)
    page.privet_kak_dela(page.get_element(xpath=page.IMG_ON_IMAGE_PAGE))

    print()
    page.quit_browser()
