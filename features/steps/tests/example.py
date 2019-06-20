from pages.base_page import BasePage


class CommonBulleteins(BasePage):
    """Общий класс
    """
    BUTTON_OK = '//*[text()="ОК"]'


class TwoNDFL(CommonBulleteins):
    """Справка 2 НДФЛ
    """


class Experience(CommonBulleteins):
    """Справка стаж работы
    """

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys(value)


class Experience2(CommonBulleteins):
    """Справка стаж работы
    """
    BUTTON_OK = '//*[text()="ок"]'


class Experience3(CommonBulleteins):
    """Справка стаж работы
    """



class Experience4(CommonBulleteins):
    """Справка стаж работы
    """


class Experience5(CommonBulleteins):
    """Справка стаж работы
    """
