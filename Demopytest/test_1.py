from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
driver.maximize_window()

def test_selenium_Demo1 () :
    print("Title",driver.title)

def test_selenium_Demo2 ():
    driver.find_element(By.XPATH,
                        "//h4[contains(text(),'Gender')]"
                        "//following::input[@value='Male']").click()

def test_selenium_Demo3():
    driver.find_element(By.XPATH,
                       "//h4[contains(text(),'Age')]"
                       "//following::input[@name='ageGroup']").click()

def test_selenium_Demo4():
    driver.find_element(By.XPATH,
                        "//button[text()='Get values']").click()

def test_selenium_Demo5():
    gender = driver.find_element(By.CSS_SELECTOR,
        ".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR,
        ".groupradiobutton").text
    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    assert gender is "Female", "Gender Is Not Correct"
    assert driver.title.__contains__("Selenium Grid Online")
    assert "51" in age_group, "Age Group Is Not Correct"



