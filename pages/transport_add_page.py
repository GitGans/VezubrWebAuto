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
    create_vehicle_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Создать ТС']]",
        "name": "create_vehicle_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and contains(text(), 'успешно создан')]",
        "reference": ".* успешно создан.*"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
