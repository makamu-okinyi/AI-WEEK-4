from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Define the URL for the test login page
LOGIN_URL = "https://the-internet.herokuapp.com/login"

# Define credentials for valid and invalid tests
VALID_USERNAME = "tomsmith"  # The Internet Herokuapp's valid user
VALID_PASSWORD = "SuperSecretPassword!"  # The Internet Herokuapp's valid password
INVALID_USERNAME = "baduser"
INVALID_PASSWORD = "wrongpassword"


class AutomatedLoginTest:
    """
    Automates login test cases using Selenium WebDriver.
    """

    def __init__(self):
        # Setting up the Chrome WebDriver
        # Using webdriver_manager to automatically handle the correct driver download/version
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) # Wait up to 10 seconds for elements to appear

    def setup(self):
        """Opens the login page before each test."""
        self.driver.get(LOGIN_URL)
        print(f"Opened: {LOGIN_URL}")

    def teardown(self):
        """Closes the browser after all tests are complete."""
        if self.driver:
            self.driver.quit()
            print("Browser closed.")

    def run_valid_login_test(self, username, password):
        """Automates a test with valid credentials."""
        self.setup()
        print(f"\n--- Running Valid Login Test with {username} ---")

        # 1. Find the username and password fields and the login button
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in")

        # 2. Input credentials
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # 3. Click the login button
        login_button.click()
        time.sleep(10) # Small pause to let the page load

        # 4. Verification: Check for the success message (on Herokuapp, it checks for a 'secure' area element)
        try:
            # Check for the secure area heading or a success flash message
            success_message = self.driver.find_element(By.CLASS_NAME, "flash.success")
            print("✅ TEST PASSED: Valid login was successful.")
            return "Success"
        except:
            print("❌ TEST FAILED: Valid login did not redirect to the secure area.")
            return "Failure"

    def run_invalid_login_test(self, username, password):
        """Automates a test with invalid credentials, using the correct locator."""
        self.setup()
        print(f"\n--- Running Invalid Login Test with {username} ---")

        # 1. Find elements
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in")

        # 2. Input credentials and click login
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        time.sleep(1)

        # 4. Verification: Check for the failure/error message using the 'flash' ID
        try:
           
            error_message_container = self.driver.find_element(By.ID, "flash")
            
            # Check if the expected error text is present in the container
            if "Your username is invalid!" in error_message_container.text:
                print("✅ TEST PASSED: Invalid login correctly showed an error message.")
                return "Success"
            else:
                 print("❌ TEST FAILED: Invalid login showed an unexpected message.")
                 return "Failure"
        except:
            print("❌ TEST FAILED: Did not find the expected error message element (ID='flash').")
            return "Failure"


def main():
    """Main execution function to run all tests and capture results."""
    tester = AutomatedLoginTest()
    
    # Store results
    results = {
        'Valid_Login': tester.run_valid_login_test(VALID_USERNAME, VALID_PASSWORD),
        # Note: The browser closes briefly after the first test (Valid_Login) 
        # because the setup/teardown cycle is inside each run_* method in the original script.
        # It opens again for the second test (Invalid_Login).
        'Invalid_Login': tester.run_invalid_login_test(INVALID_USERNAME, INVALID_PASSWORD)
    }

    # --- ADDED PAUSE HERE ---
    print("\n--- TEST EXECUTION COMPLETE. PAUSING BROWSER FOR 5 SECONDS ---")
    time.sleep(30)  # Pause for 30 seconds to view the final result before closing
    # -------------------------

    # Calculate rates
    total_tests = len(results)
    successes = list(results.values()).count("Success")
    failures = list(results.values()).count("Failure")
    
    success_rate = (successes / total_tests) * 100
    failure_rate = (failures / total_tests) * 100

    print("\n" + "="*50)
    print("TEST EXECUTION SUMMARY")
    print(f"Total Tests Run: {total_tests}")
    print(f"Success Rate: {success_rate:.2f}% ({successes} passes)")
    print(f"Failure Rate: {failure_rate:.2f}% ({failures} failures)")
    print("="*50)

    tester.teardown()

if __name__ == "__main__":

    main()
