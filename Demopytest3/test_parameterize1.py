import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome", "edge"])
def initialize_driver(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  # elif request.param == "firefox":
  #   driver = webdriver.Firefox()
  elif request.param == "edge":
    driver = webdriver.Edge()
  request.cls.driver = driver
  print("Browser: ", request.param)
  # driver.get(TestData.url)
  driver.maximize_window()
  yield
  print("Close Driver")
  driver.close()


@pytest.mark.usefixtures("initialize_driver")

class Test_Drivers():
  def test_multiple_browsers(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/")
    header = self.driver.find_element(By.CSS_SELECTOR,
      "div#__next h1").text
    print("Header: ", header)
    assert header == "Selenium Playground"