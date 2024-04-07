from base.base_class import Base


class CargoPlaceAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Cargo place owner drop-down list"""
    cargo_place_owner_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Владелец Задания')]",
        "name": "cargo_place_owner_select"
    }
    select_own_cargo_place = {
        "xpath": "//ul[@role='listbox']/li[text()='Собственное Задание Экспедитора']",
        "name": "select_own_cargo_place"
    }
    select_cargo_place_lkz = {
        "xpath": "//ul[@role='listbox']/li[text()='Auto LKZ']",
        "name": "select_cargo_place_lkz"
    }
    """Cargo place owner drop-down list"""
    child_cp_select = {
        "xpath": "//div[@class='vz-form-item__label' and contains(text(), 'Вложенные Задания')]",
        "name": "child_cp_select"
    }
    """Cargo place type drop-down list"""
    lke_cp_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "cargo_place_type_select"
    }
    lkz_cp_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[1]",
        "name": "cargo_place_type_select"
    }
    select_type_box = {
        "xpath": "//ul[@role='listbox']/li[text()='Короб']",
        "name": "select_type_box"
    }
    select_type_bag = {
        "xpath": "//ul[@role='listbox']/li[text()='Мешок']",
        "name": "select_type_bag"
    }
    cp_quantity_input = {
        "xpath": "(//input[@role='spinbutton'])[1]",
        "name": "cp_quantity_input"
    }
    cp_weight_input = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "cp_weight_input"
    }
    cp_value_input = {
        "xpath": "(//input[@role='spinbutton'])[3]",
        "name": "cp_value_input"
    }
    cp_cost_input = {
        "xpath": "(//input[@role='spinbutton'])[4]",
        "name": "cp_cost_input"
    }
    """Cargo place status drop-down list"""
    lke_cp_status_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "lke_cp_status_select"
    }
    lkz_cp_status_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "lkz_cp_status_select"
    }
    select_status_new = {
        "xpath": "//ul[@role='listbox']/li[text()='Новое']",
        "name": "select_status_new"
    }
    select_status_waiting_send = {
        "xpath": "//ul[@role='listbox']/li[text()='Ожидание отправки']",
        "name": "select_status_waiting_send"
    }
    """Departure address drop-down list"""
    departure_address_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Адрес отправления')]",
        "name": "departure_address_select"
    }
    select_dp_address_first = {
        "xpath": "(//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'])[1]",
        "name": "select_dp_address_first"
    }
    """Delivery address drop-down list"""
    delivery_address_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Адрес доставки')]",
        "name": "delivery_address_select"
    }
    select_dl_address_first = {
        "xpath": "(//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'])[1]",
        "name": "select_dl_address_first"
    }
    create_cargo_place_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_cargo_place_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Грузоместо успешно создано']",
        "reference": "Грузоместо успешно создано"
    }
    confirm_add_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "create_button"
    }
    #Methods
    def add_base_cargo_place(self):
        self.dropdown_click_input_click(self.lkz_cp_type_select, "Короб")
        self.input_in_field(self.cp_weight_input, self.random_value_int_str(10, 20000))
        self.input_in_field(self.cp_value_input, self.random_value_float_str(0.1, 35.0))
        self.input_in_field(self.cp_cost_input, self.random_value_int_str(100, 1000000))
        self.dropdown_click_input_click(self.lkz_cp_status_select, "Новое")
        self.dropdown_click_input_enter(self.departure_address_select, "Екатеринбург")
        self.dropdown_click_input_enter(self.delivery_address_select, "Екатеринбург")
        buttons_to_click = [
            {'button': self.create_cargo_place_button, 'do_assert': True, 'wait': None},
            {'button': self.confirm_add_button, 'do_assert': False, 'wait': "lst"}
        ]
        for button_info in buttons_to_click:
            self.click_button(button_info['button'], do_assert=button_info.get('do_assert', False),
                              wait=button_info.get('wait', None))
