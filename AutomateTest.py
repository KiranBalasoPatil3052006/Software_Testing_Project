import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class TestLoginAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
    
    def screenshot(self,name):
        driver = self.driver
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        driver.save_screenshot(f"screenshots/{name}.png")
        print(f"Screenshot saved: screenshots/{name}.png")
    
    def land_on_signup(self):
        driver=self.driver
        driver.get("file:///C:/Users/Kiran/Desktop/SOFTWARE_TESTING_PROJECT/index.html")
        print("Opened login page")
        time.sleep(3)

        signup = driver.find_element(By.ID, "toggleLink")
        signup.click()
        print("Sign up button is clicked")
        time.sleep(2)

        success_element = driver.find_element(By.XPATH, "//h2[contains(text(),'Sign Up')]")

        self.assertIn("Sign Up", success_element.text)
        print("Reached sign-up page")
        
        time.sleep(2) 
        self.screenshot("OnSignUpPage")
    
    #validation of signup 
    def test_signup_page(self):
        driver = self.driver
        driver.get("file:///C:/Users/Kiran/Desktop/SOFTWARE_TESTING_PROJECT/signup.html")
        print("Opened signup page")
        time.sleep(1)

        # Fields
        name = driver.find_element(By.ID, "signupName")
        mail = driver.find_element(By.ID, "signupEmail")
        password = driver.find_element(By.ID, "signupPassword")
        confirmPassword = driver.find_element(By.ID, "confirmPassword")
        terms = driver.find_element(By.ID, "terms")    
        createAccount = driver.find_element(By.ID, "signupBtn")

        # Invalid test
        print("Checking Invalid data on SignUp Page")
        invalid_data = ["Steve", " ", "123456789", "123789"]
        name.send_keys(invalid_data[0])
        mail.send_keys(invalid_data[1])
        password.send_keys(invalid_data[2])
        confirmPassword.send_keys(invalid_data[3])
        if not terms.is_selected():
            terms.click()
        createAccount.click()
        time.sleep(2)
        self.screenshot("InValidDataSignup")
        print("Invalid data on signup - DONE")

        # Clear only text inputs
        name.clear()
        mail.clear()
        password.clear()
        confirmPassword.clear()
        if terms.is_selected():
            terms.click()  # Uncheck if needed
        time.sleep(2)

        # Valid test
        print("Checking Valid data on SignUp Page")
        valid_data = ["Steve", "steve123@gmail.com", "123456789", "123456789"]
        name.send_keys(valid_data[0])
        mail.send_keys(valid_data[1])
        password.send_keys(valid_data[2])
        confirmPassword.send_keys(valid_data[3])
        terms.click()
        createAccount.click()
        time.sleep(2)
        self.screenshot("ValidDataSignup")
        print("Valid data on signup - DONE")




    #This function goes to login page
    def land_on_login(self):
        driver = self.driver
        driver.get("file:///C:/Users/Kiran/Desktop/SOFTWARE_TESTING_PROJECT/signup.html")
        print("Opened Login page")

        loginpage = driver.find_element(By.ID,"loginBtn")
        loginpage.click()
        time.sleep(2)
        success_element = driver.find_element(By.ID, "logintitle")
        #page validattion
        self.assertIn("Login", success_element.text)
        self.screenshot("OnLoginPage")

    def test_login_page(self):
        driver = self.driver
        driver.get("file:///C:/Users/Kiran/Desktop/SOFTWARE_TESTING_PROJECT/index.html")
        print("Login page opened - DONE")

        email = driver.find_element(By.ID,"loginEmail")
        password = driver.find_element(By.ID,"loginPassword")
        login_button = driver.find_element(By.ID,"loginBtn")

        #invalid login test
        invalid_data = ["stevegmail.com"," "]
        email.send_keys(invalid_data[0])
        password.send_keys(invalid_data[1])
        login_button.click()
        print("login button is clicked")
        time.sleep(1)
        self.screenshot("InvalidDataLogin")

        time.sleep(2)
        email.clear()
        password.clear()#previous data is cleared

        # Valid login test
        valid_data = ["steve123@gmail.com", "123456789"]
        email.send_keys(valid_data[0])
        password.send_keys(valid_data[1])
        login_button.click()
        time.sleep(2)
        self.screenshot("ValidDataLogin")
        print("login button is clicked") 
        time.sleep(1)
        self.screenshot("OnToDoPage")

     # Delete a specific item from todo list
    def delete_task(self, task_text):
        driver = self.driver
        todo_items = driver.find_elements(By.CLASS_NAME, "list-item")

        deleted = False
        for item in todo_items:
            input_field = item.find_element(By.TAG_NAME, "input")
            if input_field.get_attribute("value").strip().lower() == task_text.lower():
                delete_btn = item.find_element(By.CLASS_NAME, "delete")
                delete_btn.click()
                time.sleep(1)
                print(f"Deleted item: {task_text}")
                self.screenshot(f"Deleted_{task_text.replace(' ', '_')}")
                deleted = True
                break

            self.assertTrue(deleted, f"Task '{task_text}' was not found and could not be deleted.")
    
    #to mark any task as completed
    def task_completed(self, task_text):
        driver = self.driver
        todo_items = driver.find_elements(By.CLASS_NAME, "list-item")

        marked = False
        for item in todo_items:
            input_field = item.find_element(By.TAG_NAME, "input")
            if input_field.get_attribute("value").strip().lower() == task_text.lower():
                complete_btn = item.find_element(By.CLASS_NAME, "right")
                complete_btn.click()
                time.sleep(1)
                print(f"Marked task as completed: {task_text}")
                self.screenshot(f"Completed_{task_text.replace(' ', '_')}")
                marked = True
                break

        self.assertTrue(marked, f"Task '{task_text}' was not found to mark as completed.")
    
    #To Mark Task as not completed
    def task_not_completed(self, task_text):
        driver = self.driver
        todo_items = driver.find_elements(By.CLASS_NAME, "list-item")

        unmarked = False
        for item in todo_items:
            input_field = item.find_element(By.TAG_NAME, "input")
            if input_field.get_attribute("value").strip().lower() == task_text.lower():
                incomplete_btn = item.find_element(By.CLASS_NAME, "wrong")
                incomplete_btn.click()
                time.sleep(1)
                print(f"Marked task as NOT completed: {task_text}")
                self.screenshot(f"NotCompleted_{task_text.replace(' ', '_')}")
                unmarked = True
                break

        self.assertTrue(unmarked, f"Task '{task_text}' was not found to mark as NOT completed.")



    



    def test_todo_page(self):
        driver = self.driver
        driver.get("file:///C:/Users/Kiran/Desktop/SOFTWARE_TESTING_PROJECT/todopage.html")
        print("Opened Todo List page")

        # Verify the page title
        self.assertIn("Animated Todo List", driver.title)
        print("Title verified")

        # Find input and buttons
        todo_input = driver.find_element(By.ID, "todo-input")
        add_button = driver.find_element(By.ID, "add-btn")
        clear_button = driver.find_element(By.ID, "clear-btn")
        self.assertTrue(todo_input.is_displayed() and add_button.is_displayed())

        # Add sample todos
        sample_todo = ["Buy milk", "Buy chocolates", "Buy toys","Buy Cake"]
        for index, item in enumerate(sample_todo):
            todo_input.clear()
            todo_input.send_keys(item)
            add_button.click()
            time.sleep(2)
            self.screenshot(f"Todo_Added_{index+1}")

        #Using task_completed function marked these task as completed
        self.task_completed("Buy milk")
        time.sleep(1)
        self.task_completed("Buy chocolates")
        time.sleep(1)
        self.task_completed("Buy Cake")
        time.sleep(1)

        #Using task_not_completed function marked these task as not completed
        self.task_not_completed("Buy chocolates")
        time.sleep(2)
      
        


        # Clear all tasks from todo list
        clear_button.click()
        time.sleep(5)
        remaining_items = driver.find_elements(By.CLASS_NAME, "list-item")
        self.assertEqual(len(remaining_items), 0)
        print("Cleared all todos")
        time.sleep(2)
        self.screenshot("TodoCleared") 
        time.sleep(4)
        self.screenshot("Todo is Back")





        
        


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLoginAutomation('land_on_signup'))
    suite.addTest(TestLoginAutomation('test_signup_page'))
    suite.addTest(TestLoginAutomation('land_on_login'))
    suite.addTest(TestLoginAutomation('test_login_page'))
    suite.addTest(TestLoginAutomation('test_todo_page'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
