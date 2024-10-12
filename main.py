import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "testingcode313@gmail.com"
password = "unrl ipvj uzjy wkhc"

budget = 130
product_url = "https://www.amazon.com/dp/B0C35HNPW9/ref=sbl_dpx_kitchen-electric-cookware_B08CFZF16Y_0?th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
    "DNT": "1"
}

response = requests.get(url=product_url, headers=headers)
amazon_html = response.text

soup = BeautifulSoup(amazon_html, "html.parser")


product_title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
name = (product_title.getText())


whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")

price_string = f"{whole_price.getText()}{fraction_price.getText()}"
product_price = float(price_string)

msg = f"Subject:Amazon Price Alert!\n\n{name}is now below ${budget}\n{product_url}".encode("utf-8")

if product_price < budget:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)

# To check the code Change the 'to_addrs' and add your own to get notified.
        connection.sendmail(from_addr=my_email,
                            to_addrs="oliulam03@gmail.com",
                            msg=msg)
