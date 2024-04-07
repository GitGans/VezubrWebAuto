from base.base_class import Base


class Agreement(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    extra_agreement_tab = {
        "xpath": "//a[text()='ДУ тарификации']",
        "name": "extra_agreement_tab"
    }
    add_extra_agr_button = {
        "xpath": "//p[@class='no-margin']",
        "name": "add_extra_agr_button"
    }
    tariff_add_later = {
        "xpath": "//button[contains(., 'Назначить позже')]",
        "name": "tariff_add_later"
    }
    tariff_add_new = {
        "xpath": "//button[contains(., 'Добавить новый тариф')]",
        "name": "tariff_add_new"
    }
    tariff_appoint = {
        "xpath": "//button[contains(., 'Назначить тариф')]",
        "name": "tariff_appoint",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='ДУ к договору было успешно создано']",
        "reference": "ДУ к договору было успешно создано"
    }
    select_tariff_radio_button = {
        "xpath": "//span[@class='ant-radio']",
        "name": "select_tariff_radio_button"
    }

