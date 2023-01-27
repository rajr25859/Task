# Create a web scraping script that can extract Product related information from any 2 e-commerce websites such as product names, product category and other product details along with price.
# Use the sample screenshot for your reference to generate a mapping of Product category and GST Rate. (Do not only use the sample CSV file but add your own records based on the products fetched.)

# 1. Add GST info such as GST rates by importing a csv/excel file which has a mapping of product categories and GST applicable. Add this info against each product.
# 2. Use pandas to clean / process the data
# 3. Generate insights for average GST rate by product category. Perform any 1 more anaylsis of your choice.
# 4. Scrape a list of 50 products across multiple categories.
# 5. Allow to export any one report as a csv.

# Completion of the test is defiantly a must, even if the time has elapsed and any additional features is a bonus.

import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd


gst_info = pd.read_csv('gst_rates.csv')

gst_rate = {}

with oepn('gst_rates.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        gst_rates[row[0]] == float(row[1])

def scrape_product(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    
    # print(page)
    # print(soup)
    products = []
    for product_div in soup.find_all('div', class_='product'):
        product = {}
        product['name'] = product_div.find('h3').text
        product['category'] = product_div.find('span',class_='category').text
        product['details'] = product_div.find('p',class_='details').text
        product['price'] = product_div.find('span',class_='price').text
        product['gst_rate'] = gst_rates.get(product[category],None)
        products.append(product)
        
    return products

url1 = 'https://svashudhi.com/products/'
product1 =scrape_product(url1)
url2 = 'https://www.flipkart.com/cameras/dslr-mirrorless'
product2 = scrape_product(url2)

products = product1 + product2
df= pd.DataFrame(products)
print(df)


df['price'] = df['price'].str.replace('$','').astype(float)
df['gst_rate'] = df['gst_rate'].fillna(0)

average_gst_rate_by_category = df.groupby('Category')['GST'].mean()
print(average_gst_rate_by_category)

products.to_csv('products.csv',index=False)


# _____--===================================================================================================






def scrape_product1(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    
    # print(page)
    # print(soup)

    product_names = [item.find("a").text for item in soup.find_all("div", class_="product-name")]
    product_categories = [item.find("a").text for item in soup.find_all("div", class_="product-category")]
    product_details = [item.text for item in soup.find_all("div", class_="product-details")]
    product_prices = [item.text for item in soup.find_all("div", class_="product-price")]

    products = pd.DataFrame({
        "Name":product_names,
        "Category":product_categories,
        "Details":product_details,
        "price": product_prices
    })

    products = pd.merge(products,gst_info, on="Category")       
    return products


url3 = 'https://svashudhi.com/products/'
product3 =scrape_product(url3)
url4 = 'https://www.flipkart.com/cameras/dslr-mirrorless'
product4 = scrape_product(url4)


products1 = pd.concat([product3,product4])
df1= pd.DataFrame(products1)
print(df1)

average_gst_rate_by_category = df.groupby('Category')['GST'].mean()
print(average_gst_rate_by_category)


products1.to_csv('products.csv',index=False)