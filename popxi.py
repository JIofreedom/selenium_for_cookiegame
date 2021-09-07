import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_path = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(edge_path)
driver.get("https://popxi.click/")
driver.implicitly_wait(5)
xi = driver.find_element_by_id("app")
# cat_count = driver.find_element_by_class_name("counter rot-r")

while True:
    xi.click()
