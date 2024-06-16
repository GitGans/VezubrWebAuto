from base.base_class import Base


class Profile(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    general_info_tab = {
        "xpath": "//a[text()='Общая информация']",
        "name": "general_info_tab"
    }
    fact_address_input = {
        "xpath": "//*[@id='addressFact']",
        "name": "fact_address_input"
    }
    post_address_input = {
        "xpath": "//*[@id='addressPost']",
        "name": "post_address_input"
    }
    phone_input = {
        "xpath": "//*[@id='phone']",
        "name": "phone_input"
    }
    """VAT drop-down list"""
    vat_type_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'НДС')]",
        "name": "vat_type_select"
    }
    """Direct request drop-down list"""
    direct_request_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Кому направлять рейсы')]",
        "name": "direct_request_select"
    }
    """Values in system drop-down list"""
    values_in_system_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "values_in_system_select"
    }
    electronic_document_toggl = {
        "xpath": "//button[@id='docFlowConfiguration.electronicDocFlow']",
        "name": "electronic_document_toggl"
    }
    contour_link = {
        "xpath": "//td[@class='contour-links__col-action']/a[text()='Скопировать в буфер']",
        "name": "contour_link",
        "reference_xpath": "//span[text()='Ссылка скопирована']",
        "reference": "Ссылка скопирована"
    }
    additional_info_tab = {
        "xpath": "//a[text()='Дополнительная информация']",
        "name": "additional_info_tab",
        "reference_xpath": "//h2[@class='bold']",
        "reference": "Дополнительная информация о профиле"
    }
    checking_account_input = {
        "xpath": "//*[@id='checkingAccount']",
        "name": "checking_account_input",
    }
    bik_input = {
        "xpath": "//*[@id='bik']",
        "name": "bik_input",
    }
    groups_tab = {
        "xpath": "//a[text()='Группы']",
        "name": "groups_tab"
    }
    groups_delete_button = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/"
                 "table/tbody/tr[5]/td/div/div/div/img",
        "name": "groups_delete_button"
    }
    users_tab = {
        "xpath": "//a[text()='Пользователи']",
        "name": "users_tab",
        "reference_xpath": "//h2[@class='bold' and text()='Пользователи']",
        "reference": "Пользователи"
    }
    add_user_button = {
        "xpath": "//button[@class='mid element-button theme-primary']",
        "name": "add_user_button"
    }
    save_button = {
        "xpath": "//button[@class='semi-wide element-button theme-primary']",
        "name": "save_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Профиль успешно обновлен']",
        "reference": "Профиль успешно обновлен"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button",
        "reference_xpath": "//h2[@class='bold' and text()='Профиль']",
        "reference": "Профиль"
    }
    user_link = {
        "xpath": "//a[@class='link-back']",
        "name": "user_link"
    }
    delete_user_button = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/"
                 "table/tbody/tr[1]/td/div/div[2]/div[1]/img",
        "name": "delete_user_button"
    }
    password_input = {
        "xpath": "//input[@type='password']",
        "name": "password_input"
    }
    delete_confirm_button = {
        "xpath": "//button[@class='mid  element-button theme-primary']",
        "name": "delete_confirm_button",
        "reference_xpath": "//h2[contains(@class, 'bold') and contains(text(), 'Пользователи')]",
        "reference": "Пользователи"
    }
