from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Open the Streamlit app
driver.get("http://localhost:8501")

# Wait for the file uploader to load
file_uploader = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)

# Upload a file
file_uploader.send_keys(r"C:\Users\saran\Documents\GitHub\tinyMLaaS-sarang\frontend\tests\test_image.jpg")

# Wait for the file to be uploaded
time.sleep(5)

# Check if the file is uploaded by checking the name of the uploaded file
uploaded_file_name = driver.find_element(By.CLASS_NAME, "uploadedFileName").text

assert uploaded_file_name == "test_image.jpg"

print("Test passed")
# Close the driver
driver.quit()
