from typing import NoReturn

from base.base_class import Base


class LTLAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    request_type_select = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "request_type_select"
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
    create_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
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
        "name": "calendar_ok_button"
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
        # Последовательный клик по кнопкам для выбора даты
        buttons_to_click_before_input = [
            self.start_at_from_button,
            self.today_button,
            self.start_at_from_button,
        ]
        for button in buttons_to_click_before_input:
            self.click_button(button)
        # Ввод новой временной метки в соответствующее поле
        self.backspace_num_and_input(self.start_at_from_input, 5, new_time)
        # Клик по кнопкам для подтверждения и создания LTL
        buttons_to_click_after_input = [
            self.calendar_ok_button,
            self.create_button,
        ]
        for button in buttons_to_click_after_input:
            self.click_button(button)
