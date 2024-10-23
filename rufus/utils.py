import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_page(url):
    """
    Fetches the content of a given URL.
    
    Args:
        url (str): The URL of the page to fetch.

    Returns:
        str: The HTML content of the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {url}, Error: {str(e)}")
        return None


def parse_html(html):
    """
    Parses the HTML content and returns a BeautifulSoup object.
    
    Args:
        html (str): The HTML content of a webpage.
        
    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML.
    """
    return BeautifulSoup(html, 'html.parser')


def extract_links(soup, base_url):
    """
    Extracts all hyperlinks from a BeautifulSoup object and makes them absolute.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML.
        base_url (str): The base URL of the webpage.

    Returns:
        list: A list of absolute URLs found on the page.
    """
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        links.add(full_url)
    return list(links)


def extract_text(soup):
    """
    Extracts the text content from a BeautifulSoup object, removing scripts and styles.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML.

    Returns:
        str: The cleaned text content of the page.
    """
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator=' ', strip=True)
    return text


def crawl_and_extract(url, depth=1):
    """
    Crawls a website starting from the given URL, extracting text content up to the specified depth.

    Args:
        url (str): The starting URL for crawling.
        depth (int): The number of levels deep to crawl (default is 1).

    Returns:
        dict: A dictionary containing the URL and extracted text.
    """
    visited_urls = set()
    to_visit = [url]
    extracted_data = {}

    for _ in range(depth):
        next_level = []

        for current_url in to_visit:
            if current_url in visited_urls:
                continue

            html = fetch_page(current_url)
            if not html:
                continue

            soup = parse_html(html)
            text_content = extract_text(soup)
            extracted_data[current_url] = text_content

        
            links = extract_links(soup, current_url)
            next_level.extend(links)

            visited_urls.add(current_url)

        to_visit = next_level

    return extracted_data
