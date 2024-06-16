from base.base_class import Base
import time


class ExtraAgreementAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    extra_agr_number_input = {
        "xpath": "//*[@id='agreement_form_agreementNumber']",
        "name": "extra_agr_number_input"
    }
    extra_agr_add_date_button = {
        "xpath": "//*[@id='agreement_form_signedAt']/div/input",
        "name": "extra_agr_add_date_button"
    }
    extra_agr_end_date_button = {
        "xpath": "//*[@id='agreement_form_expiresAt']/div/input",
        "name": "extra_agr_end_date_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    extra_agr_date_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "extra_agr_date_input"
    }
    extra_agr_comment_input = {
        "xpath": "//*[@id='agreement_form_comment']",
        "name": "extra_agr_comment_input"
    }
    add_extra_agr_button = {
        "xpath": "//button[@class='semi-wide margin-left-16 element-button theme-primary']",
        "name": "add_extra_agr_button"
    }
    appoint_later_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16' and span[contains(text(), 'Назначить позже')]]",
        "name": "add_extra_agr_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='ДУ к договору было успешно создано']",
        "reference": "ДУ к договору было успешно создано"
    }
    confirm_add_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "create_button"
    }
    confirm_tariff_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='ДУ к договору было успешно создано']",
        "reference": "ДУ к договору было успешно создано"
    }
    radio_button = {
        "xpath": "//input[@type='radio' and @class='ant-radio-input']",
        "name": "radio_button"
    }
    # Methods

    def add_base_extra_agreements(self):
        self.input_in_field(self.extra_agr_number_input, f"№-{self.get_timestamp()}")
        buttons_to_click = [
            self.extra_agr_add_date_button,
            self.today_button,
            self.extra_agr_end_date_button
        ]
        for button in buttons_to_click:
            self.click_button(button)
        time.sleep(0.5)
        self.input_in_field(self.extra_agr_date_input, "01012040", press_enter=True)
        self.input_in_field(self.extra_agr_comment_input, "ДУ создано автотестом", click_first=True)
        self.click_button(self.add_extra_agr_button)
