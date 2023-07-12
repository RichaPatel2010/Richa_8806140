from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to Amazon.com
driver.get("https://www.amazon.com")
wait = WebDriverWait(driver, 20)

# Find the search input field and enter a search query
search_input = driver.find_element(By.ID, "twotabsearchtextbox")
search_input.send_keys("mobile")

# Click the search button
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

Todays_Deal = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/gp/goldbox?ref_=nav_cs_gb')]")))
Todays_Deal.click()

Customer_Service = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='nav-xshop']//a[contains(@class,'')][normalize-space()='Customer Service']")))
Customer_Service.click()

Registry = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Registry']")))
Registry.click()

# Wait for the search results to load
#wait = WebDriverWait(driver, 20)
#search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']")))

# Click on the first search result
#first_result = search_results[0]
#first_result.click()

# Add the item to the cart
#add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
#add_to_cart_button.click()

# Wait for the cart count to update
#wait.until(EC.text_to_be_present_in_element((By.ID, "nav-cart-count"), "1"))

# View the cart
#view_cart_button = driver.find_element(By.ID, "nav-cart")
#view_cart_button.click()

# Perform an assertion to check if the item is in the cart
#cart_item_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sc-product-title")))
#assert "Laptop" in cart_item_title.text

# Proceed to checkout
#checkout_button = driver.find_element(By.NAME, "proceedToRetailCheckout")
#checkout_button.click()

# Close the browser window
driver.quit()
