import time
from scraper import fetch_page
from parser import parse_pagination, parse_apartments
from exporter import save_to_gs, save_to_xlsx


def main():
    first_page_html = fetch_page(1)
    total_pages = parse_pagination(first_page_html)

    def apartments_generator():
        for page in range(1, total_pages + 1):
            html = fetch_page(page)
            yield from parse_apartments(html)
            time.sleep(3)

    save_to_gs(apartments_generator())  # If you want to save result to Google Drive
    #save_to_xlsx(apartments_generator()) # If you want to save result to your computer


if __name__ == "__main__":
    main()
