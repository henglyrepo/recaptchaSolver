from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from onest_captcha import OneStCaptchaClient

APIKEY = "replaceWithYourApiKey"
client = OneStCaptchaClient(apikey=APIKEY)

# Set the path to the WebDriver executable
webdriver_path = "storages\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(webdriver_path)

# Navigate to the ReCAPTCHA demo page
driver.get("https://www.google.com/recaptcha/api2/demo")
time.sleep(5)

# Get the site URL and site key from the ReCAPTCHA element
site_url = "https://www.google.com/recaptcha/api2/demo"
site_key = driver.find_element(By.CSS_SELECTOR, 'div[data-sitekey]').get_attribute('data-sitekey')

invisible = False  # Modify this value if the ReCAPTCHA is invisible

print(site_url)
print(site_key)

# Replace the following code with the appropriate API request to your reCAPTCHA solving service
result = client.recaptcha_v2_task_proxyless(site_url=site_url, site_key=site_key, invisible=invisible)

# Check the result and handle success or failure
if result["code"] == 0:  # Success
    print('Success')
    token = result["token"]
else:  # Failure
    print('Failure')
    message = result["message"]
    print(message)

# Set the solved Captcha
solved_captcha = driver.find_element(By.ID, 'g-recaptcha-response')
driver.execute_script(f'arguments[0].value = "{token}";', solved_captcha)

print(solved_captcha)

time.sleep(10)

# Find the submit button
submit_button = driver.find_element(By.CSS_SELECTOR, '#recaptcha-demo-submit')

# Click the submit button
submit_button.click()

time.sleep(100)
# Close the browser
driver.quit()
