from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import csv
import time
from selenium.common.exceptions import TimeoutException


edge_driver_path = 'D:\\Downloads\\edgedriver_win64\\msedgedriver.exe'
csv_filename = 'D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\Ma_CK.csv'
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
 # Pass the options parameter to the webdriver.Chrome constructor
service = Service(executable_path='D:\\Downloads\\edgedriver_win64\\msedgedriver.exe')
driver = Edge(service=service, options=edge_options)

with open(csv_filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        #ATS missing
        # Assuming the data in the CSV is in the first column
        stock_code = row[0]
        # Construct the URL with the stock code
        url = f'https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-{stock_code}.html?_des_tab=2'
        print(f"Processing stock code: {stock_code}")
        # Navigate to the URL
        driver.get(url)
        select_element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "cboNhomTinBaoCaoDK"))
    )
        # Select "Báo cáo thường niên" from the dropdown
        select = Select(driver.find_element(By.ID,"cboNhomTinBaoCaoDK"))
        select.select_by_value("ANN_REPORT")

    # Click the "Tìm kiếm" button
        search_button = driver.find_element(By.ID,"btn_searchBaoCaoDK")
        search_button.click()
        try: 
            baocao_thuongnien_link = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.LINK_TEXT, "Báo cáo thường niên 2022"))
     )
            baocao_thuongnien_link.click()
            
        except TimeoutException:
    # Handle the case when the link is not found within the specified timeout
            print("Báo cáo thường niên 2022 link not found. Skipping...")
            continue
 

# Click Báo cáo thường niên 2022:
        baocao_thuongnien_link = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.LINK_TEXT, "Báo cáo thường niên 2022"))
     )
        baocao_thuongnien_link.click()

# Wait for the links to appear after clicking on "Báo cáo thường niên 2022"
# You may need to adjust the waiting conditions based on the actual behavior of the page
#link_elements = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, '//a[@class="hrefViewDetail"]'))
#)

# Extract the links
#pdf_links = [link.get_attribute("href") for link in link_elements]

        file_attach_div = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "divLstFileAttach"))
     )

# Extract links containing "pdf"
        pdf_links = []
        for link_element in file_attach_div.find_elements(By.XPATH,'.//a[contains(@href, "pdf")]'):
          pdf_links.append(link_element.get_attribute("href"))

# Write the links to a CSV file
        csv_filename = 'D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\crawl2.csv'
        with open(csv_filename, 'a', newline='') as csvfile:
             csv_writer = csv.writer(csvfile)
             # Write new rows for each link
             for link in pdf_links:
                 csv_writer.writerow([stock_code,link])
                 
driver.quit()

time.sleep(2)

# Close the browser
#driver.quit()

#url = 'https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-ADC.html?_des_tab=2'
#'https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-AAV.html?_des_tab=2'

# Set up Chrome options
