import asyncio
import logging

from patchright.async_api import async_playwright

from logging_config import setup_logging
from scraper import scrape_all_quotes
from storage import save_to_csv

BASE_URL = "https://quotes.toscrape.com/js"

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging()
    logger.info("Starting scraper")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page()

            await page.goto(BASE_URL)
            quotes = await scrape_all_quotes(page)
            logger.info(f"Scraped {len(quotes)} quotes")
            save_to_csv(quotes)
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
