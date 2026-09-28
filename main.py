
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import csv

driver = webdriver.Chrome()  
url = "http://books.toscrape.com/"


try:
    driver.get(url)

    books_data = []

    #wyszukaj kategorię "Science" i kliknij w nią
    books_category = driver.find_elements(By.CSS_SELECTOR, "ul.nav-list li ul li")
    for category in books_category:
        category_name = category.find_element(By.TAG_NAME, "a").text.strip()
        if category_name == "Science":
            category.find_element(By.TAG_NAME, "a").click()
            time.sleep(2)
            break

    book_containers = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
   
    for book in book_containers:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
        availability = book.find_element(By.CSS_SELECTOR, "p.availability").text.strip()
        books_data.append([title, price, availability])


    output_dir = Path("output_files")
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(f'output_files/books.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'price', 'availability']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books_data:
            writer.writerow({'title': book[0], 'price': book[1], 'availability': book[2]})

finally:

    driver.quit()