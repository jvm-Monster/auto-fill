import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.edge.service import Service

# Set the path to your WebDriver executable
driver_path = "C:\\Users\Jvm-Monster\\Downloads\\reactcours\\edgedriver_win64\\msedgedriver.exe"

# Initialize the WebDriver
driver = webdriver.Edge(service=Service(driver_path))

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Open the login page
# Construct the path to the HTML file
html_file_path = os.path.join(current_dir, 'htmlfile', 'autofill.html')

# Open the login page
driver.get("file:///" + html_file_path)

# Find the username and password fields and fill them in
username_field = driver.find_element(by="id", value="username")
username_field.send_keys("Group 5 Auto Fill")

password_field = driver.find_element(by="id", value="password")
password_field.send_keys("123456789.")

# Submit the form
password_field.send_keys(Keys.RETURN)

# Optionally, wait for a few seconds before closing the browser
time.sleep(100)

# Close the browser
driver.quit()

