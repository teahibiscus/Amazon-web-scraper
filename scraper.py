import requests
from bs4 import BeautifulSoup # pulls data out of HTML and XML files

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url: str) -> dict:
    product_details = {}
    # get product page content and create a soup
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features='lxml')

    try:
        # extract product name
        title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
        extracted_price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip()
        price = '$' + extracted_price.split('$')[1]

        product_details['title'] = title
        product_details['price'] = price

        return product_details
    except Exception as e:
        print(f"Failed with exception: {e}")
        print("Could not fetch product details")

product_url = input("Enter the product URL: ")
product_details = get_product_details(product_url)
print("Product Details: " + str(product_details))