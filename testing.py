import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://myappventure.herokuapp.com/login"
emailBenar="alyssa@gmail.com"
passwSalah="abcde"
passwBenar="abcdef"
email_tidak_ada="fnielson@gmail.com"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_email_kosong(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"password").send_keys(passwBenar) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"form div.flex.items-center.justify-start.text-xs.text-white.font-light").text

        self.assertIn(response_data, 'diperlukan email')

    def test_failed_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(emailBenar) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passwSalah) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Kata Sandi Salah')

    def test_failed_login_emailtdkada(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email_tidak_ada) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passwSalah) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Alamat email atau kata sandi yang\nanda masukan tidak valid')

    

    def test_password_kosong(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(emailBenar) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"form div.flex.items-center.justify-start.text-xs.text-white.font-light").text

        self.assertIn(response_data, 'diperlukan kata sandi')


    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(emailBenar) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passwBenar) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        current_url = driver.current_url
        self.assertIn(current_url, 'https://myappventure.herokuapp.com/home')

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()