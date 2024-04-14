import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

address_tag = soup.find_all("address", {"data-test": "property-card-addr"})
all_address = [address.getText(strip=True) for address in address_tag]
# print(all_address)

price_tag = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [price.getText().replace("/mo", "").split("+")[0] for price in price_tag]
# print(all_prices)

link_tag = soup.find_all(name="a", class_="property-card-link")
all_links = [link.get("href") for link in link_tag]
# print(all_links)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_address)):
    driver.get("https://forms.gle/S2f2kLW8UQ8LFQJV8")

    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(all_address[n])

    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(all_prices[n])

    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(all_links[n])

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

