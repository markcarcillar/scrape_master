import requests
from bs4 import BeautifulSoup
import json
import csv
from xml.etree import ElementTree as ET

url = 'https://markcarcillar.github.io/scrape_master/'  
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    product_divs = soup.find_all('div', class_='product')
    product_data = []
    for product_div in product_divs:
        product = {}
        product['name'] = product_div.find('h3', class_='product-name').text
        product['details'] = product_div.find('p', class_='product-details').text
        product['price'] = product_div.find('p', class_='product-price').text
        product['reviews'] = product_div.find('span', class_='review-count').text.strip('()')
        product_data.append(product)

    # Choose the output format (XML, JSON, CSV)
    output_format = input("Choose the output format (XML, JSON, CSV): ").strip().lower()

    if output_format == 'json':
        # Save data as JSON
        with open('output/products.json', 'w') as json_file:
            json.dump(product_data, json_file, indent=4)
        print('Data saved as JSON.')

    elif output_format == 'xml':
        # Create an XML element for each product
        root = ET.Element('products')
        for product in product_data:
            product_element = ET.SubElement(root, 'product')
            for key, value in product.items():
                ET.SubElement(product_element, key).text = value

        # Save data as XML
        xml_tree = ET.ElementTree(root)
        xml_tree.write('output/products.xml')
        print('Data saved as XML.')

    elif output_format == 'csv':
        # Save data as CSV
        with open('output/products.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=product_data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(product_data)
        print('Data saved as CSV.')

    else:
        print('Invalid output format. Choose from XML, JSON, CSV.')
else:
    print('Failed to retrieve the webpage. Check the URL and try again.')
