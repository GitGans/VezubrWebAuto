from base.base_class import Base


class ProducersList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    producer_lkp_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '6883106209')]",
        "name": "producer_lkp_inn"
    }
    producer_logo_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5009112893')]",
        "name": "producer_logo_inn"
    }
    producer_vaz_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '6320002223')]",
        "name": "producer_vaz_inn"
    }
    producer_lke_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5178860124')]",
        "name": "producer_lke_inn"
    }
    action_button_lkp = {
        "xpath": "(//button[.//span[contains(text(), 'Действия')]])[2]",
        "name": "action_button_lkp"
    }
    action_button_vaz = {
        "xpath": "//button[.//span[contains(text(), 'Действия')]]",
        "name": "action_button_vaz"
    }
    go_to_account_button = {
        "xpath": "//button[.//span[contains(text(), 'Перейти в ЛК контрагента')]]",
        "name": "go_to_account_button"
    }
    assert_auto_lkp = {
        "reference_xpath": "//h4[@class='title' and text()='Auto LKP']",
        "reference": "Auto LKP"
    }
    assert_auto_vaz = {
        "reference_xpath": "//h4[@class='title' and text()='НАО АВТОВАЗ']",
        "reference": "НАО АВТОВАЗ"
    }
    accept_button = {
        "xpath": "(//button[.//span[text()='Принять']])[2]",
        "name": "accept_button"
    }
    add_internal_contractor = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_internal_contractor"
    }
    first_radio_button = {
        "xpath": "(//input[@type='radio' and @class='ant-radio-input'])[3]",
        "name": "first_radio_button"
    }
    confirm_choice_button = {
        "xpath": "//button[@class='ant-btn margin-left-15 ant-btn-primary']",
        "name": "confirm_choice_button"
    }
