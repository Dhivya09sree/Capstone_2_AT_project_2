from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Define the expected menu items
        self.expected_menu_items = [
            "Admin", "PIM", "Leave", "Time", "Recruitment",
            "My Info", "Performance", "Dashboard",
            "Directory", "Maintenance", "Buzz"
        ]

        self.menu_items = [
            "User Management",
            "Job",
            "Organization",
            "Qualifications",
            "Nationalities",
            "Corporate Banking",
            "Configuration"
        ]
  # XPaths for the admin page and menu items
        self.admin_page = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        self.menu_items_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
        self.menu_elements  = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul'





    def expected_menu_validation(self):
        # Click the admin page
        admin = self.wait.until(EC.element_to_be_clickable(self.admin_page))
        admin.click()
        logger.info("Clicked the Admin page")

        # Wait for the menu items to be present
        menu_items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.menu_items_xpath)))

        # Extract the text from each menu item element
        menu_texts = [item.text for item in menu_items]


        # Validate each expected menu item
        for item in self.expected_menu_items:
            assert item in menu_texts, f"Menu item '{item}' not found on Admin page"
            logger.info(f"Menu item '{item}' found on Admin page")



    def validate_page_title(self):
            return self.driver.title

    def clickadmin(self):
        # Click the admin page
        admin = self.wait.until(EC.element_to_be_clickable(self.admin_page))
        admin.click()
        logger.info("Clicked the Admin page")


    def validate_menu_options(self):
        # Locate all menu elements by their XPath
        menu_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.menu_elements)))

        # Extract text from each menu element
        displayed_menu_items = [element.text for element in menu_elements]

        # Check if all expected menu items are displayed
        return all(item in displayed_menu_items for item in self.menu_items)