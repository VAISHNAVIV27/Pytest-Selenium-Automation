from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome()
driver.maximize_window()


@pytest.mark.parametrize("num1,num2,expected_total",
                         [
                          ("20","10","30"),
                          ("40","10","50"),
                          ("50","10","60")
                         ])


def test_parameterize_add(num1,num2,expected_total) :
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID,"sum1").send_keys(num1)
    driver.find_element(By.ID,"sum2").send_keys(num2)
    driver.find_element(By.XPATH,"//button[text()='Get Sum']").click()
    message = driver.find_element(By.ID,"addmessage").text
    assert message == expected_total, \
        "Actual & Expected Totals Do Not Match"
