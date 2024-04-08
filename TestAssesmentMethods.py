import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import os



class TestAssesmentMethods:

    global chromedriver_path

    STATUSES = (By.ID , "estatus")
    UNMASK_SSN_CHECKBOX = (By.XPATH , "//label[text() = 'Unmask SSN for download']")
    PLAN_YEAR_SELECT_OPTION = (By.XPATH , "//option[text() = '01/01/2024 to 12/31/2024']")

    BENEFIT_TYPE_SELECT_OPTION = (By.XPATH , "//td[text() = 'Available Benefit Types']/parent::tr/following-sibling::tr/td//option[text() = 'Voluntary Employee Life']")
    PLAN_SELECT_OPTION = (By.XPATH , "//td[contains(text(), 'Plans')]/parent::tr/following-sibling::tr/td//option[text() = 'Voluntary Employee Life']")


    PLAN_FIELD_SELECT_OPTION_CREATED_AT = (By.XPATH , "//td[text() = 'Available Plan Fields']/parent::tr/following-sibling::tr/td//option[text() = 'Created At']")
    PLAN_FIELD_SELECT_OPTION_CHANGE_DATE = (By.XPATH , "//td[text() = 'Available Plan Fields']/parent::tr/following-sibling::tr/td//option[text() = 'Change Effective Date']")
    RUN_REPORT_BUTTON = (By.ID , "run-report-now-btn")


    def __init__(self):
        options = Options()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.download_dir = os.path.join(current_dir, 'downloads')
        options.add_experimental_option('prefs', {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://benefits.plansourcetest.com")
        self.driver.maximize_window()

    def read_file(self):
        # Get the latest file in the download directory
        files = os.listdir(self.download_dir)
        paths = [os.path.join(self.download_dir, basename) for basename in files]
        latest_file = max(paths, key=os.path.getctime)

    def admin_login(self):
            self.driver.find_element(By.ID, 'user_name').send_keys('nidavellir_admin')
            self.driver.find_element(By.ID, 'password').send_keys('automation1')
            login = self.driver.find_element(By.ID, 'logon_submit')
            login.click()

    def redirect_to_report_benifit(self):
        self.driver.get("https://benefits.plansourcetest.com/admin/report_benefit")

    def select_employee_status(self):
        select_element = self.driver.find_element(*self.STATUSES)
        element = Select(select_element)
        element.select_by_visible_text("All Statuses")

    def check_unmask_ssn(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.UNMASK_SSN_CHECKBOX))


        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(5)

    def select_plan_year(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAN_YEAR_SELECT_OPTION))
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(5)

    def select_benefit_type(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.BENEFIT_TYPE_SELECT_OPTION))
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(5)
    def select_plan(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAN_SELECT_OPTION))
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(5)

    def select_plan_fields(self):
        option1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAN_FIELD_SELECT_OPTION_CREATED_AT))
        option2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAN_FIELD_SELECT_OPTION_CHANGE_DATE))
        actions = ActionChains(self.driver)

        actions.double_click(option1).perform()
        actions.double_click(option2).perform()
        time.sleep(5)

    def select_available_employee_fields(self):
        options = ["Address 1","Hire Date","First Name","Last Name","Gender","Benefit Salary","SSN"]

        for option in options:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,f"//td[text() = 'Available Employee Fields']/parent::tr/following-sibling::tr/td//option[text() = '{option}']")))
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            time.sleep(1)


    def run_report(self):
        time.sleep(2)
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.RUN_REPORT_BUTTON))
        button.click()
        time.sleep(3)