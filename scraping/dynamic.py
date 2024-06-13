from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict

def get_html_selenium(url: str) -> str:
    driver = webdriver.Chrome()  # Make sure to have ChromeDriver installed
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def parse_html(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for item in soup.select('.gpu-rental-item'):
        gpu_model = item.select_one('.gpu-model').text
        price = item.select_one('.rental-price').text
        availability = item.select_one('.availability').text
        data.append({
            'GPU Model': gpu_model,
            'Price': price,
            'Availability': availability
        })
    return data

def scrape_data(url: str) -> pd.DataFrame:
    html = get_html_selenium(url)
    data = parse_html(html)
    return pd.DataFrame(data)

