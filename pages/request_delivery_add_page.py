from typing import NoReturn
import time
from base.base_class import Base


class DeliveryAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    request_type_select = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "request_type_select"
    }
    request_owner_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Грузовладелец')]",
        "name": "request_owner_select"
    }
    attach_cargo_place_button = {
        "xpath": "//button[@class='ant-btn order-assignments__add  ant-btn-primary ant-btn-lg']",
        "name": "attach_cargo_place_button"
    }
    existing_cargo_place_button = {
        "xpath": "//button[.//span[text()='Прикрепить существующие ГМ']]",
        "name": "existing_cargo_place_button"
    }
    start_at_from_button = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Дата и время начала от')]",
        "name": "start_at_from_button"
    }
    start_at_from_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "start_at_from_input"
    }
    calendar_ok_button = {
        "xpath": "//a[@class='ant-calendar-ok-btn']",
        "name": "calendar_ok_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    type_transportation_select = {
        "xpath": "//span[contains(@class, 'ant-select-selection__placeholder') and "
                 "text()='Выберите тип автоперевозки']",
        "name": "type_transportation_select"
    }
    select_type_cargo = {
        "xpath": "//span[contains(@class, 'ant-select-tree-title') and text()='Грузовая']",
        "name": "select_type_cargo"
    }
    vehicle_type_select = {
        "xpath": "//span[contains(@class, 'vz-form-item__label') and text()='Тип ТС']",
        "name": "vehicle_type_select"
    }
    body_type_select = {
        "xpath": "//span[contains(@class, 'vz-form-item__label') and text()='Тип кузова']",
        "name": "body_type_select"
    }
    select_closed = {
        "xpath": "//span[contains(@class, 'ant-select-tree-title') and text()='Закрытый']",
        "name": "select_closed"
    }
    text_route = {
        "xpath": "//h4[contains(@class, 'vz-form-group__title') and text()='Маршрут']",
        "name": "text_route"
    }
    first_address_select = {
        "xpath": "//*[@id='order-address-0']",
        "name": "first_address_select"
    }
    second_address_select = {
        "xpath": "//*[@id='order-address-1']",
        "name": "second_address_select"
    }
    address_radio_button = {
        "xpath": "//span[@class='ant-radio']",
        "name": "address_radio_button"
    }
    address_filter = {
        "xpath": "//input[@placeholder='Введите Адрес']",
        "name": "address_filter"
    }
    confirm_address_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Применить выбранный')]]",
        "name": "confirm_address_button"
    }
    required_documents_select = {
        "xpath": "//span[contains(@class, 'vz-form-item__label') and text()='Требуемые документы']",
        "name": "required_documents_select"
    }
    responsible_user_select = {
        "xpath": "//div[contains(@class, 'ant-select-selection__placeholder') and text()='Выберите пользователя']",
        "name": "responsible_user_select"
    }
    create_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    publish_later_button = {
        "xpath": "//button[.//span[text()='Опубликовать позже']]",
        "name": "publish_later_button",
        "reference_xpath": "//h2[@class='big-title title-bold']",
        "reference": "Заявки на доставку Груза"
    }
    publish_naw_button = {
        "xpath": "//button[.//span[text()='Опубликовать заявку']]",
        "name": "publish_naw_button"
    }
    tariff_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'По тарифу')]]",
        "name": "tariff_button"
    }
    rate_radio = {
        "xpath": "//span[text()='Задать ставку (тариф) вручную']",
        "name": "rate_radio"
    }
    rate_input = {
        "xpath": "//input[@role='spinbutton']",
        "name": "rate_input"
    }
    producer_select = {
        "xpath": "//span[contains(@class, 'ant-select-search__field__placeholder') and text()='Выберите подрядчиков']",
        "name": "producer_select"
    }
    producer_button = {
        "xpath": "//span[@class='ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal']",
        "name": "producer_button"
    }
    producer_lke_button = {
        "xpath": "//span[@title='Auto LKE']",
        "name": "producer_lke_button"
    }
    producer_lkp_button = {
        "xpath": "//span[@title='Auto LKP']",
        "name": "producer_lkp_button"
    }
    publish_button = {
        "xpath": "//button[.//span[text()='Опубликовать']]",
        "name": "publish_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Заявка была успешно расшарена']",
        "reference": "Заявка была успешно расшарена"
    }
    ok_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "calendar_ok_button",
        "reference_xpath": "//h2[@class='big-title title-bold']",
        "reference": "Активные LTL Заявки"
    }
    text_to_click = {
        "xpath": "//h4[@class='vz-form-group__title' and contains(text(), 'Выбор подрядчиков')]",
        "name": "text_to_click"
    }
    save_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "save_button"
    }

    # Methods
    """ Base request LTL"""
    def add_base_ltl(self) -> NoReturn:
        """
        Создание базовой LTL заявки. Метод включает выбор даты и времени доставки - текущее время + 30 минут,
        прикрепление грузоместа и завершается созданием LTL заявки.

        Parameters
        ----------
        Нет входных параметров.

        Returns
        -------
        NoReturn
            Метод не возвращает значения, но вызывает изменения на веб-странице.
        """
        # Получение нового времени с учетом изменений
        new_time = self.naw_time_change(30)
        # Клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_from_button)
        # Клик по кнопке выбора сегодняшней даты
        self.click_button(self.today_button)
        # Еще раз клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_from_button)
        # Ввод новой временной метки в соответствующее поле
        self.backspace_num_and_input(self.start_at_from_input, 5, new_time)
        # Клик по кнопке подтверждения выбора даты и времени
        self.click_button(self.calendar_ok_button)
        time.sleep(1)
        
    """ Base request FTL"""
    def add_base_ftl(self) -> NoReturn:
        """
        Создание базовой FTL заявки. Метод включает выбор даты и времени доставки - текущее время + 30 минут,
        выбор типа автоперевозки и ТС, прикрепление грузоместа, выбор адресов и завершается созданием FTL заявки.

        Parameters
        ----------
        Нет входных параметров.

        Returns
        -------
        NoReturn
            Метод не возвращает значения, но вызывает изменения на веб-странице.
        """
        # Получение нового времени с учетом изменений
        new_time = self.naw_time_change(30)
        # Клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_from_button)
        # Клик по кнопке выбора сегодняшней даты
        self.click_button(self.today_button)
        # Еще раз клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_from_button)
        # Ввод новой временной метки в соответствующее поле
        self.backspace_num_and_input(self.start_at_from_input, 5, new_time)
        # Клик по кнопке подтверждения выбора даты и времени
        self.click_button(self.calendar_ok_button)
        time.sleep(1)  # Ожидание перед продолжением выполнения
        # Выбор типа автоперевозки
        self.click_button(self.type_transportation_select)
        # Выбор типа груза (например, FTL)
        self.click_button(self.select_type_cargo)
        # Выбор типа ТС
        self.dropdown_click_input_click(self.vehicle_type_select, "до 0.5т")
        # Выбор типа кузова
        self.click_button(self.body_type_select)
        # Выбор закрытого типа кузова
        self.click_button(self.select_closed)
        # Клик на текст для закрытия списка типов кузова
        self.click_button(self.text_route)
        # Выбор первого адреса из списка
        self.click_button(self.first_address_select)
        # Фильтрация адресов и выбор первого адреса
        self.input_in_field(self.address_filter,
                            "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а")
        time.sleep(1)
        self.click_button(self.address_radio_button)
        # Подтверждение выбора адреса
        self.click_button(self.confirm_address_button)
        time.sleep(3)  # Ожидание перед продолжением выполнения
        # Выбор второго адреса из списка
        self.click_button(self.second_address_select)
        # Фильтрация адресов и выбор второго адреса
        self.input_in_field(self.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13")
        time.sleep(1)
        self.click_button(self.address_radio_button)
        # Подтверждение выбора адреса
        self.click_button(self.confirm_address_button)
