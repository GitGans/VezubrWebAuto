import time
from typing import NoReturn

import allure
from base.base_class import Base


class Registration(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sms_url = "https://cp.redsms.ru/"

    # Locators
    client_button = {
        "xpath": "//button[.//span[text()='Грузовладелец']]",
        "name": "client_button"
    }
    expeditor_button = {
        "xpath": "//button[.//span[text()='Экспедитор']]",
        "name": "expeditor_button"
    }
    producer_button = {
        "xpath": "//button[.//span[text()='Перевозчик']]",
        "name": "producer_button"
    }
    phone_input = {
        "xpath": "//input[@class='ant-input']",
        "name": "phone_input"
    }
    privacy_policy_checkbox = {
        "xpath": "//label[@class='ant-checkbox-wrapper']",
        "name": "privacy_policy_checkbox"
    }
    get_code_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "get_code_button"
    }
    code_input = {
        "xpath": "//input[@class='ant-input']",
        "name": "code_input"
    }
    continue_button = {
        "xpath": "//button[.//span[text()='Продолжить']]",
        "name": "continue_button"
    }
    inn_input = {
        "xpath": "//input[@type='text']",
        "name": "inn_input"
    }
    email_input = {
        "xpath": "(//input[@type='text'])[3]",
        "name": "email_input"
    }
    user_name_input = {
        "xpath": "(//input[@type='text'])[4]",
        "name": "user_name_input"
    }
    user_surname_input = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "user_surname_input"
    }
    password_input = {
        "xpath": "//input[@type='password']",
        "name": "password_input"
    }
    repeat_password_input = {
        "xpath": "(//input[@type='password'])[2]",
        "name": "repeat_password_input"
    }
    complete_button = {
        "xpath": "//button[.//span[text()='Завершить регистрацию']]",
        "name": "complete_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and contains(text(), 'Вы успешно')]",
        "reference": "Вы успешно зарегистрировались"
    }
    ok_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "calendar_ok_button"
    }
    registration_new_account = {
        "xpath": "//button[.//span[contains(text(), 'Регистрация Нового')]]",
        "name": "registration_new_account"
    }
    
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
        time.sleep(0.1)  # Фиксированная задержка
        value_word = element.text
        with allure.step(title=f"Assert \"{value_word}\" == \"{reference_value}\""):
            assert value_word == reference_value, f"Expected '{reference_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{reference_value}\"")
    