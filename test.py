from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Define the login credentials
email = "youremail@example.com" # your email for logging in
password = "password" # your password

# Start the WebDriver and navigate to the website
driver = webdriver.Chrome() # initialize chrome webdriver
driver.get("https://magento.softwaretestingboard.com/") # open the website URL

# Sign In
# Locate and click on the "Sign In" Link
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

# Enter email and password
# Locate the email and password fields, then enter the provided credentials
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "pass")))
email_field.send_keys(email)
password_field.send_keys(password)

# Click the Sign In button
# Locate and click on the "Sign In" button
driver.find_element(By.ID, "send2").click()

# Wait for the login success message
# Wait for the success message element to be visible
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'logged-in')]")))

# Search for "Radiant Tee"(selected item for testing) in the search bar
# Locate the search bar element, then type "Radiant Tee" and press Enter
search_bar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "search")))
search_bar.send_keys("Radiant Tee")
search_bar.send_keys(Keys.RETURN)

# Click on the Radiant Tee product
# Locate and click on the link to the Radiant Tee product
radiant_tee = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='product-item-link' and contains(text(), 'Radiant Tee')]")))
radiant_tee.click()

# Select XS size
# Locate and click on the option for XS size
size_XS = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='option-label-size-143-item-166' and @option-label='XS']")))
size_XS.click()

# Select color blue (selected color for testing)
# Locate and click on the option for blue color
color_blue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='option-label-color-93-item-50' and @option-label='Blue']")))
color_blue.click()

# Enter quantity
# Locate the quantity field and enter the quantity "1" (selected amount for testing)
quantity_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "qty")))
quantity_field.clear()
quantity_field.send_keys("1")

# Add to Cart
# Locate and click on the "Add to Cart" button
add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Cart']")))
add_to_cart_button.click()

# Wait for the product to be added to the cart
# Wait for the success message indicating that the product has been added to the cart
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message-success success message']")))

# Print success message
# Print a success message to indicate that the product has been successfully added to the cart
print("Product successfully added to the cart.")

# Close the browser
# Close the browser window after completing the automation process
driver.quit()
