from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver
webdriver_path = "/Users/hammad/Downloads/edgedriver_mac64_m1/msedgedriver"  # Replace with your actual path

# Set up the Edge driver
service = Service(webdriver_path)
driver = webdriver.Edge(service=service)

# Open the website
url = "http://10.1.56.5:8080/#library_id=Calibre_Library&panel=book_list"  # Replace with your actual URL


# Open the webpage
driver.get(url)

# Wait for JavaScript to load the content (adjust the sleep time as needed)
time.sleep(5)  # This is a simple way, but you can use WebDriverWait for more precision

# Get the page source after the page has loaded
html = driver.page_source


# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(html, 'html.parser')

# Now you can find the container with all the books
container = soup.find("div", class_="book-list-container")
if container:
    # Find the grid with books inside the container
    grid = container.find("div", class_="book-list-cover-grid")
    if grid:
        # Find all book links (a tags with class "book-list-item")
        books = grid.find_all("a", class_="book-list-item")
        book_data = []
        # Extract book IDs and titles
        for book in books:
            book_id = book.get("data-book-id")
            title = book.get("title")
            if book_id and title:
                book_data.append({"id": book_id, "title": title})

        # Print the extracted book data
        for book in book_data:
            print(f"ID: {book['ID']}, Title: {book['title']}")
    else:
        print("No book list grid found.")
else:
    print("No book list container found.")

# Close the browser session
driver.quit()