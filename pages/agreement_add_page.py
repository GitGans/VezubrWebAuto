from base.base_class import Base


class AgreementAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    agr_number_input = {
        "xpath": "//input[@id='contract_form_contractNumber']",
        "name": "agr_number_input"
    }
    agr_add_date_button = {
        "xpath": "//*[@id='contract_form_signedAt']/div/input",
        "name": "agr_add_date_button"
    }
    agr_end_date_button = {
        "xpath": "//*[@id='contract_form_expiresAt']/div/input",
        "name": "agr_end_date_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    agr_date_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "agr_date_input"
    }
    default_rate_toggl = {
        "xpath": "//*[@id='contract_form_defaultForClientRate']",
        "name": "default_rate_toggl"
    }
    default_bargain_toggl = {
        "xpath": "//*[@id='contract_form_defaultForBargain']",
        "name": "default_bargain_toggl"
    }
    """Registers auto type drop-down list"""
    registers_auto_select = {
        "xpath": "//*[@id='contract_form_typeAutomaticRegisters']/div/div",
        "name": "registers_auto_select"
    }
    select_all = {
        "xpath": "//li[@title='Включить все завершенные в отчетном периоде рейсы']",
        "name": "select_all"
    }
    select_confirmed = {
        "xpath": "//li[@title='Только рейсы с подтвержденными документами ГВ, "
                 "Расчетами Заказчиком и полученными оригиналами у водителей']",
        "name": "select_confirmed"
    }
    select_disabled = {
        "xpath": "//li[@title='Автоматическое формирование Реестров отключено']",
        "name": "select_disabled"
    }
    """Registers period type drop-down list"""
    registers_period_select = {
        "xpath": "//*[@id='contract_form_periodRegisters']/div/div",
        "name": "registers_period_select"
    }
    select_daily = {
        "xpath": "//li[contains(text(), 'Ежедневно')]",
        "name": "select_daily"
    }
    select_weekly = {
        "xpath": "//li[contains(text(), 'Еженедельно (каждый Понедельник)')]",
        "name": "select_weekly"
    }
    select_monthly = {
        "xpath": "//li[contains(text(), 'Ежемесячно (каждого 1 числа месяца)')]",
        "name": "select_monthly"
    }
    add_agr_button = {
        "xpath": "//button[@class='semi-wide margin-left-16 element-button theme-primary']",
        "name": "add_agr_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Договор был успешно создан']",
        "reference": "Договор был успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_add_button"
    }
    action_button = {
        "xpath": "//button[@class='filter-button circle box-shadow margin-left-12 default']",
        "name": "action_button"
    }
    termination_contract_button = {
        "xpath": "//span[contains(@class, 'text-big') and text()='Договор прекращен']",
        "name": "termination_contract_button"
    }
    agr_date_finish = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input ant-input-disabled'])[2]",
        "name": "agr_date_finish"
    }
    