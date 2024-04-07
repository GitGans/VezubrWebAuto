from base.base_class import Base


class InsurersList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    insurer_energy_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '7705041231')]",
        "name": "insurer_energy_inn"
    }