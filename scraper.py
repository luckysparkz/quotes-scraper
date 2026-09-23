from patchright.async_api import Page

from quote import Quote

QUOTE_SELECTOR = ".quote"


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
    return False


async def scrape_all_quotes(page: Page) -> list[Quote]:
    await wait_for_quotes(page)
    return await extract_quotes_from_page(page)
