from base.base_class import Base


class Contractor(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_agreements_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "add_agreements_button"
    }
    settings_tab = {
        "xpath": "//a[contains(text(), 'Настройки')]",
        "name": "settings_tab"
    }
    delegation_type_select = {
        "xpath": "//div[@class='ant-select-selection-selected-value']",
        "name": "delegation_type_select"
    }
    agreements_link = {
        "xpath": "(//div[@class='cell-text-overflow-content'])[1]",
        "name": "agreements_link"
    }
    save_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "save_button",
        "reference_xpath": "//span[text()='Данные обновлены']",
        "reference": "Данные обновлены"
    }
    user_checkbox_empty = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "user_checkbox_empty"
    }
    user_checkbox_filled = {
        "xpath": "//span[@class='ant-checkbox ant-checkbox-checked']",
        "name": "user_checkbox_filled"
    }
    save_delegation_button = {
        "xpath": "//button[@class='ant-btn settings-btn ant-btn-primary']",
        "name": "save_delegation_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Изменения сохранены']",
        "reference": "Изменения сохранены"
    }
    ok_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "ok_button"
    }