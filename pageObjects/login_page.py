from selenium.webdriver.common.by import By

class LoginPage:
    __USERNAME_ID = "user-name"
    __PASSWORD_ID = "password"
    __LOGIN_BUTTON_ID = "login-button"

    def __init__(self,driver) -> None:
        self.driver = driver

    def set_user_name(self, username):
        element = self.driver.find_element(By.ID, self.__USERNAME_ID)
        element.clear()
        element.send_keys(username)

    def set_password(self, password):
        element = self.driver.find_element(By.ID, self.__PASSWORD_ID)
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(By.ID, self.__LOGIN_BUTTON_ID)
        element.click()
