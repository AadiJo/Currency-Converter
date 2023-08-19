from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse

def main():
    from_ = input("From: ")
    to_ = input("To: ")
    amount = float(input("Amount: "))

    url = f"https://www.x-rates.com/calculator/?from={from_}&to={to_}&amount=1/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    try:
        rate = float(doc.select("span.ccOutputRslt")[0].text.strip(f" {to_}"))

    except ValueError:
        print("\nInvalid currency")
        exit()

    print("\n%.2f" % amount + f" {from_} = " + str(round(rate * amount, 2)) + f" {to_}")


if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        print("\n\nExiting...")