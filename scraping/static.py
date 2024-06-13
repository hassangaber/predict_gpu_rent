import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict

def get_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

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
    html = get_html(url)
    data = parse_html(html)
    return pd.DataFrame(data)

