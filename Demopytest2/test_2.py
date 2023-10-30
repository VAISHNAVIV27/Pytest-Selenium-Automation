from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/")
driver.maximize_window()

def test_title():
    print("Title",driver.title)

def test_searching_product():
    driver.find_element(By.XPATH,
                        "//input[@placeholder='Search For Products']")\
                        .send_keys("iphone")
    driver.find_element(By.XPATH,
                        "//button[text()='Search']").click()
    search_value = driver.find_element(By.XPATH,
                                       "//h1[contains(text(),'Search')]").text
    assert "iphone" in search_value