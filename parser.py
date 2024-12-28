from bs4 import BeautifulSoup


def parse_pagination(html: str) -> int:
    """Extracts the number of pages from the HTML."""
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find("div", class_="serp-pagination-wrap-new")
    return int(pagination.find_all("a", class_="active")[-1].text)


def parse_apartments(html: str):
    """Extracts apartment data from HTML."""
    soup = BeautifulSoup(html, "lxml")
    apartments = soup.find_all("div", class_="prop-card ng-star-inserted")
    for apartment in apartments:
        link = apartment.find_next('a')['href']
        apartment_id = apartment.find_next("div", class_="tw-text-xs tw-text-white text--semibold").text
        apartment_price = int(apartment.find_next('span').text[:-1].replace('.', '').strip())
        description = apartment.find_next("div", class_="property-card__place").text
        yield apartment_id, apartment_price, description, link
