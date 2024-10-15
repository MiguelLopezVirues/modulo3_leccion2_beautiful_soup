from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
import time
from typing import Dict
from tqdm import tqdm
import shutil
import os



def extract_atrezzo(start: int = 1, n_pages: int = 1, limit: int = 48) -> pd.DataFrame:
    """
    Extract data from atrezzo website over multiple pages.
    Create '../data/saved' directory and for each page, save page's csv into it ofr recovery in case of error.
    After completion, remove '../data/saved' folder and save final csv into '../data/scraped'.
    
    Args:
        start: The starting page number.
        n_pages: Number of pages to scrape.
        limit: Number of items per page.
        
    Returns:
        A DataFrame containing extracted data.
    """
    # create directory to save each page's csv
    os.makedirs('../data/saved', exist_ok=True)

    #create directory for final csv to process
    os.makedirs('../data/scraped', exist_ok=True)
    end = start + n_pages
    df_atrezzo = pd.DataFrame()


    for n_page in tqdm(range(start, end)):
        url_request = f"https://atrezzovazquez.es/shop.php?limit={limit}&page={n_page}"
        
        try:
            df_page = extract_atrezzo_from_page(url_request, n_page)
            df_atrezzo = pd.concat([df_atrezzo, df_page])
        except:
            # print("Error extracting page:", n_page) toggle on if debugging
            continue

        try:
            df_page.to_csv(f"../data/saved/atrezzo_saved_page{n_page}.csv")
        except:
            # print("Error saving csv:", n_page) toggle on if debugging
            continue

    
    shutil.rmtree('../data/saved')

    df_atrezzo.to_csv("../data/scraped/atrezzo_scraped.csv")

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

def get_element_info(element: BeautifulSoup) -> Dict[str, str]:
    """
    Extract name, category, section, description, dimensions and image 
    from an HTML element.
    
    Args:
        element: HTML element containing product info.
        
    Returns:
        A dictionary of extracted product details.
    """
    # time.sleep(random.random() * 2)

    dictionary = dict()

    fields = {
        "name": lambda e: e.find("a", {"class": "title"}).text.strip(),
        "category": lambda e: e.find("a", {"class": "tag"}).text.strip(),
        "section": lambda e: e.find("div", {"class": "cat-sec-box"}).text.strip(),
        "description": lambda e: e.find("p").text.strip(),
        "dimensions": lambda e: e.find("div", {"class": "price"}).find("div").text.strip(),
        "image": lambda e: e.find("div", {"class": "product-image"}).find_all("img")[0]["src"]
    }
    
    for field, extractor in fields.items():
        try:
            dictionary[field] = extractor(element)
        except Exception as ex:
            # print(f"Problem with {field}: {ex}") toggle on if debugging
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
            print(get_element_info(element))
            print(f"Error processing element on page {n_page}")
            continue

    df_page = pd.DataFrame(lista_dicts)
    df_page["page"] = n_page

    return df_page
