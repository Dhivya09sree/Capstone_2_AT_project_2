import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Object_OrangeHRM.Login_page import LoginPage
from Page_Object_OrangeHRM.Admin_page import AdminPage

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('test_login.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class TestLoginPage:

    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def setup(self):
        logger.info("Setting up WebDriver instance")
        driver = webdriver.Chrome()
        yield driver
        logger.info("Tearing down WebDriver instance")
        driver.quit()

    def test_login(self, setup):
        logger.info("TC_PIM_01")

        self.driver = setup
        self.driver.get(self.BASE_URL)
        logger.info(f"Navigated to {self.BASE_URL}")

        login_page = LoginPage(self.driver)

        login_page.forget_Password()
        logger.info("Clicked forget password link")
        logger.info("Entered user input")
        logger.info("Clicked reset password link")

        # Wait for the message element to be visible
        success_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/h6')))
        print(success_message.text)

        # Validate the Reset Password message text
        if "Reset Password link sent successfully" in success_message.text:
            print("Reset Password link sent successfully")
            logger.info(f"Reset Password link sent successfully: {success_message.text}")
        else:
            print("Failed to reset Password link. Unexpected success message.")
            logger.error("Failed to reset Password link. Unexpected success message.")


    def test_admin_menu( self, setup):

        logger.info("TC_PIM_02")

        self.driver = setup
        self.driver.get(self.BASE_URL)
        logger.info(f"Navigated to {self.BASE_URL}")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.validate_page_title()
        # Validation part
        if admin_page.validate_page_title() == "OrangeHRM":
            logger.info("Title is correct")
        else:
            logger.info("Page title is incorrect")

        admin_page.clickadmin()
        logger.info("click the admin page")

        self.driver.implicitly_wait(30)

        admin_page.validate_menu_options()

        menu_items = [
            "User Management ",
            "Job",
            "Organization",
            "Qualifications",
            "Nationalities",
            "Corporate Branding",
            "Configuration"
        ]

        # Locate all menu elements by their XPath
        menu_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]')))

        # Extract text from each menu element
        displayed_menu_text = [element.text for element in menu_elements]

        # Split the text into individual menu items (assuming they are separated by '\n')
        displayed_menu_items = []
        for text in displayed_menu_text:
            displayed_menu_items.extend(text.split('\n'))

        # Trim any leading or trailing whitespace from each menu item
        displayed_menu_items = [item.strip() for item in displayed_menu_items]

        logger.info(f"Menu items displayed: {displayed_menu_items}")

        # Check if all expected menu items are displayed
        for item in menu_items:
            assert item.strip() in displayed_menu_items, f"Menu item '{item}' not found on Admin page"
            logger.info(f"Menu item '{item}' found on Admin page")

    def test_admin(self, setup):
        logger.info("TC_PIM_03")

        self.driver = setup
        self.driver.get(self.BASE_URL)
        logger.info(f"Navigated to {self.BASE_URL}")

        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.expected_menu_validation()

        # Define the expected menu items
        expected_menu_items = [
            "Admin", "PIM", "Leave", "Time", "Recruitment",
            "My Info", "Performance", "Dashboard",
            "Directory", "Maintenance", "Buzz"
        ]

        # Wait for the menu items to be present
        menu_items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')))

        # Extract the text from each menu item element
        menu_texts = [item.text for item in menu_items]
        logger.info(f"Menu items displayed: {menu_texts}")

        # Validate each expected menu item
        for item in expected_menu_items:
            assert item in menu_texts, f"Menu item '{item}' not found on Admin page"
            logger.info(f"Menu item '{item}' found on Admin page")
