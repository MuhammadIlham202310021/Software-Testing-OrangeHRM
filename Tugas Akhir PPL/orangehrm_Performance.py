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

    # Pengguna memasuki Menu Performance 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]').click()
    time.sleep(3)

    # Pengguna memasuki Sub Menu Manage Reviews    
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    time.sleep(3)

    # Pengguna melakukan Manage Performance Reviews berdasarkan rentang waktuy yang sesuai 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('2023-07-18')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('2024-07-18')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Pengguna melakukan Manage Performance Reviews berdasarkan rentang waktu dengan format yang salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('18-2023-07')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Pengguna menambahkan Performance Review tanpa input apapun 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[1]').click()
    time.sleep(3)

    # Pengguna melihat detail Performance Reviews 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    time.sleep(3)

    # Pengguna Melihat My Performance Trackers 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
    time.sleep(3)
