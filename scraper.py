import logging

from patchright.async_api import Page

from quote import Quote

QUOTE_SELECTOR = ".quote"

logger = logging.getLogger(__name__)


async def wait_for_quotes(page: Page) -> None:
    await page.wait_for_selector(QUOTE_SELECTOR)


async def extract_quotes_from_page(page: Page) -> list[Quote]:
    quotes = []
    quote_elements = await page.locator(QUOTE_SELECTOR).all()

    for element in quote_elements:
        text = await element.locator(".text").inner_text()
        author = await element.locator(".author").inner_text()
        tags = await element.locator(".tag").all_inner_texts()
        quote = Quote(text, author, tags)
        quotes.append(quote)

    return quotes


async def go_to_next_page(page: Page) -> bool:
    button = page.get_by_role("link", name="Next")

    if await button.count() == 0:
        return False

    await button.click()
    return True


async def scrape_all_quotes(page: Page) -> list[Quote]:
    all_quotes = []
    page_number = 1

    while True:
        await wait_for_quotes(page)
        page_quotes = await extract_quotes_from_page(page)
        all_quotes.extend(page_quotes)
        logger.info(f"Page {page_number}: found {len(page_quotes)} quotes")

        has_next = await go_to_next_page(page)
        if not has_next:
            break

        page_number += 1

    return all_quotes
