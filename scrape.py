import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")
    chrome_driver_path = "./chromedriver.exe"  # Path to your ChromeDriver

    # Correct initialization of ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Setting headless mode here

    # Correcting service instantiation
    service = Service(chrome_driver_path)
    
    # Launch Chrome with the service and options
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source

        return html
    finally:
        driver.quit()

# Example usage
website_url = "https://example.com"
html_content = scrape_website(website_url)
print(html_content)

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup.find_all(["script", "style"]):
        script_or_style.decompose()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]
