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

    # Pengguna memasuki Menu Buzz 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]').click()
    time.sleep(3)

    # Pengguna melakukan post komentar pada menu Buzz
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div/form/div/div[2]/input').send_keys('Postingan Pertamaku' + Keys.ENTER)
    time.sleep(3)

    # Pengguna melakukan like pada postingan pada menu Buzz
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/div').click()
    time.sleep(3)

    # Pengguna melakukan post data (postingan) Buzz Newsfeed pada menu Buzz (Berupa Teks)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/textarea').send_keys('Test Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/div/button').click()
    time.sleep(3)

    # Pengguna melakukan post data (postingan) Buzz Newsfeed pada menu Buzz (Berupa Link video)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/textarea').send_keys('https://www.youtube.com/watch?v=jfiqzf5MXT8&pp=ygUDbmNz')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(3)

    


