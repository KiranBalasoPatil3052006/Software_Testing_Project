import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#==============checking login page==============#

class TestLoginAutomation(unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Edge() #set up before each test begin
        self.driver.maximize_window() # maximize the screen
    
    def tearDown(self):
        self.driver.quit() #After ever test clean the resources
    
    def TestLogin(self):
        driver = self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")
        print("Opened login page")




