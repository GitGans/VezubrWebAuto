from base.base_class import Base


class LUOTariffAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Tariffs types drop-down list"""
    tariff_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[1]",
        "name": "tariff_type_select"
    }
    tariff_name_input = {
        "xpath": "//input[@placeholder='Название тарифа']",
        "name": "tariff_name_input"
    }
    """Loader types drop-down list"""
    loader_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[5]",
        "name": "loader_type_select"
    }
    price_input = {
        "xpath": "//div[@class='tariff-cost-wrap tariff-cost-wrap--editable']",
        "name": "price_input"
    }
    price_hour_input = {
        "xpath": "//div[@class='tariff-cost-wrap tariff-cost-wrap--editable']",
        "name": "price_hour_input"
    }
    price_mrr_input = {
        "xpath": "(//div[@class='tariff-cost-wrap tariff-cost-wrap--editable'])[2]",
        "name": "price_mrr_input"
    }
    params_input = {
        "xpath": "//input[@role='spinbutton']",
        "name": "hourly_params_input"
    }
    add_tariff_button = {
        "xpath": "//button[@class='semi-wide margin-left-16 element-button theme-primary']",
        "name": "add_tariff_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Тариф был успешно создан']",
        "reference": "Тариф был успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    clone_tariff_button = {
        "xpath": "//button[contains(., 'Клонировать')]",
        "name": "clone_tariff_button"
    }
    action_menu_button = {
        "xpath": "//button[@class='filter-button circle default']",
        "name": "action_menu_button"
    }
    copy_tariff_button = {
        "xpath": "//span[contains(., 'Копировать тариф')]",
        "name": "copy_tariff_button"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button",
        "reference_xpath": "//div[contains(@class, 'ant-modal-confirm-content') and contains(., 'Тариф')]",
        "reference": 'Тариф.*'
    }
