from base.base_class import Base


class Insurer(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    insurer_info = {
        "xpath": "//a[@class='vz-tabs-modern__item matched' and contains(text(), 'Общая информация')]",
        "name": "insurer_info"
    }
    insurer_contracts = {
        "xpath": "//a[@class='vz-tabs-modern__item' and contains(text(), 'Договоры')]",
        "name": "insurer_contracts"
    }
    add_contract_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "add_contract_button"
    }
    insured_orders_list = {
        "xpath": "//a[@class='vz-tabs-modern__item' and contains(text(), 'Застрахованные рейсы')]",
        "name": "insured_orders_list"
    }
    first_contract_link = {
        "xpath": "//div[@class='cell-text-overflow-content']",
        "name": "first_contract_link"
    }
