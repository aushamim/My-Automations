import os
import time
import psutil
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from plyer import notification


# Function to close all Edge processes
def close_edge_processes():
    for proc in psutil.process_iter(["pid", "name"]):
        if "msedge.exe" in proc.info["name"]:  # Check if the process is Edge
            proc.kill()


# Close all existing Edge windows
close_edge_processes()


# Load environment variables from .env file
load_dotenv()

# Set the URL you want to open
WEBSITE_URL = "https://www.smartquantai.com/"
USERNAME = os.getenv("WOSONHJ_USERNAME")
PASSWORD = os.getenv("WOSONHJ_PASSWORD")

# Set up Edge options to use your existing profile
edge_options = Options()
edge_options.add_argument(f"--user-data-dir={os.getenv('WOSONHJ_EDGE_PROFILE_PATH')}")
edge_options.add_argument("--profile-directory=Default")
edge_options.add_argument("--headless")

# Initialize WebDriver
driver = webdriver.Edge(options=edge_options)

# Open the URL
driver.maximize_window()
driver.get(WEBSITE_URL)

try:
    # Check if login button is available
    sign_in_button = driver.find_element(By.ID, "rtj_ydenglu")
    sign_in_button.click()
    time.sleep(1)

    # Enter username and password
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    remember_me_checkbox = driver.find_element(By.NAME, "cookietime")
    if not remember_me_checkbox.is_selected():
        remember_me_checkbox.click()

    sign_in_button = driver.find_element(By.NAME, "loginsubmit")
    sign_in_button.click()

    time.sleep(3)

except:
    print("Already logged in or login not required.")

    award_link = driver.find_element(
        By.CSS_SELECTOR, f"a[href*='plugin.php?id=are_sign:getaward&typeid=1']"
    )
    award_link.click()
    time.sleep(1)

print("WOSONHJ - Automation Finished")
notification.notify(
    title="WOSONHJ - Automation Finished",
    message="The login and award link clicking process is complete.",
    timeout=1,
)

driver.quit()
exit()
