from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
import time
from typing import Dict
from tqdm import tqdm

def extract_atrezzo(start: int = 1, n_pages: int = 1, limit: int = 48) -> pd.DataFrame:
    """
    Extract data from atrezzo website over multiple pages.
    
    Args:
        start: The starting page number.
        n_pages: Number of pages to scrape.
        limit: Number of items per page.
        
    Returns:
        A DataFrame containing extracted data.
    """
    end = start + n_pages
    df_atrezzo = pd.DataFrame()
    
    for n_page in tqdm(range(start, end)):
        url_request = f"https://atrezzovazquez.es/shop.php?limit={limit}&page={n_page}"
        
        try:
            df_page = extract_atrezzo_from_page(url_request, n_page)
            df_atrezzo = pd.concat([df_atrezzo, df_page])
        except:
            print("Error extracting page:", n_page)
            continue

    return df_atrezzo

def request_parse(url: str) -> BeautifulSoup:
    """
    Request and parse HTML from a given URL.
    
    Args:
        url: The webpage URL.
        
    Returns:
        Parsed HTML content as BeautifulSoup object.
    """
    try:
        response = requests.get(url)
    except:
        print(f"Bad request for URL: {url}")
        return None

    try:
        response_html = BeautifulSoup(response.content, "html.parser")
    except:
        print(f"Failed to parse HTML for: {url}")
        return None

    return response_html

def get_element_info_sub():

def get_element_info(element: BeautifulSoup) -> Dict[str, str]:
    """
    Extract product information from an HTML element.
    
    Args:
        element: HTML element containing product info.
        
    Returns:
        A dictionary of extracted product details.
    """
    # time.sleep(random.random() * 2)
    
    sub_element_info = {
        "name": element.find("a", {"class": "title"}).text.strip(),
        "category": element.find("a", {"class": "tag"}).text.strip(),
        "section": element.find("div", {"class": "cat-sec"}).text.strip(),
        "description": element.find("p").text.strip(),
        "dimensions": element.find("div", {"class": "price"}).find("div").text.strip(),
        "image": element.find("div", {"class": "product-image"}).find_all("img")[0]["src"]
    }
    
    dictionary = dict()
    for field, info in sub_element_info.items():
        try:
            dictionary[field] = info
        except:
            dictionary[field] = np.nan
    return dictionary

def extract_atrezzo_from_page(url: str, n_page: int) -> pd.DataFrame:
    """
    Extracts product data from a single page.
    
    Args:
        url: URL of the page to scrape.
        n_page: The page number for tracking purposes.
        
    Returns:
        A DataFrame with extracted product information.
    """
    lista_dicts = list()

    response_html = request_parse(url)
    if response_html is None:
        return pd.DataFrame()

    elements = response_html.find_all("div", {"class": "col-md-3 col-sm-4 shop-grid-item"})

    for element in elements:
        try:
            lista_dicts.append(get_element_info(element))
        except:
            print(f"Error processing element on page {n_page}")
            continue

    df_page = pd.DataFrame(lista_dicts)
    df_page["page"] = n_page

    return df_page
