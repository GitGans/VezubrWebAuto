from base.base_class import Base


class SideBar(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    new_order_reference_xpath = "//*[@id='main']/div/div[3]/div[2]/div/div/div[1]/h3"
    base_reference_xpath = "//h2[@class='big-title title-bold']"
    instructions_reference = "/html/body/div[1]/div/div/div[2]/div/div[1]/nav/div[1]/div[1]/a/div/div[2]/span"

    """Sidebar"""
    sidebar_button = {
        "xpath": ("//button[@class='border narrow light-bold notBlocked top-nav__sidebar "
                  "button-icon-menuHamburgerOrange element-button-icon element-button theme-simple']"),
        "name": "sidebar_button"
    }
    """Monitor"""
    monitor_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Монитор')]",
        "name": "monitor_button",
        "reference_xpath": "//*[@id='monitor-bargains']",
        "reference": "ТОРГИ"
    }
    """New order"""
    new_order_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Новый Заказ']",
        "name": "new_order_hover"
    }
    new_ftl_city_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'FTL Заказ - городской')]",
        "name": "new_ftl_city_button",
        "reference_xpath": new_order_reference_xpath,
        "reference": "Новый Заказ FTL перевозки"
    }
    new_ftl_inter_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'FTL Заказ - междугородний')]",
        "name": "new_ftl_inter_button",
        "reference_xpath": new_order_reference_xpath,
        "reference": "Новый Заказ FTL перевозки"
    }
    new_ltl_button = {
        "xpath": "//*[@id='cargo-side']",
        "name": "new_ltl_button",
        "reference_xpath": "//div[@class='order-form__title']",
        "reference": "Создание Заявки"
    }
    new_ftl_regular_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Регулярный рейс')]",
        "name": "new_ftl_regular_button",
        "reference_xpath": new_order_reference_xpath,
        "reference": "Создание шаблона рейса"
    }
    new_loaders_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'ПРР')]",
        "name": "new_loaders_button",
        "reference_xpath": new_order_reference_xpath,
        "reference": "Новый заказ ПРР"
    }
    """Requests"""
    requests_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Заявки']",
        "name": "requests_hover"
    }
    ftl_active_list_button = {
        "xpath": "//*[@id='requests-rate-tariff-side']",
        "name": "ftl_active_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Активные заявки"
    }
    ltl_active_list_button = {
        "xpath": "//*[@id='requests-ltl-side']",
        "name": "ltl_active_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Заявки на доставку Груза"
    }
    ftl_archive_list_button = {
        "xpath": "//*[@id='requests-side']",
        "name": "ftl_archive_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Архив заявок"
    }
    """Orders"""
    order_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Рейсы']",
        "name": "order_hover"
    }
    ftl_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Все FTL рейсы')]",
        "name": "ftl_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Рейсы"
    }
    auction_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Торги')]",
        "name": "auction_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Торги"
    }
    deferred_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Отложенные')]",
        "name": "deferred_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Отложенные рейсы"
    }
    regular_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Регулярные')]",
        "name": "regular_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Регулярные рейсы"
    }
    """Assignments"""
    assignments_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Задания']",
        "name": "assignments_hover"
    }
    cargo_place_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Задания')]",
        "name": "cargo_place_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Задания"
    }
    dispatch_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Отправления')]",
        "name": "dispatch_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Отправления"
    }
    """Contractor"""
    contractor_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Контрагенты']",
        "name": "contractor_hover"
    }
    clients_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Заказчики')]",
        "name": "clients_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Список контрагентов"
    }
    producers_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Подрядчики')]",
        "name": "producers_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Список контрагентов"
    }
    """Registries"""
    registries_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Реестры']",
        "name": "registries_hover"
    }
    reg_client_create_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Сформировать')]",
        "name": "reg_client_create_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Формирование .*"
    }
    reg_producer_create_list_button = {
        "xpath": "(//li[contains(@class, 'ant-menu-item') and contains(., 'Сформировать')])[2]",
        "name": "reg_producer_create_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Формирование .*"
    }
    registries_client_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Реестры для Заказчика')]",
        "name": "registries_client_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Реестры для заказчика"
    }
    registries_list_button_lkp = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Список реестров')]",
        "name": "registries_list_button_lkp",
        "reference_xpath": base_reference_xpath,
        "reference": "Реестры"
    }
    registries_list_button_lkz = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Реестры')]",
        "name": "registries_list_button_lkz",
        "reference_xpath": base_reference_xpath,
        "reference": "Реестры"
    }
    registries_producer_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Реестры от Подрядчика')]",
        "name": "registries_producer_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Реестры от подрядчика"
    }
    """Documents"""
    documents_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Документооборот']",
        "name": "documents_hover"
    }
    transport_doc_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Перевозочные документы')]",
        "name": "transport_doc_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Перевозочные документы"
    }
    verification_doc_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Проверка документов')]",
        "name": "verification_doc_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Проверка документов"
    }
    """Directories"""
    directories_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Справочники']",
        "name": "directories_hover"
    }
    addresses_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Адреса')]",
        "name": "addresses_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Адреса"
    }
    tariffs_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Тарифы')]",
        "name": "tariffs_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Тарифы"
    }
    drivers_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Водители')]",
        "name": "drivers_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Водители"
    }
    transports_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Т/С')]",
        "name": "transports_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Транспортные средства"
    }
    tractors_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Тягачи')]",
        "name": "tractors_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Тягачи"
    }
    trailers_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Полуприцепы')]",
        "name": "trailers_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Полуприцепы"
    }
    loaders_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Специалисты')]",
        "name": "loaders_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Специалисты"
    }
    insurers_list_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Страховые компании')]",
        "name": "insurers_list_button",
        "reference_xpath": base_reference_xpath,
        "reference": "Страховщики"
    }
    """Profile"""
    profile_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Профиль')]",
        "name": "profile_button",
        "reference_xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[1]/div[1]/h2",
        "reference": "Общая информация о профиле"
    }
    """Settings"""
    settings_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Настройки')]",
        "name": "settings_button",
        "reference_xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[1]/div/div/h1",
        "reference": "Настройки"
    }
    """References"""
    instructions_hover = {
        "xpath": "//span[@class='route-name no-events' and text()='Справка']",
        "name": "instructions_hover"
    }
    instructions_client_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Грузовладелец')]",
        "name": "instructions_client_button",
        "reference_xpath": instructions_reference,
        "reference": "Инструкция для грузовладельцев."
    }
    instructions_producer_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Перевозчик')]",
        "name": "instructions_producer_button",
        "reference_xpath": instructions_reference,
        "reference": "Инструкция для перевозчиков."
    }
    instructions_dispatcher_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Экспедитор')]",
        "name": "instructions_dispatcher_button",
        "reference_xpath": instructions_reference,
        "reference": "Инструкция для экспедиторов."
    }
    instructions_app_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'Моб. Приложение')]",
        "name": "instructions_app_button",
        "reference_xpath": instructions_reference,
        "reference": "Инструкция  для МП"
    }
    faq_button = {
        "xpath": "//li[contains(@class, 'ant-menu-item') and contains(., 'F.A.Q.')]",
        "name": "faq_button",
        "reference_xpath": instructions_reference,
        "reference": "FAQ"
    }
    """Exit"""
    exit_button = {
        "xpath": "//a[contains(@class, 'sidebar__list-item') and contains(., 'Выход')]",
        "name": "exit_button"
    }
