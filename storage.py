import csv
import logging
from dataclasses import fields

from quote import Quote

logger = logging.getLogger(__name__)
csv_fieldnames = [f.name for f in fields(Quote)]


def quote_to_row(quote: Quote) -> dict[str, str]:
    return {"text": quote.text, "author": quote.author, "tags": ", ".join(quote.tags)}


def save_to_csv(quotes: list[Quote], filepath: str = "quotes.csv") -> None:
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fieldnames)
        writer.writeheader()

        for quote in quotes:
            writer.writerow(quote_to_row(quote))

    logger.info(f"Saved {len(quotes)} quotes to {filepath}")
