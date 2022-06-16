import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def scrapper(url):
    df = pd.read_html(url)
    csv = df[0]
    print(type(csv))
    csv.to_csv("taiyo.csv")

url = "https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid"
scrapper(url)

data = pd.read_csv("taiyo.csv")
print(data)