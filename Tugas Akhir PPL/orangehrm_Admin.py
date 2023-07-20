import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test(driver):
    time.sleep(3)
    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123' + Keys.ENTER)
    time.sleep(3)

    # Pengguna memasuki Menu Admin 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
    time.sleep(3)

    # Pengguna melakukan pencarian Users berdasarkan username yang terdaftar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('Alice.Duval')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Pengguna melakukan pencarian Users berdasarkan username yang tidak terdaftar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('Ilham')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Pengguna menambahkan User tanpa menginput apapun 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]').click()
    time.sleep(3)

    # Pengguna mencari User tanpa menginput apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()





    