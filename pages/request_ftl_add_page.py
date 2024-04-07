from base.base_class import Base
import re


class FTLAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Request owner drop-down list"""
    request_owner_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Грузовладелец')]",
        "name": "request_owner_select"
    }
    select_own_request = {
        "xpath": "//ul[@role='listbox']/li[text()='Собственный Заказ']",
        "name": "select_own_request"
    }
    start_date_field = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Дата подачи')]",
        "name": "start_date_field"
    }
    start_time_field = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Время подачи')]",
        "name": "start_time_field"
    }
    start_time_input = {
        "xpath": "//input[@class='ant-time-picker-panel-input']",
        "name": "start_time_input"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    """Request category drop-down list"""
    request_category_select = {
        "xpath": "//span[@class='ant-select-selection__rendered']",
        "name": "request_category_select"
    }
    select_freight = {
        "xpath": "//span[contains(text(), 'Грузовая')]",
        "name": "select_freight"
    }
    """TS type drop-down list"""
    vehicle_type_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Тип ТС')]",
        "name": "vehicle_type_select"
    }
    """TS body drop-down list"""
    vehicle_body_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Тип кузова')]",
        "name": "vehicle_body_select"
    }
    body_type_closed_checkbox= {
        "xpath": "//span[@class='ant-select-tree-title' and contains(text(), 'Закрытый')]",
        "name": "body_type_closed_checkbox"
    }
    """First address drop-down list"""
    first_address_select = {
        "xpath": "//*[@id='order-address-0']",
        "name": "first_address_select"
    }
    select_first_radio = {
        "xpath": "//span[@class='ant-radio']",
        "name": "select_first_radio"
    }
    """Second address drop-down list"""
    second_address_select = {
        "xpath": "//*[@id='order-address-1']",
        "name": "second_address_select"
    }
    select_second_radio = {
        "xpath": "(//span[@class='ant-radio'])[2]",
        "name": "select_first_radio"
    }
    confirm_address_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Применить выбранный')]]",
        "name": "confirm_address_button"
    }
    calculate_loading = {
        "xpath": "//i[@aria-label='icon: loading']",
        "name": "calculate_loading"
    }
    calculate_finish = {
        "xpath": "//span[@class='cost cost-min']",
        "name": "calculate_finish"
    }
    tariff_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'По тарифу')]]",
        "name": "tariff_button"
    }
    bargain_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'В торги')]]",
        "name": "bargain_button"
    }
    """Producer drop-down list"""
    producer_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Подрядчики')]",
        "name": "producer_select"
    }
    select_all_producer = {
        "xpath": "//span[@class='ant-select-tree-title' and contains(text(), 'Все подрядчики')]",
        "name": "select_all_producer"
    }
    producer_select_text = {
        "xpath": "//h4[@class='vz-form-group__title' and contains(text(), 'Выбор подрядчиков')]",
        "name": "producer_select_text"
    }
    publish_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Опубликовать')]]",
        "name": "publish_button"
    }
    continue_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Продолжить')]]",
        "name": "continue_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and contains(text(), 'Рейс был успешно создан')]",
        "reference": r'Рейс был успешно создан, .*'
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'OK')]]",
        "name": "create_button"
    }




