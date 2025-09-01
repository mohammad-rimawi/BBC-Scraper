from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict
import pandas as pd
import os

@dataclass
class News:
    title: str = None
    url: str = None

def main():
    nom = int(input("Enter the number of news items you need: "))
    all_news = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page()
        page.goto("https://www.bbc.com/arabic/topics/cv2xyrnr8dnt", timeout=60000)

        while len(all_news) < nom:
            page.wait_for_timeout(2000)

            news_blocks = page.locator('//li[@class="bbc-t44f9r"]')
            count = news_blocks.count()

            for i in range(count):
                if len(all_news) >= nom:
                    break

                try:
                    news_element = news_blocks.nth(i)
                    title = news_element.locator('xpath=.//h2/a').inner_text()
                    url = news_element.locator('a').get_attribute('href')

                    if url and url.startswith("/"):
                        url = "https://www.bbc.com" + url

                    news = News(title=title, url=url)
                    all_news.append(news)

                except Exception as e:
                    print(f"Error processing item {i}: {e}")

           
            break

        browser.close()

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame([asdict(news) for news in all_news])
    df.to_csv("data/news.csv", index=False, encoding='utf-8-sig')
    print(f" {len(all_news)} news items saved to data/news.csv")

if __name__ == "__main__":
    main()
