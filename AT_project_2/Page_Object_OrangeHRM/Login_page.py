from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        self.username_input_feild = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
        self.rest_password = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
        self.rest_message = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/h6')

        self.forgot_password_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')

        self.username_input = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        self.password_input = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.login_button = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")
        self.error_message = (By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > div > div.oxd-alert.oxd-alert--error > div.oxd-alert-content.oxd-alert-content--error > p")

    def forget_Password(self):
        forgot_password_element = self.wait.until(EC.element_to_be_clickable(self.forgot_password_link))
        forgot_password_element.click()
        logger.info("click forget password")

        username_element = self.wait.until(EC.element_to_be_clickable(self.username_input_feild))
        username_element.click()
        username_element.send_keys("Admin")
        logger.info("Enter the username : Admin")

        rest_password_element = self.wait.until(EC.element_to_be_clickable(self.rest_password))
        rest_password_element.click()
        logger.info("click reset password")

    def login(self, username, password):

        username_element = self.wait.until(EC.presence_of_element_located(self.username_input))
        username_element.send_keys(username)
        logger.info("Enter the username"+username)


        password_element = self.wait.until(EC.presence_of_element_located(self.password_input))
        password_element.send_keys(password)
        logger.info("Enter Password"+password)


        login_button_element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()
        logger.info("Login button clicked")

        