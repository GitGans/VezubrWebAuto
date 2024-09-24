from base.base_class import Base


class FTLList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
