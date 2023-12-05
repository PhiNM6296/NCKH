from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions
import csv 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
options = ChromeOptions()
options.headless=True
# Pass the options parameter to the webdriver.Chrome constructor
service = Service(executable_path='D:\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver = Chrome(service=service, options=options)

# Navigate to the URL
url = "https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-AAV.html?_des_tab=2"
driver.get(url)

# Find links containing "bao_cao_tai_chinh" and "pdf"
keyword1 = "Bao_cao_thuong_nien"
keyword2 = "pdf"
links = driver.find_elements_by_css_selector(f'a[href*="{keyword1}"][href*="{keyword2}"]')

# Print and save links to a CSV file
with open('D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\CEOStuff\\csvoutput.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Links'])

    for link in links:
        link_href = link.get_attribute('href')
        print(link_href)
        csvwriter.writerow([link_href])

# Close the browser
driver.quit()
