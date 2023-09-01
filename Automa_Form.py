import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir o navegador
def run():
        with webdriver.Chrome() as driver:
                # Acessar o formulário
                driver.get("https://pythonexamples.org/tmp/selenium/index-37.html?fname=teste&lname=teste")
                driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys("bob")
                driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys("dylan")
                driver.find_element(By.XPATH, '//*[@id="myform"]/input[3]').click

                input()      


if __name__ == '__main__':
        run()
        