#! /usr/bin/python3
from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import fspath
import details
import pytest

class TestFibersafeDashboard():

    #exec_path = "\\home\\sqared2\\Downloads\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"

    @pytest.fixture(scope="session")
    # def path_to_chrome():
    #     return ChromeDriverManager().install()
    #
    # @pytest.fixture
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver.implicitly_wait(10)
        driver.get(self.base_URL)
        driver.maximize_window()
        yield
        print("Test Completed")
        driver.close()
        driver.quit()
        

    def test_login(self,test_setup):
        #driver.get('https://fibersafe.tmrnd.com.my:84/portal/login')
        #driver.get('https://patrol.tmrnd.com.my/portal/login')
        driver.find_element_by_id(fspath.Login.login_usrname).send_keys(details.tenantuser)
        driver.find_element_by_id(fspath.Login.login_pass).send_keys(details.tenantpass)
        driver.find_element_by_xpath(fspath.Login.login_button).click()
        time.sleep(30)

    def test_dashboard_recentActivities(self,test_setup):
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(fspath.Dashboard.activities).click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(fspath.Dashboard.backbutton).click()

    def test_dashboard_decline(self,test_setup):
        time.sleep(10)
        driver.find_element_by_xpath(fspath.Dashboard.decline).click()
        time.sleep(2)
        driver.back()

    def test_dashboard_InProgress(self,test_setup):
        driver.find_element_by_xpath(fspath.Dashboard.inspection).click()
        time.sleep(2)
        driver.back()

    def test_dashboard_Inspection(self,test_setup):
        driver.find_element_by_xpath(fspath.Dashboard.progress).click()
        time.sleep(2)
        driver.back()

    def test_dashboard_Submitted(self,test_setup):
        driver.find_element_by_xpath(fspath.Dashboard.submitted).click()
        time.sleep(2)
        driver.back()

    def test_dashboard_Unassigned(self,test_setup):
        driver.find_element_by_xpath(fspath.Dashboard.unassigned).click()
        time.sleep(2)
        driver.back()

    def test_dashboard_Fibercut(self,test_setup):
        driver.find_element_by_xpath(fspath.Dashboard.fibercut).click()
        time.sleep(2)
        driver.back()


    def test_dashboard_filter(self,test_setup):
        driver.implicitly_wait(20)
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.regiondrop))
        select.select_by_visible_text('CENTRAL1')
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.statedrop))
        select.select_by_visible_text('SELANGOR')
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.wilayahdrop))
        select.select_by_visible_text('Msc')
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.zonedrop))
        select.select_by_visible_text('Zone Cyberjaya')
        time.sleep(5)

    def test_dashboard_FiberChart(self,test_setup):
        time.sleep(3)
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.chartdrop))
        select.select_by_visible_text('Fiber Cut')
        time.sleep(1)
        select = Select(driver.find_element_by_xpath(fspath.Dashboard.chartdrop))
        select.select_by_visible_text('AI App Downloads')



    def test_dashboard_recentWorklist(self,test_setup):
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(fspath.Dashboard.alerts).click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(fspath.Dashboard.backbutton).click()




