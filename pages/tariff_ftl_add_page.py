from base.base_class import Base


class FTLTariffAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Tariffs types drop-down list"""
    tariff_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[1]",
        "name": "tariff_type_select"
    }
    """Ftl types drop-down list"""
    ftl_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "ftl_type_select"
    }
    """Fixed types drop-down list"""
    fixed_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "fixed_type_select"
    }
    departures_city_input = {
        "xpath": "(//input[@class='ant-input ant-select-search__field'])[1]",
        "name": "departures_city_input"
    }
    arrival_city_input = {
        "xpath": "(//input[@class='ant-input ant-select-search__field'])[2]",
        "name": "arrival_city_input"
    }
    tariff_name_input = {
        "xpath": "//input[@placeholder='Название тарифа']",
        "name": "tariff_name_input"
    }
    """Vehicle types drop-down list"""
    vehicle_type_select = {
        "xpath": "(//div[@title='Добавить машину'])[2]",
        "name": "vehicle_type_select"
    }
    body_type_closed_checkbox = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "body_type_closed_checkbox"
    }
    price_input = {
        "xpath": "//div[@class='tariff-cost-wrap tariff-cost-wrap--editable']",
        "name": "price_input"
    }
    address_cost_input = {
        "xpath": "(//div[@class='tariff-cost-wrap tariff-cost-wrap--editable'])[1]",
        "name": "address_cost_input"
    }
    free_downtime_input = {
        "xpath": "(//div[@class='tariff-cost-wrap tariff-cost-wrap--editable'])[2]",
        "name": "free_downtime_input"
    }
    extra_mileage_input = {
        "xpath": "//div[@class='tariff-cost-wrap tariff-cost-wrap--editable']",
        "name": "extra_mileage_input"
    }
    hourly_params_input = {
        "xpath": "//input[@role='spinbutton']",
        "name": "hourly_params_input"
    }
    fixed_params_input = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "fixed_params_input"
    }
    mileage_params_input = {
        "xpath": "(//input[@role='spinbutton'])",
        "name": "mileage_params_input"
    }
    mileage_params_input_2 = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "mileage_params_input"
    }
    mileage_params_input_3 = {
        "xpath": "(//input[@role='spinbutton'])[3]",
        "name": "mileage_params_input"
    }
    add_hourly_tariff_button = {
        "xpath": "//button[@class='semi-wide margin-left-16 element-button theme-primary']",
        "name": "add_hourly_tariff_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Тариф был успешно создан']",
        "reference": "Тариф был успешно создан"
    }
    add_fm_tariff_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "add_fm_tariff_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Тариф был успешно создан']",
        "reference": "Тариф был успешно создан"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button",
        "reference_xpath": "//div[contains(@class, 'ant-modal-confirm-content') and contains(., 'Тариф')]",
        "reference": 'Тариф.*'
    }
    """First address drop-down list"""
    first_address_select = {
        "xpath": "//*[@id='tariff-address-0']",
        "name": "first_address_select"
    }
    select_first_radio = {
        "xpath": "//span[@class='ant-radio']",
        "name": "select_first_radio"
    }
    """Second address drop-down list"""
    second_address_select = {
        "xpath": "//*[@id='tariff-address-1']",
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
    add_min_price_button = {
        "xpath": "//i[@title='Фильтр']",
        "name": "add_min_price_button"
    }
    add_confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary ant-btn-sm']",
        "name": "add_min_price_button"
    }
    delete_tariff_button = {
        "xpath": "//button[contains(., 'Удалить')]",
        "name": "delete_tariff_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Тариф успешно удален']",
        "reference": "Тариф успешно удален"
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
