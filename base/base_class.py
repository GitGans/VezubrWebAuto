import datetime
import time
import random
import re
import allure
from typing import Any, ClassVar, Dict, Type, NoReturn, Optional
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

"""Variable"""
chrome_driver_path = 'C:\\Users\\Gans\\PycharmProjects\\VezubrAutomationProject\\resource\\chromedriver.exe'


class Base:
    """
    Базовый класс содержащий методы для взаимодействия с веб-драйвером.
    """
    driver: WebDriver
    loading_form: ClassVar[Dict[str, str]]
    loading_list: ClassVar[Dict[str, str]]

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр класса с драйвером.

        Parameters
        ----------
        driver : WebDriver
            Драйвер для управления браузером.
        """
        self.driver = driver

    """ Main locators"""
    loading_form = {
        "xpath": "(//div[@id='loader'])[2]",
        "name": "loading_form"
    }
    loading_list = {
        "xpath": "//span[@class='ant-spin-dot ant-spin-dot-spin']",
        "name": "loading_list"
    }

    """Single methods with Allure"""
    """ Get driver"""

    @classmethod
    def get_driver(cls: Type['Base']) -> 'Base':
        """
        Создает и возвращает экземпляр драйвера и класса.

        Returns
        -------
        Base
            Экземпляр класса Base с инициализированным веб-драйвером.
        """
        with allure.step(title="Start test"):
            options = webdriver.ChromeOptions()
            service = Service(chrome_driver_path)
            driver = webdriver.Chrome(options=options, service=service)
            print("Start test")
            return cls(driver)

    """Headless - Включение режима без графического интерфейса"""
    # @classmethod
    # def get_driver(cls):
    # """
    # Создает и возвращает экземпляр класса с драйвером Chrome, работающим в фоновом режиме.
    #
    # Этот метод инициализирует веб-драйвер Chrome с опцией "--headless",
    # что позволяет выполнять тесты без открытия браузера.
    #
    # Returns
    # -------
    # Base
    #     Экземпляр класса Base с инициализированным веб-драйвером Chrome, работающим в фоновом режиме.
    # """
    #     with allure.step(title="Start test"):
    #         chrome_options = Options()
    #         chrome_options.add_argument("--headless")
    #         service = Service(chrome_driver_path)
    #         driver = webdriver.Chrome(service=service, options=chrome_options)
    #
    #         print("Start test")
    #         return cls(driver)

    """ Finish test"""

    def finish_test(self) -> None:
        """
        Завершает тест и закрывает браузер.
        """
        with allure.step(title="Finish test"):
            print("Finish test")
            self.driver.quit()

    """ Get current url"""

    def get_current_url(self) -> None:
        """
        Получает и выводит текущий URL адрес в консоль.
        """
        get_url = self.driver.current_url
        with allure.step(title="Current url: " + get_url):
            print("Current url: " + get_url)

    """ Get element wait clickable"""

    def get_element_clickable(self, element_info: Dict[str, str]) -> Dict[str, Any]:
        """
        Ожидает, пока элемент не станет кликабельным, и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, element_info['xpath'])))}

    """ Get element wait visibility"""

    def get_element_visibility(self, element_info: Dict[str, str]) -> Dict[str, Any]:
        """
        Ожидает видимости элемента и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, element_info['xpath'])))}

    """ Get element wait located"""

    def get_element_located(self, element_info: Dict[str, str]) -> Dict[str, Any]:
        """
        Ожидает нахождения элемента в DOM и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, element_info['xpath'])))}

    """ Get element find"""

    def get_element_find(self, element_info: Dict[str, str]) -> Dict[str, Any]:
        """
        Находит элемент по заданному локатору и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        return {'name': element_info['name'], 'element': self.driver.find_element(By.XPATH, element_info['xpath'])}

    """ Wait element invisibility"""

    def wait_element_invisibility(self, element_info: Dict[str, str]) -> NoReturn:
        """
        Ожидает, пока элемент не станет невидимым на странице.

        Этот метод используется для ожидания, когда элемент, идентифицированный по заданному XPath, перестанет быть
        видимым на странице. Метод ожидает до 60 секунд, прежде чем прервать ожидание, если элемент остается видимым.

        Parameters
        ----------
        element_info : dict
            Словарь, содержащий информацию о локаторе элемента, включая его 'xpath'.
        """
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, element_info['xpath'])))
        return

    """ Get timestamp"""

    @staticmethod
    def get_timestamp() -> str:
        """
        Возвращает текущее время в формате UTC без разделителей.

        Returns
        -------
        str
            Текущее время в формате "ГГГГММДДЧЧММСС".
        """
        return datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def get_timestamp_eight_signs() -> str:
        """
        Возвращает текущее время в формате UTC без разделителей.

        Returns
        -------
        str
            Текущее время в формате "ДДЧЧММСС".
        """
        return datetime.datetime.utcnow().strftime("%d%H%M%S")

    """ Get timestamp with dot"""

    @staticmethod
    def get_timestamp_dot() -> str:
        """
        Возвращает текущее время в формате UTC с точками в качестве разделителей.

        Returns
        -------
        str
            Текущее время в формате "ГГГГ.ММ.ДД.ЧЧ.ММ.СС".
        """
        return datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")

    """ Assert word wait clickable"""

    def assert_word(self, element_dict: Dict[str, str]) -> NoReturn:
        """
        Проверяет, что текст элемента соответствует заданному значению.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о локаторе элемента и ожидаемым текстом.

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        value_word = (WebDriverWait(self.driver, 60).
                      until(EC.element_to_be_clickable((By.XPATH, element_dict['reference_xpath']))).text)
        with allure.step(title=f"Assert \"{value_word}\" == \"{element_dict['reference']}\""):
            assert re.fullmatch(element_dict['reference'], value_word)
            print(f"Assert \"{value_word}\" == \"{element_dict['reference']}\"")

    """ Assert word input reference wait clickable"""

    def flexible_assert_word(self, element_dict: Dict[str, str], reference_value: str) -> NoReturn:
        """
        Проверяет, что текст элемента соответствует заданному значению.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о локаторе элемента.
        reference_value : str
            Ожидаемый текст для проверки соответствия тексту элемента.

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        value_word = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, element_dict['reference_xpath']))
        ).text
        with allure.step(title=f"Assert \"{value_word}\" == \"{reference_value}\""):
            assert re.fullmatch(reference_value, value_word), f"Expected '{reference_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{reference_value}\"")

    """ Assert text extraction by INN wait clickable"""

    def verify_text_by_inn(self, inn_value: str, reference_value: str) -> NoReturn:
        """
        Проверяет наличие и соответствие конкретного текста для строки таблицы, содержащей заданный ИНН.

        Parameters
        ----------
        inn_value : str
            ИНН, используемый для поиска соответствующей строки в таблице.
        reference_value : str
            Ожидаемый текст для сравнения, который должен точно совпадать с текстом элемента.

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        locator = (By.XPATH, f"//tr[.//a[contains(text(), '{inn_value}')]]//div[contains(text(), '{reference_value}')]")
        element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        value_word = element.text
        with allure.step(title=f"Assert \"{value_word}\" == \"{reference_value}\""):
            assert value_word == reference_value, f"Expected '{reference_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{reference_value}\"")

    """ Get random value float str"""

    @staticmethod
    def random_value_float_str(of: float, to: float) -> str:
        """
        Возвращает случайное вещественное число в виде строки с одним знаком после запятой.

        Parameters
        ----------
        of : float
            Нижняя граница диапазона.
        to : float
            Верхняя граница диапазона.

        Returns
        -------
        str
            Строковое представление случайного вещественного числа.
        """
        return f'{random.uniform(of, to):.1f}'

    """ Get random value int str"""

    @staticmethod
    def random_value_int_str(of: int, to: int) -> str:
        """
        Возвращает случайное целое число в виде строки.

        Parameters
        ----------
        of : int
            Нижняя граница диапазона.
        to : int
            Верхняя граница диапазона.

        Returns
        -------
        str
            Строковое представление случайного целого числа.
        """
        return f'{random.randint(of, to)}'

    """ Get random value int """

    @staticmethod
    def random_value_int(of: int, to: int) -> int:
        """
        Возвращает случайное целое число из заданного диапазона.

        Parameters
        ----------
        of : int
            Нижняя граница диапазона.
        to : int
            Верхняя граница диапазона.

        Returns
        -------
        int
            Случайное целое число.
        """
        return random.randint(of, to)

    """ Get random value custom start int """

    @staticmethod
    def random_value_custom_start(prefix: str, n: int) -> str:
        """
        Генерирует случайное число с заданным префиксом и общей длиной.

        Parameters
        ----------
        prefix : str
            Префикс числа.
        n : int
            Общая длина результата, включая префикс.

        Returns
        -------
        str
            Строка, представляющая собой случайное число с заданным префиксом.
        """
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(n - len(prefix))])
        return f'{prefix}{random_digits}'

    """ Get screenshot"""

    def get_screenshot(self) -> NoReturn:
        """
        Сохраняет скриншот текущего состояния браузера.

        Файл скриншота будет сохранен в специфичном для проекта каталоге с именем, включающим текущую дату и время.
        """
        name_screenshot = f'{self.get_timestamp_dot()}.png'
        self.driver.save_screenshot(
            'C:\\Users\\Gans\\PycharmProjects\\VezubrAutomationProject\\screens\\{0}'.format(name_screenshot))
        with allure.step(title="Screen taken:" + name_screenshot):
            print("Screen taken:" + name_screenshot)

    """ Assert url"""

    def assert_url(self, result: str) -> NoReturn:
        """
        Проверяет, соответствует ли текущий URL заданному значению.

        Parameters
        ----------
        result : str
            Ожидаемое значение URL.

        Raises
        ------
        AssertionError
            Если текущий URL не соответствует ожидаемому значению.
        """
        get_url = self.driver.current_url
        with allure.step(title="Assert url true"):
            assert get_url == result
            print("Assert url true")

    """ Click button wait clickable"""

    def click_button(self, element_dict: Dict[str, str], do_assert: Optional[bool] = False,
                     wait: Optional[str] = None) -> NoReturn:
        """
        Кликает по кнопке, ожидая ее кликабельности.
        После клика может выполнить проверку текста и ожидание исчезновения элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        with allure.step(title=f"Click {element_dict['name']}"):
            button_dict = self.get_element_clickable(element_dict)
            button_dict['element'].click()
            print(f"Click {button_dict['name']}")
            if do_assert:
                time.sleep(0.1)
                self.assert_word(element_dict)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)

    """ Click button index wait clickable"""

    def click_button_index(self, element_dict: Dict[str, str], index: int = 1, do_assert: bool = False,
                           wait: Optional[str] = None) -> NoReturn:
        """
        Кликает по кнопке с указанным индексом, ожидая ее кликабельности.
        Позволяет кликнуть по одному из множества однотипных элементов.

        Parameters
        ----------
        element_dict : dict
            Словарь с базовой информацией о элементах для клика.
        index : int, optional
            Индекс элемента, по которому будет выполнен клик.
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        with allure.step(title=f"Click {element_dict['name']}"):
            locator = f"({element_dict['xpath']})[{index}]"
            updated_element_dict = {
                "name": f"{element_dict['name']} index {index}",
                "xpath": locator
            }
            button_dict = self.get_element_clickable(updated_element_dict)
            button_dict['element'].click()
            print(f"Click {button_dict['name']}")
            if do_assert:
                self.assert_word(element_dict)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)

    """ Click button wait visibility"""

    def click_button_visibility(self, element_dict: Dict[str, str], do_assert: bool = False,
                                wait: Optional[str] = None) -> NoReturn:
        """
        Кликает по кнопке, ожидая ее видимости.
        После клика может выполнить проверку текста и ожидание исчезновения элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        with allure.step(title=f"Click {element_dict['name']}"):
            button_dict = self.get_element_visibility(element_dict)
            button_dict['element'].click()
            print(f"Click {button_dict['name']}")
            if do_assert:
                self.assert_word(element_dict)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)

    """ Click button wait located"""

    def click_button_located(self, element_dict: Dict[str, str], do_assert: bool = False,
                             wait: Optional[str] = None) -> NoReturn:
        """
        Кликает по кнопке, ожидая ее нахождения в DOM.
        После клика может выполнить проверку текста и ожидание исчезновения элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        with allure.step(title=f"Click {element_dict['name']}"):
            button_dict = self.get_element_located(element_dict)
            button_dict['element'].click()
            print(f"Click {button_dict['name']}")
            if do_assert:
                self.assert_word(element_dict)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)

    """ Click button find"""

    def click_button_find(self, element_dict: Dict[str, str], do_assert: bool = False,
                          wait: Optional[str] = None) -> NoReturn:
        """
        Находит и кликает по кнопке без предварительного ожидания состояний.
        После клика может выполнить проверку текста и ожидание исчезновения элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        with allure.step(title=f"Click {element_dict['name']}"):
            button_dict = self.get_element_find(element_dict)
            button_dict['element'].click()
            print(f"Click {button_dict['name']}")
            if do_assert:
                self.assert_word(element_dict)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)

    """ In dropdown click clickable, input enter find"""

    def dropdown_click_input_enter(self, element_dict: Dict[str, str], option_text: str,
                                   press_enter: bool = True) -> None:
        """
        Выбирает текст в выпадающем списке с помощью клика по элементу, ввода текста и нажатия Enter.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для выбора.
        press_enter : bool, optional
            Если True, после ввода текста будет выполнено нажатие Enter.

        """
        with allure.step(title=f"Select '{option_text}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            option_to_select = dropdown_dict['element'].find_element(By.XPATH, "./../..//input")
            option_to_select.send_keys(option_text)
            if press_enter:
                option_to_select.send_keys(Keys.ENTER)
            print(f"Selected '{option_text}' from dropdown {dropdown_dict['name']}")

    """In dropdown click clickable, input find, wait located, enter find"""

    def dropdown_click_input_wait_enter(self, element_dict: Dict[str, str], option_text: str,
                                        press_enter: bool = True) -> None:
        """
        Выбирает текст в выпадающем списке, ожидая появления опции после ввода текста, и нажимает Enter.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для выбора.
        press_enter : bool, optional
            Если True, после появления текста будет выполнено нажатие Enter.

        """
        with allure.step(title=f"Select '{option_text}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            option_to_select = dropdown_dict['element'].find_element(By.XPATH, "./../..//input")
            option_to_select.send_keys(option_text)
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, f".//li[@role='option' and normalize-space(.)='{option_text}']")
                )
            )
            if press_enter:
                option_to_select.send_keys(Keys.ENTER)
            print(f"Selected '{option_text}' from dropdown {dropdown_dict['name']}")

    """In dropdown click clickable, input enter located"""

    def dropdown_click_input_enter_located(self, element_dict: Dict[str, str], option_text: str,
                                           press_enter: bool = True) -> None:
        """
        Выбирает текст в выпадающем списке с помощью клика, ввода текста и нажатия Enter, ожидая расположения опции.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для выбора.
        press_enter : bool, optional
            Если True, после ввода текста будет выполнено нажатие Enter.

        """
        with allure.step(title=f"Select '{option_text}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            option_to_select = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
                (By.XPATH, f".//li[@role='option' and normalize-space(.)='{option_text}']")))
            option_to_select.send_keys(option_text)
            if press_enter:
                option_to_select.send_keys(Keys.ENTER)
            print(f"Selected '{option_text}' from dropdown {dropdown_dict['name']}")

    """In dropdown click input + index click clickable"""

    def dropdown_click_input_click(self, element_dict: Dict[str, str], option_text: str, index: int = 1) -> None:
        """
        Выбирает опцию в выпадающем списке с помощью поиска и клика по найденному элементу.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для поиска и выбора.
        index : int
            Индекс опции в списке, начиная с 1, который нужно выбрать.

        """
        step_title = f"Select '{option_text}' from dropdown {element_dict['name']}"
        print_message = f"Selected '{option_text}' from dropdown {element_dict['name']}"
        if index != 1:
            step_title += f" at index {index}"
            print_message += f" at index {index}"

        with allure.step(title=step_title):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            xpath_expression = f"(.//li[@role='option' and normalize-space(text())='{option_text}'])[{index}]"
            option_to_select = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath_expression)))
            option_to_select.click()
            print(print_message)

    """ In dropdown click clickable, input click located"""

    def dropdown_click_input_click_located(self, element_dict: Dict[str, str], option_text: str) -> None:
        """
        Выбирает опцию в выпадающем списке, ожидая расположения элемента поиска и кликая по нему.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для поиска и выбора.

        """
        with allure.step(title=f"Select '{option_text}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            option_to_select = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, f".//li[@role='option' and normalize-space(.)='{option_text}']")))
            option_to_select.click()
            print(f"Selected '{option_text}' from dropdown {dropdown_dict['name']}")

    """ In dropdown select index clickable"""

    def dropdown_click_index_click(self, element_dict: Dict[str, str], index: int) -> None:
        """
        Выбирает опцию в выпадающем списке по индексу с помощью клика по элементу и клика по опции с заданным индексом.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        index : int
            Индекс опции для выбора.

        """
        with allure.step(title=f"Select by index '{index}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element_clickable(element_dict)
            dropdown_dict['element'].click()
            option_xpath = (f"(//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'])"
                            f"[{index}]")
            option_to_select = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, option_xpath)))
            option_to_select.click()
            print(f"Selected by index '{index}' from dropdown {dropdown_dict['name']}")

    """ Move to element wait clickable"""

    def move_to_element(self, element_dict: Dict[str, str]) -> None:
        """
        Перемещает курсор мыши к элементу, ожидая его кликабельности.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе, к которому необходимо переместить курсор.

        """
        with allure.step(title=f"Move to {element_dict['name']}"):
            button_dict = self.get_element_clickable(element_dict)
            ActionChains(self.driver).move_to_element(button_dict['element']).perform()
            print(f"Move to {button_dict['name']}")

    """ Move to element find"""

    def move_to_element_find(self, element_dict: Dict[str, str]) -> None:
        """
        Перемещает курсор мыши к элементу без предварительного ожидания его состояний.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе, к которому необходимо переместить курсор.

        """
        with allure.step(title=f"Move to {element_dict['name']}"):
            button_dict = self.get_element_find(element_dict)
            ActionChains(self.driver).move_to_element(button_dict['element']).perform()
            print(f"Move to {button_dict['name']}")

    """ Switch to original window"""

    def switch_to_original_window(self) -> None:
        """
        Переключается обратно к оригинальному окну браузера.

        """
        with allure.step(title="Returned to the original window"):
            original_window_handle = self.driver.current_window_handle
            self.driver.switch_to.window(original_window_handle)
            print("Returned to the original window")

    """ Input field wait clickable"""

    def input_in_field(self, element_dict: Dict[str, str], value: str, wait: Optional[str] = None,
                       safe: bool = False) -> None:
        """
        Вводит текст в поле ввода, ожидая его кликабельности. Может ожидать исчезновение элементов загрузки после ввода.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после ввода.
        safe : bool, optional
            Если True, заменяет введенное значение на символы "***" в логах.

        """
        with allure.step(title=f"In {element_dict['name']}: " + ("***" if safe else str(value))):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].send_keys(value)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)
            print(f"In {field_dict['name']}: " + ("***" if safe else str(value)))

    """ Input field find"""

    def input_in_field_find(self, element_dict: Dict[str, str], value: str) -> None:
        """
        Вводит текст в поле ввода без предварительного ожидания его состояний.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.

        """
        with allure.step(title=f"In {element_dict['name']}: {value}"):
            field_dict = self.get_element_find(element_dict)
            field_dict['element'].send_keys(value)
            print(f"In {field_dict['name']}: {value}")

    """ Clear field wait clickable"""

    def clear_field(self, element_dict: Dict[str, str]) -> None:
        """
        Очищает поле ввода, ожидая его кликабельности.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода, которое необходимо очистить.

        """
        with allure.step(title=f"Clear {element_dict['name']}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].clear()
            print(f"Clear {field_dict['name']}")

    """ Input field and enter wait clickable"""

    def input_in_field_and_enter(self, element_dict: Dict[str, str], value: str, wait: Optional[str] = None) -> None:
        """
        Вводит текст в поле ввода, ожидая его кликабельности, и нажимает Enter.
        Может ожидать исчезновение элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после ввода.

        """
        with allure.step(f"In {element_dict['name']}: {value} - and pressed enter"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].send_keys(value)
            field_dict['element'].send_keys(Keys.RETURN)
            if wait == 'lst':
                self.wait_element_invisibility(self.loading_list)
            elif wait == 'form':
                self.wait_element_invisibility(self.loading_form)
            print(f"In {field_dict['name']}: {value} - and pressed enter")

    """ Enter and input field wait clickable"""

    def enter_and_input_in_field(self, element_dict: Dict[str, str], value: str) -> None:
        """
        Сначала нажимает Enter, а затем вводит текст в поле ввода, ожидая его кликабельности.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.

        """
        with allure.step(f"Enter pressed in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].send_keys(Keys.RETURN)
            field_dict['element'].send_keys(value)
            print(f"Enter pressed in {field_dict['name']}: {value}")

    """ Click and input field wait clickable"""

    def click_and_input_in_field(self, element_dict: Dict[str, str], value: str) -> None:
        """
        Кликает по полю ввода, ожидая его кликабельности, и вводит текст.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.

        """
        with allure.step(f"Click and in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].click()
            field_dict['element'].send_keys(value)
            print(f"Click and in {field_dict['name']}: {value}")

    """ Click and enter wait clickable"""

    def click_and_enter(self, element_dict: Dict[str, str]) -> None:
        """
        Кликает по полю ввода, ожидая его кликабельности, и нажимает Enter.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.

        """
        with allure.step(f"Click {element_dict['name']} and pressed enter"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].click()
            field_dict['element'].send_keys(Keys.ENTER)
            print(f"Click {field_dict['name']} and pressed enter")

    """ Click input and enter wait clickable"""

    def click_input_and_enter(self, element_dict: Dict[str, str], value: str) -> None:
        """
        Кликает по полю ввода, ожидая его кликабельности, вводит текст и нажимает Enter.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.

        """
        with allure.step(f"Click {element_dict['name']} and pressed enter"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].click()
            field_dict['element'].send_keys(value)
            field_dict['element'].send_keys(Keys.ENTER)
            print(f"Click {field_dict['name']} input: {value} and pressed enter")

    """ Backspace len and input wait clickable"""

    def backspace_len_and_input(self, element_dict: Dict[str, str], value: str,
                                press_enter: Optional[bool] = False) -> None:
        """
        Выполняет нажатие клавиши Backspace для удаления символов,
        соответствующих длине вводимого значения, и вводит текст.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        with allure.step(title=f"Backspace and input in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].send_keys(Keys.BACKSPACE * len(value))
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"Backspace and in {field_dict['name']}: {value}")

    """ Backspace len and input wait clickable"""

    def backspace_all_and_input(self, element_dict: Dict[str, str], value: str,
                                press_enter: Optional[bool] = False) -> None:
        """
        Очищает поле ввода путем нажатий клавиши Backspace для каждого символа в поле,
        затем вводит новое значение.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        with allure.step(title=f"Backspace and input in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].click()
            current_value = field_dict['element'].get_attribute('value')
            for _ in range(len(current_value)):
                field_dict['element'].send_keys(Keys.BACKSPACE)
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"Backspaced and input in {field_dict['name']}: {value}")

    """ Click backspace and input wait clickable"""

    def click_backspace_and_input(self, element_dict: Dict[str, str], value: str) -> None:
        """
        Кликает по полю ввода, выполняет нажатие клавиши Backspace для удаления символов и вводит текст.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.

        """
        with allure.step(title=f"Click backspace and input in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_element = field_dict['element']
            field_element.click()
            field_element.send_keys(Keys.BACKSPACE * len(value))
            field_element.send_keys(value)
            print(f"Click backspace and in {field_dict['name']}: {value}")

    """ Backspace num times and input wait clickable"""

    def backspace_num_and_input(self, element_dict: Dict[str, str], num: int, value: str,
                                press_enter: Optional[bool] = False) -> None:
        """
        Выполняет нажатие клавиши Backspace заданное количество раз и вводит текст.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        num : int
            Количество раз для нажатия клавиши Backspace.
        value : str
            Значение для ввода.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        with allure.step(title=f"Backspace {num} times and input in {element_dict['name']}: {value}"):
            field_dict = self.get_element_clickable(element_dict)
            field_dict['element'].send_keys(Keys.BACKSPACE * num)
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"Backspaced {num} times and input in {field_dict['name']}: {value}")

    """ Scroll X Y"""

    def scroll_page(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """
        Прокручивает страницу на заданное количество пикселей по горизонтали и вертикали.

        Parameters
        ----------
        x : int, optional
            Количество пикселей для прокрутки по горизонтали.
        y : int, optional
            Количество пикселей для прокрутки по вертикали.

        """
        with allure.step(title=f"Scroll page X by {x} pixels and Y by {y} pixels"):
            script = "window.scrollBy({}, {});".format(x, y) if x is not None and y is not None else ""
            self.driver.execute_script(script)
            if x is not None or y is not None:
                print(f"Scroll page", end="")
                if x is not None:
                    print(f" X {x} pixels", end="")
                if y is not None:
                    print(f" Y by {y} pixels", end="")
                print()

    """Combined methods"""
    """ Move and click button clickable"""

    def move_and_click(self, move_to: Dict[str, str], click_to: Dict[str, str], do_assert: bool = False,
                       wait: Optional[str] = None) -> None:
        """
        Перемещается к элементу и кликает по другому элементу.

        Parameters
        ----------
        move_to : dict
            Словарь с информацией о элементе для перемещения к нему.
        click_to : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполняет дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки.

        """
        self.move_to_element(move_to)
        time.sleep(0.2)
        self.click_button(click_to, do_assert=do_assert, wait=wait)

    """ Move find and click button wait clickable"""

    def move_find_and_click(self, move_to: Dict[str, str], click_to: Dict[str, str], do_assert: bool = False,
                            wait: Optional[str] = None) -> None:
        """
        Перемещается к элементу, найденному без ожидания, и кликает по другому элементу.

        Parameters
        ----------
        move_to : dict
            Словарь с информацией о элементе для перемещения.
        click_to : dict
            Словарь с информацией о элементе для клика.
        do_assert : bool, optional
            Если True, выполняет дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки.

        """
        self.move_to_element_find(move_to)
        time.sleep(0.2)
        self.click_button(click_to, do_assert=do_assert, wait=wait)

    """ Naw time change"""

    @staticmethod
    def naw_time_change(minutes: int) -> str:
        """
        Изменяет текущее время, добавляя указанное количество минут и округляет результат.

        Parameters
        ----------
        minutes : int
            Количество минут для добавления к текущему времени.

        Returns
        -------
        str
            Строка с новым временем в формате HHMM, округленным до ближайших 5 минут.

        """
        original_time = datetime.datetime.now()
        new_time = original_time + datetime.timedelta(minutes=minutes)
        new_time_str = new_time.strftime("%H%M")
        rounded_time_str = str(int(round(int(new_time_str) / 5) * 5)).zfill(4)
        return rounded_time_str

    """ Naw datatime change"""

    @staticmethod
    def naw_datatime_change(minutes: int) -> str:
        """
        Изменяет текущую дату и время, добавляя указанное количество минут и округляет результат.

        Parameters
        ----------
        minutes : int
            Количество минут для добавления к текущей дате и времени.

        Returns
        -------
        str
            Строка с новой датой и временем в формате DDMMYYYY HHMM, округленным до ближайших 5 минут.

        """
        original_time = datetime.datetime.now()
        new_time = original_time + datetime.timedelta(minutes=minutes)
        new_time_str = new_time.strftime("%d%m%Y %H%M")
        rounded_time_str = str(int(round(int(new_time_str) / 5) * 5)).zfill(4)
        return rounded_time_str

    """ Get sms code"""

    def get_confirmation_code(self, phone_number):
        """
        Извлекает код подтверждения, связанный с заданным номером телефона.

        Parameters
        ----------
        phone_number : str
            Номер телефона в формате 10 цифр без префикса.

        Returns
        -------
        str
            Код подтверждения как строку, если найден.

        Raises
        ------
        ValueError
            Если код подтверждения не найден.
        """
        formatted_phone = '+7' + phone_number
        xpath_locator = f"//tr[contains(.//div, '{formatted_phone}')]//div[contains(text(), 'Код подтверждения:')]"
        try:
            element_text = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, xpath_locator))
            ).text
        except TimeoutException:
            raise ValueError(f"Код подтверждения для номера {formatted_phone} не найден.")

        match = re.search(r'\d+', element_text)
        if match:
            return match.group(0)
        else:
            raise ValueError(f"Не удалось извлечь код подтверждения из текста: {element_text}")

    """ Generate inn"""

    @staticmethod
    def generate_inn(entity_type: str) -> str:
        """
        Генерирует ИНН для физического лица (individual) или юридического лица (entity).

        Parameters
        ----------
        entity_type : str
            Тип сущности, для которой генерируется ИНН. Допустимые значения: 'individual', 'entity'.

        Returns
        -------
        str
            Сгенерированный ИНН в виде строки.
            Для юридического лица ИНН состоит из 10 цифр, для физического лица - из 12 цифр.

        Raises
        ------
        ValueError
            Если передан неизвестный тип сущности. Допустимые значения параметра entity_type: 'individual', 'entity'.
        """

        def calculate_control_sum(numbers: list[int], local_coeffs: list[int]) -> int:
            return sum(a * b for a, b in zip(numbers, local_coeffs)) % 11 % 10

        if entity_type == "entity":
            base = [random.randint(0, 9) for _ in range(9)]
            entity_coeffs = [2, 4, 10, 3, 5, 9, 4, 6, 8]
            control_sum = calculate_control_sum(base, entity_coeffs)
            inn = ''.join(map(str, base)) + str(control_sum)
        elif entity_type == "individual":
            base = [random.randint(0, 9) for _ in range(10)]
            individual_coeffs_first = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
            individual_coeffs_second = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 5]
            first_control_sum = calculate_control_sum(base, individual_coeffs_first)
            second_control_sum = calculate_control_sum(base + [first_control_sum], individual_coeffs_second)
            inn = ''.join(map(str, base)) + str(first_control_sum) + str(second_control_sum)
        else:
            raise ValueError("Неизвестный тип сущности. Допустимые значения: 'individual', 'entity'.")

        return inn
