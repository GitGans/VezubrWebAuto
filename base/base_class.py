import datetime
import time
import random
import re
import allure
import os
import platform
from typing import Any, ClassVar, Dict, Type, NoReturn, Optional
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""Variable"""
# Определение пути к драйверам
WINDOWS_DRIVER_PATH = os.path.join('resource', 'windows', 'chromedriver.exe')
LINUX_DRIVER_PATH = '/app/resource/linux/chromedriver'


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
        options = webdriver.ChromeOptions()
        
        if platform.system() == 'Windows':
            # Настройки для Windows
            chrome_driver_path = WINDOWS_DRIVER_PATH
            options.add_argument('--window-size=1920x1080')  # Устанавливает размер окна браузера
        else:
            # Настройки для Linux (например, в контейнерах)
            chrome_driver_path = LINUX_DRIVER_PATH
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            # options.add_argument('--headless')  # Режим без графического интерфейса
        
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(options=options, service=service)
        
        with allure.step(title="Start test"):
            print("Start test")
        
        return cls(driver)

    """Test finish"""
    def test_finish(self) -> None:
        """
        Завершает тест и закрывает браузер.
        """
        with allure.step(title="Test finish"):
            print("Test finish")
            self.driver.quit()

    """ Get current url"""
    def get_current_url(self) -> None:
        """
        Получает и выводит текущий URL адрес в консоль.
        """
        get_url = self.driver.current_url
        with allure.step(title="Current url: " + get_url):
            print("Current url: " + get_url)

    """ Get element with choosing a method for obtaining an element"""
    def get_element(self, element_info: Dict[str, str], wait_type: str = 'clickable') -> Dict[str, Any]:
        """
        Ожидает элемент в зависимости от выбранного типа ожидания и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.
        wait_type : str, optional
            Тип ожидания: 'clickable', 'visible', 'located', 'find', или 'invisibility'.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        if wait_type == 'clickable':
            return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, element_info['xpath'])))}
        elif wait_type == 'visible':
            return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, element_info['xpath'])))}
        elif wait_type == 'located':
            return {'name': element_info['name'], 'element': WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, element_info['xpath'])))}
        elif wait_type == 'find':
            return {'name': element_info['name'], 'element': self.driver.find_element(By.XPATH, element_info['xpath'])}
        elif wait_type == 'invisibility':
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, element_info['xpath'])))
            return {'name': element_info['name'], 'element': None}
        else:
            raise ValueError(f"Unsupported wait type: {wait_type}")

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

    """ Get timestamp eight signs"""
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
    
    """ Assert word fix reference"""
    def assert_word(self, element_dict: Dict[str, str], wait_type: str = 'clickable') -> NoReturn:
        """
        Проверяет, что текст элемента соответствует заданному значению. Если предоставлен 'reference_xpath',
        использует его для точного определения элемента для проверки текста.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о локаторе элемента и ожидаемым текстом.
            Может включать 'reference_xpath' для спецификации элемента, текст которого следует проверять.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find').

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        if 'reference_xpath' in element_dict:
            reference_element = self.get_element(
                {'name': 'Reference element', 'xpath': element_dict['reference_xpath']}, wait_type='located')['element']
            time.sleep(0.3)  # Фиксированная задержка
            value_word = reference_element.text
        else:
            element = self.get_element(element_dict, wait_type=wait_type)['element']
            time.sleep(0.3)  # Фиксированная задержка
            value_word = element.text
        
        with allure.step(title=f"Assert \"{value_word}\" == \"{element_dict['reference']}\""):
            assert re.fullmatch(element_dict['reference'],
                                value_word), f"Expected '{element_dict['reference']}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{element_dict['reference']}\"")
        
        """ Assert word input reference"""
    def flexible_assert_word(self, element_dict: Dict[str, str], reference_value: str,
                             wait_type: str = 'clickable') -> None:
        """
        Проверяет, что текст элемента или значение его атрибута 'value' соответствует заданному значению.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о локаторе элемента.
        reference_value : str
            Ожидаемый текст или значение для проверки соответствия тексту элемента или его атрибуту 'value'.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find').

        Raises
        ------
        AssertionError
            Если текст элемента или его атрибут 'value' не соответствует ожидаемому значению.
        """
        element = self.get_element(element_dict, wait_type=wait_type)['element']
        time.sleep(0.3)  # Фиксированная задержка
        actual_text = element.text or element.get_attribute('value')  # Получаем текст или значение атрибута 'value'
        with allure.step(title=f"Assert \"{actual_text}\" == \"{reference_value}\""):
            assert re.fullmatch(reference_value,
                                actual_text), f"Expected '{reference_value}', but found '{actual_text}'."
            print(f"Assert \"{actual_text}\" == \"{reference_value}\"")
    
    """ Assert text extraction by INN wait clickable"""
    def verify_text_by_inn(self, inn_value: str, reference_value: str, wait_type: str = 'located') -> NoReturn:
        """
        Проверяет наличие и соответствие конкретного текста для строки таблицы, содержащей заданный ИНН,
        с выбором типа ожидания элемента.

        Parameters
        ----------
        inn_value : str
            ИНН, используемый для поиска соответствующей строки в таблице.
        reference_value : str
            Ожидаемый текст для сравнения, который должен точно совпадать с текстом элемента.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find').

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        element_info = {
            "name": f"Text for INN {inn_value} matching '{reference_value}'",
            "xpath": f"//tr[.//a[contains(text(), '{inn_value}')]]//div[contains(text(), '{reference_value}')]"
        }
        element = self.get_element(element_info, wait_type=wait_type)['element']
        time.sleep(0.3)  # Фиксированная задержка
        value_word = element.text
        with allure.step(title=f"Assert \"{value_word}\" == \"{reference_value}\""):
            assert value_word == reference_value, f"Expected '{reference_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{reference_value}\"")
    
    """ Get random value float to str"""
    @staticmethod
    def random_value_float_str(of: float, to: float, precision: int = 0) -> str:
        """
        Возвращает случайное вещественное число в виде строки с заданным количеством знаков после запятой.

        Parameters
        ----------
        of : float
            Нижняя граница диапазона.
        to : float
            Верхняя граница диапазона.
        precision : int, optional
            Количество знаков после запятой, по умолчанию 0.

        Returns
        -------
        str
            Строковое представление случайного вещественного числа с заданной точностью.
        """
        return f'{random.uniform(of, to):.{precision}f}'

    """ Get random value custom start int to str"""
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
    
    """ Click button"""
    def click_button(self, element_dict: Dict[str, str], index: int = 1, do_assert: Optional[bool] = False,
                     wait: Optional[str] = None, wait_type: str = 'clickable') -> NoReturn:
        """
        Кликает по кнопке с заданным типом ожидания и опционально по индексу элемента.
        Может выполнять дополнительную проверку текста элемента после клика (ассерт) и ожидание
        исчезновения элементов загрузки (списки или формы).

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о кнопке для клика.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).
        do_assert : bool, optional
            Если True, выполнит дополнительную проверку текста элемента после клика.
        wait : str, optional
            Определяет, какой спиннер ожидать после клика ('lst' для списка или 'form' для формы).
        wait_type : str, optional
            Тип ожидания элемента перед кликом ('clickable', 'visible', 'located', 'find'), по умолчанию 'clickable'.

        """
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_name, "xpath": locator}
        
        with allure.step(title=f"Click on {element_name}"):
            button_dict = self.get_element(updated_element_dict, wait_type)
            button_dict['element'].click()
            print(f"Click on {button_dict['name']}")
            if do_assert:
                self.assert_word(element_dict)
            if wait:
                # Определяем, какой спиннер ожидать
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                self.get_element(loading_spinner, wait_type="visible")  # Ожидание появления соответствующего спиннера
                self.get_element(loading_spinner, wait_type="invisibility")  # Ожидание исчезновения спиннера
    
    """ In dropdown click, wait, input and enter"""
    def dropdown_click_input_wait_enter(self, element_dict: Dict[str, str], option_text: str, press_enter: bool = True,
                                        wait_presence: bool = False, wait_type: str = 'clickable') -> None:
        """
        Выбирает текст в выпадающем списке, вводит текст и, опционально, ожидает появления опции,
        после чего может нажимать Enter. Позволяет выбор типа ожидания для элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для выбора.
        press_enter : bool, optional
            Если True, после ввода текста будет выполнено нажатие Enter.
        wait_presence : bool, optional
            Если True, ожидает появления текста перед нажатием Enter.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find'), по умолчанию 'clickable'.

        """
        with allure.step(title=f"Select '{option_text}' from dropdown {element_dict['name']}"):
            dropdown_dict = self.get_element(element_dict, wait_type=wait_type)
            dropdown_dict['element'].click()
            option_to_select = dropdown_dict['element'].find_element(By.XPATH, "./../..//input")
            option_to_select.send_keys(option_text)
            if wait_presence:
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f".//li[@role='option' and contains(normalize-space(.), '{option_text}')]")
                    )
                )
            if press_enter:
                option_to_select.send_keys(Keys.ENTER)
            print(f"Selected '{option_text}' from dropdown {dropdown_dict['name']}")

    """In dropdown click input + index click"""
    def dropdown_click_input_click(self, element_dict: Dict[str, str], option_text: str, dd_index: int = 1,
                                   index: int = 1) -> None:
        """
        Выбирает опцию в выпадающем списке с помощью поиска и клика по найденному элементу.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе выпадающего списка.
        option_text : str
            Текст опции для поиска и выбора.
        dd_index : int
            Индекс выпадающего списка для инициации клика, начиная с 1.
        index : int
            Индекс опции в списке, начиная с 1, который нужно выбрать.

        """
        step_title = f"Select '{option_text}' from dropdown {element_dict['name']}"
        print_message = f"Selected '{option_text}' from dropdown {element_dict['name']}"
        
        if dd_index != 1:
            step_title += f" at dropdown index {dd_index}"
            print_message += f" at dropdown index {dd_index}"
        
        if index != 1:
            step_title += f" at option index {index}"
            print_message += f" at option index {index}"
        
        with allure.step(title=step_title):
            xpath_dropdown = f"({element_dict['xpath']})[{dd_index}]" if dd_index > 1 else element_dict['xpath']
            dropdown_dict = self.get_element({"name": element_dict['name'], "xpath": xpath_dropdown})
            dropdown_dict['element'].click()
            
            xpath_expression = f"(.//li[@role='option' and normalize-space(.)='{option_text}'])[{index}]"
            option_to_select = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath_expression)))
            option_to_select.click()
            
            print(print_message)
    
    """ Move to element"""
    def move_to_element(self, element_dict: Dict[str, str], index: int = 1, wait_type: str = 'clickable') -> None:
        """
        Перемещает курсор мыши к элементу с заданным типом ожидания и опционально по индексу элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о элементе, к которому необходимо переместить курсор.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).
        wait_type : str, optional
            Тип ожидания элемента для интеракции ('clickable', 'visible', 'located', 'find', 'invisibility').

        """
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_name, "xpath": locator}

        with allure.step(title=f"Move to {element_name}"):
            button_dict = self.get_element(updated_element_dict, wait_type)
            ActionChains(self.driver).move_to_element(button_dict['element']).perform()
            print(f"Moved to {button_dict['name']}")

    """ Switch to original window"""
    def switch_to_original_window(self) -> None:
        """
        Переключается обратно к оригинальному окну браузера.

        """
        with allure.step(title="Returned to the original window"):
            original_window_handle = self.driver.current_window_handle
            self.driver.switch_to.window(original_window_handle)
            print("Returned to the original window")
    
    """ Input in field with optional click, enter, index and wait loading"""
    def input_in_field(self, element_dict: Dict[str, str], value: str, click_first: bool = False,
                       press_enter: bool = False, wait: Optional[str] = None, safe: bool = False,
                       wait_type: str = 'clickable', index: int = 1) -> None:
        """
        Универсальный метод для ввода текста в поле с опциональным кликом перед вводом и нажатием Enter после.
        Поддерживает дополнительные параметры для управления взаимодействием, включая индекс элемента,
        ожидание прогрузки элементов (списки или формы), и выбор типа ожидания доступности элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода текста.
        wait : str, optional
            Указывает, нужно ли ожидать исчезновение элементов загрузки после ввода ('lst' или 'form').
        safe : bool, optional
            Если True, заменяет введенное значение на символы "***" в логах.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find'), по умолчанию 'clickable'.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).

        """
        log_value = "***" if safe else value
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_name, "xpath": locator}
        
        with allure.step(title=f"{('Click and ' if click_first else '')}Input in {element_name}: " + log_value):
            field_dict = self.get_element(updated_element_dict, wait_type)
            if click_first:
                field_dict['element'].click()
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"{('Click and ' if click_first else '')}Input in {field_dict['name']}: " + log_value)
            if wait:
                # Определяем, какой спиннер ожидать
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                self.get_element(loading_spinner, wait_type="visible")  # Ожидание появления соответствующего спиннера
                self.get_element(loading_spinner, wait_type="invisibility")  # Ожидание исчезновения спиннера
    
    """ Backspace len and input with optional click, enter"""
    def backspace_len_and_input(self, element_dict: Dict[str, str], value: str,
                                click_first: bool = False, press_enter: Optional[bool] = False) -> None:
        """
        Выполняет нажатие клавиши Backspace для удаления символов,
        соответствующих длине вводимого значения, и вводит текст.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        element_name = element_dict['name']
        with allure.step(title=f"{'Click and ' if click_first else ''}Backspace and input in {element_name}: {value}"):
            field_dict = self.get_element(element_dict)
            if click_first:
                field_dict['element'].click()
            field_dict['element'].send_keys(Keys.BACKSPACE * len(value))
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"{'Click and ' if click_first else ''}Backspace and input in {element_name}: {value}")
    
    """ Backspace all and input with optional click, enter"""
    def backspace_all_and_input(self, element_dict: Dict[str, str], value: str,
                                click_first: bool = False, press_enter: Optional[bool] = False) -> None:
        """
        Очищает поле ввода путем нажатий клавиши Backspace для каждого символа в поле,
        затем вводит новое значение.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        element_name = element_dict['name']
        with allure.step(title=f"{'Click and ' if click_first else ''}Backspace and input in {element_name}: {value}"):
            field_dict = self.get_element(element_dict)
            if click_first:
                field_dict['element'].click()
            current_value = field_dict['element'].get_attribute('value')
            for _ in range(len(current_value)):
                field_dict['element'].send_keys(Keys.BACKSPACE)
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"{'Click and ' if click_first else ''}Backspaced and input in {element_name}: {value}")
    
    """ Backspace num times and input with optional click, enter"""
    def backspace_num_and_input(self, element_dict: Dict[str, str], num: int, value: str,
                                click_first: bool = False, press_enter: Optional[bool] = False) -> None:
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
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.

        """
        element_name = element_dict['name']
        with allure.step(
                title=f"{'Click and ' if click_first else ''}Backspace {num} times and input in {element_name}: {value}"
        ):
            field_dict = self.get_element(element_dict)
            if click_first:
                field_dict['element'].click()
            field_dict['element'].send_keys(Keys.BACKSPACE * num)
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(f"{'Click and ' if click_first else ''}Backspaced {num} times and input in {element_name}: {value}")

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

    """ Move to and click button"""
    def move_and_click(self, move_to: Dict[str, str], click_to: Dict[str, str], move_index: int = 1,
                       click_index: int = 1, move_wait_type: str = 'clickable', click_wait_type: str = 'clickable',
                       do_assert: bool = False, wait: Optional[str] = None) -> None:
        """
        Перемещается к элементу с заданным типом ожидания и индексом,
        и кликает по другому элементу с выбором типа ожидания и индексом.
        После клика может выполнить дополнительную проверку текста элемента (ассерт)
        и ожидание исчезновения элементов загрузки (списки или формы).

        Parameters
        ----------
        move_to : dict
            Словарь с информацией о элементе для перемещения.
        click_to : dict
            Словарь с информацией о элементе для клика.
        move_index : int, optional
            Индекс элемента для перемещения. По умолчанию 1 (первый элемент).
        click_index : int, optional
            Индекс элемента для клика. По умолчанию 1 (первый элемент).
        move_wait_type : str, optional
            Тип ожидания элемента для перемещения ('clickable', 'visible', 'located', 'find').
        click_wait_type : str, optional
            Тип ожидания элемента для клика ('clickable', 'visible', 'located', 'find').
        do_assert : bool, optional
            Если True, выполняет дополнительную проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        self.move_to_element(move_to, index=move_index, wait_type=move_wait_type)
        time.sleep(0.2)
        self.click_button(click_to, index=click_index, wait_type=click_wait_type, do_assert=do_assert, wait=wait)

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
