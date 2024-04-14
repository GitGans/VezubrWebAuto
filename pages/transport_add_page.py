from base.base_class import Base


class TransportAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Transport types drop-down list"""
    vehicle_type_select = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/label/div/div[1]/div/div/div",
        "name": "vehicle_type_select"
    }
    vehicle_owner_select = {
        "xpath": "//div[@class='ant-input flexbox ']",
        "name": "vehicle_owner_select"
    }
    plate_number_input = {
        "xpath": "//input[@name='plateNumber']",
        "name": "plate_number_input"
    }
    mark_model_input = {
        "xpath": "//input[@name='markAndModel']",
        "name": "mark_model_input"
    }
    """Owner types drop-down list"""
    owner_types_select = {
        "xpath": "//span[contains(text(), 'Собственник')]",
        "name": "owner_types_select"
    }
    """Year of issue drop-down list"""
    year_select = {
        "xpath": "//span[contains(text(), 'Год Выпуска')]",
        "name": "year_select"
    }
    """Vehicle categories drop-down list"""
    vehicle_categories_select = {
        "xpath": "//span[contains(text(), 'Тип автоперевозки')]",
        "name": "year_select"
    }
    """Vehicle body types drop-down list"""
    vehicle_body_types_select = {
        "xpath": "//span[contains(text(), 'Подходящие типы кузова')]",
        "name": "vehicle_body_types_select"
    }
    capacity_input = {
        "xpath": "//input[@name='liftingCapacityInKg']",
        "name": "capacity_input"
    }
    volume_input = {
        "xpath": "//input[@name='volume']",
        "name": "volume_input"
    }
    pallets_input = {
        "xpath": "//input[@name='palletsCapacity']",
        "name": "pallets_input"
    }
    height_from_ground_input = {
        "xpath": "//input[@name='heightFromGroundInCm']",
        "name": "height_from_ground_input"
    }
    crane_capacity_input = {
        "xpath": "//input[@name='craneCapacity']",
        "name": "crane_capacity_input"
    }
    crane_length_input = {
        "xpath": "//input[@name='craneLength']",
        "name": "crane_length_input"
    }
    create_vehicle_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Создать ТС']]",
        "name": "create_vehicle_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and contains(text(), 'успешно создан')]",
        "reference": ".* успешно создан.*"
    }
    edit_confirm_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Сохранить']]",
        "name": "edit_confirm_vehicle_button",
        "reference_xpath": "//span[contains(text(), 'успешно обновлен')]",
        "reference": ".* успешно обновлен.*"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    number_passengers_select = {
        "xpath": "//span[contains(text(), 'Пассажиров (без учета водителя)')]",
        "name": "number_passengers_select"
    }
    edit_button = {
        "xpath": "//button[contains(text(), 'Редактировать ТС')]",
        "name": "edit_button"
    }
    hydro_lift_toggl = {
        "xpath": "//span[contains(text(), 'Наличие гидроборта')]",
        "name": "hydro_lift_toggl"
    }
    gps_monitoring_toggl = {
        "xpath": "//span[contains(text(), 'Наличие GPS датчика')]",
        "name": "gps_monitoring_toggl"
    }
    pallets_jack_toggl = {
        "xpath": "//span[contains(text(), 'Наличие рохлы')]",
        "name": "hydro_lift_toggl"
    }
    conics_toggl = {
        "xpath": "//span[contains(text(), 'Наличие коников')]",
        "name": "conics_toggl"
    }
    strap_toggl = {
        "xpath": "//span[contains(text(), 'Наличие ремней')]",
        "name": "strap_toggl"
    }
    chain_toggl = {
        "xpath": "//span[contains(text(), 'Наличие цепи')]",
        "name": "chain_toggl"
    }
    tarpaulin_toggl = {
        "xpath": "//span[contains(text(), 'Наличие брезента')]",
        "name": "tarpaulin_toggl"
    }
    net_toggl = {
        "xpath": "//span[contains(text(), 'Наличие сети')]",
        "name": "net_toggl"
    }
    wheel_chock_toggl = {
        "xpath": "//span[contains(text(), 'Наличие башмаков')]",
        "name": "wheel_chock_toggl"
    }
    corner_pillar_toggl = {
        "xpath": "//span[contains(text(), 'Наличие угловых стоек')]",
        "name": "corner_pillar_toggl"
    }
    doppel_stock_toggl = {
        "xpath": "//span[contains(text(), 'Наличие допельштока')]",
        "name": "doppel_stock_toggl"
    }
    wooden_floor_toggl = {
        "xpath": "//span[contains(text(), 'Наличие деревянного пола')]",
        "name": "wooden_floor_toggl"
    }
    side_loading_toggl = {
        "xpath": "//span[contains(text(), 'Боковая погрузка')]",
        "name": "side_loading_toggl"
    }
    top_loading_toggl = {
        "xpath": "//span[contains(text(), 'Верхняя погрузка')]",
        "name": "top_loading_toggl"
    }


