import requests
from bs4 import BeautifulSoup

def simple_web_crawler(url, depth=2):
    visited_urls = set()

    def crawl(current_url, current_depth):
        if current_depth > depth or current_url in visited_urls:
            return

        print("Crawling:", current_url)

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract information or perform actions with the parsed HTML
                # Example: Print the title of the page
                title = soup.title.text.strip()
                print("Title:", title)

                # Add the current URL to the set of visited URLs
                visited_urls.add(current_url)

                # Extract links and recursively crawl them
                links = soup.find_all('a', href=True)
                for link in links:
                    next_url = link['href']
                    crawl(next_url, current_depth + 1)

        except Exception as e:
            print(f"Error crawling {current_url}: {str(e)}")

    crawl(url, 0)

# Example usage:
if __name__ == "__main__":
    start_url = "https://www.phonearena.com/phones"
    simple_web_crawler(start_url)