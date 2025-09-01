# BBC Arabic News Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Installed-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**BBC Arabic News Scraper** is a Python tool that uses [Playwright](https://playwright.dev/python/docs/intro) to scrape the latest news headlines and URLs from BBC Arabic.

---

## Features

- Scrape news headlines and URLs from BBC Arabic topics pages.
- Save scraped news into a CSV file (`data/news.csv`).
- Specify the number of news items to scrape.
- Handles dynamic content loading using Playwright.
- Works on Windows, Linux, and MacOS.

---

## Requirements

- Python 3.9 or higher
- Required Python packages:
```bash
pip install playwright pandas
playwright install
