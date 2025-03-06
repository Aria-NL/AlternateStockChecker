from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os
from playsound import playsound

# Set up Firefox options
firefox_options = Options()
firefox_options.binary_location = "C:\\path\\to\\firefox\\firefox.exe" # REPLACE THIS WITH THE PATH TO YOUR FIREFOX.EXE, YOU CAN ALSO USE FIREFOX FORKS LIKE WATERFOX OR FLOORP
# usually the path is C:\\Program Files\\Mozilla Firefox\\firefox.exe but it can vary depending on your installation

# Initialize the webdriver
driver = webdriver.Firefox(options=firefox_options, service=Service(r'C:\\path\\to\\geckodriver\\geckodriver.exe')) # REPLACE THIS WITH THE PATH TO YOUR GECKODRIVER.EXE

# URL to monitor
url = "https://www.alternate.nl/PowerColor/Radeon-RX-9070-XT-Reaper-16GB-GDDR6-grafische-kaart/html/product/1935817" # REPLACE THIS WITH ANY ALTERNATE.NL PRODUCT URL

# Text to search for
in_stock_text = "Op voorraad"
out_of_stock_texts = ["De beschikbare voorraad is momenteel gereserveerd", "Uitverkocht"]

def check_stock():
    # Get page source
    html = driver.page_source
    
    # Check if product is in stock
    if in_stock_text in html:
        return True
    # Check if product is out of stock
    for text in out_of_stock_texts:
        if text in html:
            return False
    return False  # Default to false if neither text is found

def main():
    try:
        # Open the webpage
        driver.get(url)
        
        while True:
            if check_stock():
                print("Product is in stock!")
                # close the browser first
                driver.quit()
                os.system(f"start firefox {url}") # REPLACE "firefox" WITH THE NAME OF YOUR FIREFOX FORK (E.G. "waterfox" or "floorp") IF YOU ARE USING ONE
                # Play sound (adjust path to your audio file)
                playsound('alert.wav')  # Make sure to have an alert.wav file in the same directory. Recommend something very loud, or you can use the one I've provided. Headphone users beware!        
                break
            else:
                print("Product still out of stock, refreshing...")
                sleep(3)  # Wait 1 second before refreshing
                driver.refresh()
                
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()