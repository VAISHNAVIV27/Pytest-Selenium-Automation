from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

pytestmark = [pytest.mark.regression, pytest.mark.sanity]


@pytest.mark.smoke
def test_ajaxform ():
    print("Title:",driver.title)

@pytest.mark.regression
def test_ajax ():
    driver.find_element(By.ID,"title")\
        .send_keys("Pytest Tutorials")
    driver.find_element(By.ID, "description")\
        .send_keys("Pytest Tutorials")
    driver.find_element(By.ID, "btn-submit").click()

    message = driver.find_element(By.ID, "submit-control").text
    assert message.__contains__("Ajax")

@pytest.mark.sanity
def test_ajax_login () :
    print("Login Successful")

@pytest.mark.integration
def test_ajax_logout () :
    print("Logout Successful")