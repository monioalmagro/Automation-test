#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#


import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class run_test_pages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_la_interempresarial(self):
        driver = self.driver
        driver.get("http://www.lainterempresarial.com")
        element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,"pie")))

    def test_hoy_dulce(self):
        driver = self.driver
        driver.get("https://muestraurllib.000webhostapp.com/index.html")
       
    def  test_portfolio(self):
        driver = self.driver
        driver.get("https:www.almagro.pythonanywhere.com")


    def tearDown(self):
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultado de mi test plan'))
