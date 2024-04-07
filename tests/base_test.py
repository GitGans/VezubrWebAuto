from base.base_class import Base
from pages.login_page import Login
from pages.sidebar import SideBar


def base_test(domain, role):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.authorization(role)

    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.sidebar_button)

    return base, sidebar
