from base.base_class import Base


class LTLTariffAdd(Base):
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
    """Ltl types drop-down list"""
    ltl_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "ltl_type_select"
    }
    """Ltl delivery region drop-down list"""
    dispatch_region_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "dispatch_region_select"
    }
    select_options = {
        "xpath": "//li[@class='ant-select-search ant-select-search--inline']//input[@class='ant-select-search__field']",
        "name": "select_options"
    }
    """Ltl dispatch region drop-down list"""
    delivery_region_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "delivery_region_select"
    }
    min_weight_input = {
        "xpath": "(//input[@role='spinbutton'])[1]",
        "name": "min_weight_input"
    }
    volumetric_weight_input = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "volumetric_weight_input"
    }
    direct_price_input = {
        "xpath": "(//input[@role='spinbutton'])[3]",
        "name": "direct_price_input"
    }
    reverse_price_input = {
        "xpath": "(//input[@role='spinbutton'])[4]",
        "name": "reverse_price_input"
    }
    min_price_input = {
        "xpath": "(//input[@role='spinbutton'])[5]",
        "name": "min_price_input"
    }
    kg_price_input = {
        "xpath": "(//input[@role='spinbutton'])[6]",
        "name": "kg_price_input"
    }
    temp_coeff_input = {
        "xpath": "(//input[@role='spinbutton'])[7]",
        "name": "temp_coeff_input"
    }
    delivery_time_input = {
        "xpath": "(//input[@role='spinbutton'])[8]",
        "name": "delivery_time_input"
    }
    add_tariff_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "add_hourly_tariff_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Тариф был успешно создан']",
        "reference": "Тариф был успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
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
