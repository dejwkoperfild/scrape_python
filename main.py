
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  

try:
    driver.get("http://books.toscrape.com/")
    
    
    time.sleep(2) 

    books_data = []
    
    
    book_containers = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

   
    for book in book_containers:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        
        
        price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
        
        
        availability = book.find_element(By.CSS_SELECTOR, "p.availability").text.strip()
        
        books_data.append([title, price, availability])
        print(f"Pobrano: {title} | {price}")

finally:

    driver.quit()