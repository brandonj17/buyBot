from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Driver to use Chrome 
web_browser = webdriver.Chrome(PATH)

# Dummy Page for testing 
# web_browser.get("https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508")

# Product to Buy 
web_browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

SoldOut = True

while SoldOut:
    try:
        add_to_cart = addButton = web_browser.find_element_by_class_name('btn-disabled')
        print('Sold Out')
        time.sleep(1)
        web_browser.refresh()
    except:
        add_to_cart = addButton = web_browser.find_element_by_class_name('btn-primary')
        print('Button Clicked')
        add_to_cart.click()
        SoldOut = False