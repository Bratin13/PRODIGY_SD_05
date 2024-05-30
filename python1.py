import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website to scrape
url = 'https://www.example-ecommerce.com/products'

# Send a request to fetch the HTML content
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Define a function to extract product information
def extract_product_info(product):
    name = product.find('h2', class_='product-name').text.strip()
    price = product.find('span', class_='product-price').text.strip()
    rating = product.find('div', class_='product-rating').text.strip()
    return name, price, rating

# Find all product elements on the page
products = soup.find_all('div', class_='product-item')

# Open a CSV file to write the extracted data
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Rating'])

    # Iterate over all products and extract the required information
    for product in products:
        name, price, rating = extract_product_info(product)
        writer.writerow([name, price, rating])

print("Data has been successfully extracted and saved to products.csv")
