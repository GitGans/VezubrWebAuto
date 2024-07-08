from base.base_class import Base


class InsuranceAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    number_contract_field = {
        "xpath": "//*[@id='insurer-contract_form_number']",
        "name": "number_contract_field"
    }
    name_contract_field = {
        "xpath": "//*[@id='insurer-contract_form_title']",
        "name": "name_contract_field"
    }
    date_signing_field = {
        "xpath": "//*[@id='insurer-contract_form_startsAt']/div/input",
        "name": "date_signing_field"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    contract_time_field = {
        "xpath": "//*[@id='insurer-contract_form_expiresAt']/div/input",
        "name": "contract_time_field"
    }
    contract_time_field_open = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "contract_time_field_open"
    }
    max_value_field = {
        "xpath": "//*[@id='insurer-contract_form_maxAmountRestriction']",
        "name": "max_value_field"
    }
    bordero_togl = {
        "xpath": "//*[@id='insurer-contract_form_isBordero']",
        "name": "bordero_togl"
    }
    insurance_premium_field = {
        "xpath": "//*[@id='insurer-contract_form_premiumRate']",
        "name": "insurance_premium_field"
    }
    min_premium_field = {
        "xpath": "//*[@id='insurer-contract_form_minPremium']",
        "name": "min_premium_field"
    }
    add_contract_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "add_contract_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Договор был успешно создан']",
        "reference": "Договор был успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button"
    }
