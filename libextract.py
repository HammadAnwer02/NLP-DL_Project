from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time
from dotenv import load_dotenv
# Set up the Selenium WebDriver
webdriver_path =  os.getenv("WEB_DRIVER_PATH") 

# Set up the Edge driver
service = Service(webdriver_path)
driver = webdriver.Edge(service=service)

# Open the website
url = "http://10.1.56.5:8080/#library_id=Calibre_Library&panel=book_list"  # Replace with your actual URL
driver.get(url)

# Wait for JavaScript to load the content
time.sleep(5)  # Adjust the sleep time if needed

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

        # Create a directory to save the downloaded books
        output_dir = "Downloaded_Books"
        os.makedirs(output_dir, exist_ok=True)

        # Download each book
        base_url = "http://10.1.56.5:8080/get/PDF"
        for book in book_data:
            book_id = book["id"]
            title = book["title"].replace("/", "-")  # Replace problematic characters
            download_url = f"{base_url}/{book_id}/Calibre_Library"
            print(f"Downloading {title} from {download_url}...")

            # Use requests to download the PDF
            try:
                response = requests.get(download_url, stream=True)
                if response.status_code == 200:
                    file_path = os.path.join(output_dir, f"{title}.pdf")
                    with open(file_path, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Successfully downloaded: {title}")
                else:
                    print(f"Failed to download {title}. HTTP Status Code: {response.status_code}")
            except Exception as e:
                print(f"An error occurred while downloading {title}: {e}")
    else:
        print("No book list grid found.")
else:
    print("No book list container found.")

# Close the browser session
driver.quit()